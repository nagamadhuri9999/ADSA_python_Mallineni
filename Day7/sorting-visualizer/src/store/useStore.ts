import { create } from 'zustand';

// Types and Interfaces
export type ColorState = 'default' | 'comparing' | 'swapping' | 'pivot' | 'sorted' | 'minimum';

export interface ArrayElement {
  id: string;
  value: number;
  state: ColorState;
}

export interface AlgorithmMetrics {
  timeComplexity: { best: string, avg: string, worst: string };
  spaceComplexity: string;
}

export interface AnimationFrame {
  array: ArrayElement[];
  activeLine: number;
  explanation: string;
  callStack: string[];
  comparisons: number;
  swaps: number;
  isComplete?: boolean;
}

interface VisualizerState {
  // Core State
  array: ArrayElement[];
  
  // Teaching State
  activeLine: number;
  explanation: string;
  callStack: string[];
  comparisons: number;
  swaps: number;
  isComplete: boolean;
  
  // Config & UI
  codeSnippet: string;
  metrics: AlgorithmMetrics | null;
  isPlaying: boolean;
  speed: number;
  arraySize: number;
  mode: 'visualize' | 'learn';
  algorithmName: string;
  theme: 'dark' | 'light';
  
  // Frame Engine
  frames: AnimationFrame[];
  currentFrameIdx: number;
  
  // Actions
  generateArray: () => void;
  setArraySize: (size: number) => void;
  setSpeed: (speed: number) => void;
  setMode: (mode: 'visualize' | 'learn') => void;
  setAlgorithm: (name: string, snippet: string, metrics: AlgorithmMetrics) => void;
  setFrames: (frames: AnimationFrame[]) => void;
  playPause: () => void;
  stepForward: () => void;
  stepBackward: () => void;
  reset: () => void;
  applyFrame: (idx: number) => void;
  toggleTheme: () => void;
}

const generateRandomArray = (size: number): ArrayElement[] => {
  return Array.from({ length: size }, (_, i) => ({
    id: `val-${Math.random()}-${i}`,
    value: Math.floor(Math.random() * 400) + 50,
    state: 'default' as ColorState
  }));
};

export const useStore = create<VisualizerState>((set, get) => ({
  array: [],
  activeLine: -1,
  explanation: "Select an algorithm to begin.",
  callStack: [],
  comparisons: 0,
  swaps: 0,
  isComplete: false,
  
  codeSnippet: "",
  metrics: null,
  isPlaying: false,
  speed: 300,
  arraySize: 15,
  mode: 'visualize',
  algorithmName: "None",
  theme: (localStorage.getItem('theme') as 'dark' | 'light') || 'dark',
  
  frames: [],
  currentFrameIdx: 0,

  generateArray: () => {
    const size = get().arraySize;
    set({
      array: generateRandomArray(size),
      activeLine: -1,
      explanation: "Array generated. Ready to sort.",
      callStack: [],
      comparisons: 0,
      swaps: 0,
      frames: [],
      currentFrameIdx: 0,
      isPlaying: false,
      isComplete: false,
    });
  },

  setArraySize: (size) => set({ arraySize: size }),
  setSpeed: (speed) => set({ speed }),
  setMode: (mode) => set({ mode }),
  
  setAlgorithm: (name, snippet, metrics) => set({ 
    algorithmName: name, 
    codeSnippet: snippet, 
    metrics,
    frames: [],
    currentFrameIdx: 0,
    isPlaying: false
  }),
  
  setFrames: (frames) => {
    set({ frames, currentFrameIdx: 0, isPlaying: true, isComplete: false });
    get().applyFrame(0);
  },

  playPause: () => set((state) => ({ isPlaying: !state.isPlaying })),
  
  stepForward: () => {
    const { currentFrameIdx, frames, applyFrame } = get();
    if (currentFrameIdx < frames.length - 1) {
      const nextIdx = currentFrameIdx + 1;
      set({ currentFrameIdx: nextIdx });
      applyFrame(nextIdx);
    } else {
      set({ isPlaying: false, isComplete: true });
    }
  },

  stepBackward: () => {
    const { currentFrameIdx, applyFrame } = get();
    if (currentFrameIdx > 0) {
      const prevIdx = currentFrameIdx - 1;
      set({ currentFrameIdx: prevIdx, isComplete: false });
      applyFrame(prevIdx);
    }
  },
  
  reset: () => {
    set({ isPlaying: false, currentFrameIdx: 0, isComplete: false });
    get().applyFrame(0);
  },

  applyFrame: (idx) => {
    const { frames } = get();
    const frame = frames[idx];
    if (!frame) return;

    set({
      array: frame.array,
      activeLine: frame.activeLine,
      explanation: frame.explanation,
      callStack: frame.callStack,
      comparisons: frame.comparisons,
      swaps: frame.swaps,
      isComplete: frame.isComplete || false
    });
  },

  toggleTheme: () => {
    const newTheme = get().theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', newTheme);
    set({ theme: newTheme });
  }
}));
