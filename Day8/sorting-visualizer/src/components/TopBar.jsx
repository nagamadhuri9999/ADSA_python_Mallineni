import React from 'react';
import { useStore } from '../store/useStore';
import { Play, Pause, RefreshCw } from 'lucide-react';
import { getBubbleSortAnimations, BUBBLE_SORT_CODE } from '../algorithms/bubbleSort';
import { getMergeSortAnimations, MERGE_SORT_CODE } from '../algorithms/mergeSort';

export default function TopBar() {
  const { 
    generateArray, arraySize, setArraySize, speed, setSpeed, 
    isPlaying, playPause, mode, setMode, setAlgorithm, setFrames
  } = useStore();

  const runAlgorithm = (name, fn, code) => {
    setAlgorithm(name, code);
    const array = useStore.getState().array;
    const animations = fn(array);
    setFrames(animations);
  };

  return (
    <div className="bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-4 flex flex-wrap items-center justify-between gap-4">
      <div className="flex items-center gap-4">
        <h1 className="text-xl font-black bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent tracking-tight">
          DSA Visualizer Pro
        </h1>
        <div className="h-6 w-px bg-slate-600 mx-2"></div>
        
        {/* Array Size */}
        <div className="flex flex-col gap-1">
          <label className="text-xs font-bold text-slate-400 uppercase">Array Size: {arraySize}</label>
          <input type="range" min="5" max="50" value={arraySize} 
                 onChange={(e) => setArraySize(Number(e.target.value))}
                 className="w-24 accent-blue-500" />
        </div>

        {/* Speed */}
        <div className="flex flex-col gap-1">
          <label className="text-xs font-bold text-slate-400 uppercase">Speed: {speed}ms</label>
          <input type="range" min="10" max="1000" value={speed} 
                 onChange={(e) => setSpeed(Number(e.target.value))}
                 className="w-24 accent-purple-500" />
        </div>

        <button onClick={generateArray} className="ml-2 flex items-center gap-2 px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm font-semibold transition-colors">
          <RefreshCw size={16} /> New Array
        </button>
      </div>

      <div className="flex items-center gap-4">
        {/* Mode Toggle */}
        <div className="flex bg-slate-900 rounded-lg p-1">
          <button onClick={() => setMode('visualize')} className={`px-4 py-1 text-sm font-bold rounded-md transition-colors ${mode === 'visualize' ? 'bg-blue-500 text-white' : 'text-slate-400 hover:text-white'}`}>
            Visualize
          </button>
          <button onClick={() => setMode('learn')} className={`px-4 py-1 text-sm font-bold rounded-md transition-colors ${mode === 'learn' ? 'bg-purple-500 text-white' : 'text-slate-400 hover:text-white'}`}>
            Learn
          </button>
        </div>

        {/* Play/Pause */}
        <button onClick={playPause} className={`flex items-center justify-center w-10 h-10 rounded-full transition-transform hover:scale-105 shadow-lg ${isPlaying ? 'bg-red-500 hover:bg-red-400' : 'bg-green-500 hover:bg-green-400'}`}>
          {isPlaying ? <Pause fill="currentColor" size={18} /> : <Play fill="currentColor" size={18} className="ml-1" />}
        </button>

        {/* Algorithms */}
        <div className="flex gap-2 border-l border-slate-700 pl-4">
          <button onClick={() => runAlgorithm("Bubble Sort", getBubbleSortAnimations, BUBBLE_SORT_CODE)} className="px-4 py-1.5 bg-blue-600 hover:bg-blue-500 rounded-lg text-sm font-bold shadow-md transition-colors">
            Bubble Sort
          </button>
          <button onClick={() => runAlgorithm("Merge Sort", getMergeSortAnimations, MERGE_SORT_CODE)} className="px-4 py-1.5 bg-purple-600 hover:bg-purple-500 rounded-lg text-sm font-bold shadow-md transition-colors">
            Merge Sort
          </button>
        </div>
      </div>
    </div>
  );
}
