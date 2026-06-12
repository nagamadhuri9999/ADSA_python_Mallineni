import { create } from 'zustand';

export const useStore = create((set, get) => ({
  // Core Array State
  array: [],
  colors: [],
  
  // Teaching State
  activeLine: -1,
  explanation: "Select an algorithm and click Play to begin.",
  callStack: [],
  comparisons: 0,
  swaps: 0,
  
  // UI & Config State
  codeSnippet: "",
  isPlaying: false,
  speed: 300,
  arraySize: 15,
  mode: 'visualize', // 'visualize' or 'learn'
  algorithmName: "None",
  
  // Animation State
  frames: [],
  currentFrameIdx: 0,

  // Actions
  generateArray: () => {
    const size = get().arraySize;
    const newArray = Array.from({ length: size }, () => Math.floor(Math.random() * 400) + 50);
    set({
      array: newArray,
      colors: new Array(size).fill('rgba(255, 255, 255, 0.8)'),
      activeLine: -1,
      explanation: "Array generated. Ready to sort.",
      callStack: [],
      comparisons: 0,
      swaps: 0,
      frames: [],
      currentFrameIdx: 0,
      isPlaying: false,
    });
  },

  setArraySize: (size) => set({ arraySize: size }),
  setSpeed: (speed) => set({ speed }),
  setMode: (mode) => set({ mode }),
  setAlgorithm: (name, snippet) => set({ algorithmName: name, codeSnippet: snippet }),
  
  setFrames: (frames) => {
    set({ frames, currentFrameIdx: 0, isPlaying: true });
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
      set({ isPlaying: false });
    }
  },

  stepBackward: () => {
    const { currentFrameIdx, applyFrame } = get();
    if (currentFrameIdx > 0) {
      const prevIdx = currentFrameIdx - 1;
      set({ currentFrameIdx: prevIdx });
      applyFrame(prevIdx);
    }
  },

  applyFrame: (idx) => {
    const { frames } = get();
    const frame = frames[idx];
    if (!frame) return;

    set({
      array: frame.array,
      colors: frame.colors,
      activeLine: frame.activeLine !== undefined ? frame.activeLine : -1,
      explanation: frame.explanation || "",
      callStack: frame.callStack || [],
      comparisons: frame.comparisons || 0,
      swaps: frame.swaps || 0,
    });
  }
}));
