import { create } from 'zustand';
import type { Edge, Node } from '@xyflow/react';

export type CallStackFrame = {
  id: string;
  functionName: string;
  parameters: string;
  localVars: string;
  status: string;
};

export type TraceStep = {
  id: string; // Unique ID for the step
  type: 'divide' | 'merge' | 'compare' | 'swap' | 'base_case' | 'completed' | 'partition';
  activeIndices: number[]; // Indices currently being operated on
  array: number[]; // Full array state at this point
  
  // Call Stack State
  callStack: CallStackFrame[];
  
  // Recursion Tree State
  treeNodes: Node[];
  treeEdges: Edge[];
  
  // Code Execution State
  activeLine: number;
  
  // Intuition / Explanation State
  explanationTitle: string;
  explanationText: string;
  
  // Specialized visualization state
  partitions?: { startIndex: number, endIndex: number }[];
  pivotIndex?: number;
  pointerIndices?: number[]; // [i, j] pointers for quick sort
};

type AlgorithmType = 'merge' | 'quick';

interface AppState {
  algorithm: AlgorithmType;
  setAlgorithm: (algo: AlgorithmType) => void;
  
  array: number[];
  setArray: (arr: number[]) => void;
  
  traces: TraceStep[];
  setTraces: (traces: TraceStep[]) => void;
  
  currentTraceIndex: number;
  setCurrentTraceIndex: (index: number) => void;
  nextStep: () => void;
  prevStep: () => void;
  
  isPlaying: boolean;
  setIsPlaying: (playing: boolean) => void;
  
  playbackSpeed: number;
  setPlaybackSpeed: (speed: number) => void;
  
  theme: 'dark' | 'light';
  toggleTheme: () => void;
  
  generateNewArray: (size: number) => void;
}

export const useStore = create<AppState>((set) => ({
  algorithm: 'merge',
  setAlgorithm: (algo) => set({ algorithm: algo }),
  
  array: [],
  setArray: (arr) => set({ array: arr }),
  
  traces: [],
  setTraces: (traces) => set({ traces, currentTraceIndex: 0 }),
  
  currentTraceIndex: 0,
  setCurrentTraceIndex: (index) => set({ currentTraceIndex: index }),
  
  nextStep: () => set((state) => ({ 
    currentTraceIndex: Math.min(state.currentTraceIndex + 1, state.traces.length - 1) 
  })),
  
  prevStep: () => set((state) => ({ 
    currentTraceIndex: Math.max(state.currentTraceIndex - 1, 0) 
  })),
  
  isPlaying: false,
  setIsPlaying: (playing) => set({ isPlaying: playing }),
  
  playbackSpeed: 500,
  setPlaybackSpeed: (speed) => set({ playbackSpeed: speed }),
  
  theme: 'dark',
  toggleTheme: () => set((state) => ({ theme: state.theme === 'dark' ? 'light' : 'dark' })),
  
  generateNewArray: (size) => {
    const newArr = Array.from({ length: size }, () => Math.floor(Math.random() * 100) + 1);
    set({ array: newArr });
  }
}));
