import { useStore } from '../store/useStore';
import { Play, Pause, RefreshCw, ChevronLeft, ChevronRight, RotateCcw, Sun, Moon } from 'lucide-react';
import { generateBubbleSort } from '../algorithms/bubbleSort';
import { generateSelectionSort, SELECTION_SORT_CODE } from '../algorithms/selectionSort';
import { generateInsertionSort, INSERTION_SORT_CODE } from '../algorithms/insertionSort';
import { generateMergeSort, MERGE_SORT_CODE } from '../algorithms/mergeSort';
import { generateQuickSort, QUICK_SORT_CODE } from '../algorithms/quickSort';

export default function Header() {
  const { 
    generateArray, arraySize, setArraySize, speed, setSpeed, 
    isPlaying, playPause, mode, setMode, setAlgorithm, setFrames,
    stepForward, stepBackward, reset, theme, toggleTheme
  } = useStore();

  const handleRun = (name: string, generator: any, code: string, metrics: any) => {
    setAlgorithm(name, code, metrics);
    const array = useStore.getState().array;
    const animations = generator(array);
    setFrames(animations);
  };

  return (
    <div className="bg-panel backdrop-blur-md rounded-xl shadow-panel border border-border p-4 flex flex-wrap items-center justify-between gap-4 transition-colors duration-300">
      {/* Branding & Controls */}
      <div className="flex flex-wrap items-center gap-4">
        <h1 className="text-xl font-black bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent tracking-tight">
          DSA Platform
        </h1>
        <div className="h-6 w-px bg-border mx-2 hidden sm:block"></div>
        
        {/* Array Size */}
        <div className="flex flex-col gap-1">
          <label className="text-xs font-bold text-secondary uppercase tracking-wider">Size: {arraySize}</label>
          <input type="range" min="5" max="50" value={arraySize} 
                 onChange={(e) => setArraySize(Number(e.target.value))}
                 className="w-24 accent-blue-500" />
        </div>

        {/* Speed */}
        <div className="flex flex-col gap-1">
          <label className="text-xs font-bold text-secondary uppercase tracking-wider">Speed: {speed}ms</label>
          <input type="range" min="10" max="1000" value={speed} 
                 onChange={(e) => setSpeed(Number(e.target.value))}
                 className="w-24 accent-purple-500" />
        </div>

        <button onClick={generateArray} className="flex items-center gap-2 px-3 py-1.5 bg-btn hover:bg-btn-hover text-primary rounded-lg text-sm font-semibold transition-colors shadow-sm">
          <RefreshCw size={16} /> New Array
        </button>
      </div>

      {/* Playback & Modes */}
      <div className="flex flex-wrap items-center gap-4">
        
        {/* Theme Toggle */}
        <button onClick={toggleTheme} className="p-2 rounded-full bg-btn hover:bg-btn-hover text-primary shadow-inner transition-colors border border-border" title="Toggle Theme">
          {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
        </button>

        {/* Mode Toggle */}
        <div className="flex bg-btn rounded-lg p-1 border border-border shadow-inner">
          <button onClick={() => setMode('visualize')} className={`px-4 py-1 text-sm font-bold rounded-md transition-colors ${mode === 'visualize' ? 'bg-blue-600 text-white shadow' : 'text-secondary hover:text-primary'}`}>
            Visualize
          </button>
          <button onClick={() => setMode('learn')} className={`px-4 py-1 text-sm font-bold rounded-md transition-colors ${mode === 'learn' ? 'bg-purple-600 text-white shadow' : 'text-secondary hover:text-primary'}`}>
            Learn Mode
          </button>
        </div>

        {/* Playback Controls */}
        <div className="flex items-center gap-1 bg-btn rounded-full p-1 border border-border shadow-inner">
          <button onClick={reset} className="p-2 text-secondary hover:text-primary transition-colors" title="Reset (R)"><RotateCcw size={16} /></button>
          <button onClick={stepBackward} className="p-2 text-secondary hover:text-primary transition-colors" title="Step Backward (Left Arrow)"><ChevronLeft size={18} /></button>
          <button onClick={playPause} className={`p-2 rounded-full transition-transform hover:scale-105 shadow-md ${isPlaying ? 'bg-red-500 hover:bg-red-400 text-white' : 'bg-green-500 hover:bg-green-400 text-white'}`} title="Play/Pause (Space)">
            {isPlaying ? <Pause fill="currentColor" size={16} /> : <Play fill="currentColor" size={16} className="ml-0.5" />}
          </button>
          <button onClick={stepForward} className="p-2 text-secondary hover:text-primary transition-colors" title="Step Forward (Right Arrow)"><ChevronRight size={18} /></button>
        </div>

        {/* Algorithm Selectors */}
        <div className="flex gap-2 border-l border-border pl-4 overflow-x-auto pb-1 max-w-[400px] scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent">
          <button 
            onClick={() => handleRun("Bubble Sort", generateBubbleSort, `def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n - 1):\n        swapped = False\n        for j in range(n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n                swapped = True\n        if not swapped:\n            break\n    return arr`, {
              timeComplexity: { best: "Ω(N)", avg: "Θ(N²)", worst: "O(N²)" },
              spaceComplexity: "O(1)"
            })} 
            className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-sm font-bold shadow-md transition-colors whitespace-nowrap"
          >
            Bubble
          </button>
          <button 
            onClick={() => handleRun("Selection Sort", generateSelectionSort, SELECTION_SORT_CODE, {
              timeComplexity: { best: "Ω(N²)", avg: "Θ(N²)", worst: "O(N²)" },
              spaceComplexity: "O(1)"
            })} 
            className="px-3 py-1.5 bg-pink-600 hover:bg-pink-500 rounded-lg text-sm font-bold shadow-md transition-colors whitespace-nowrap"
          >
            Selection
          </button>
          <button 
            onClick={() => handleRun("Insertion Sort", generateInsertionSort, INSERTION_SORT_CODE, {
              timeComplexity: { best: "Ω(N)", avg: "Θ(N²)", worst: "O(N²)" },
              spaceComplexity: "O(1)"
            })} 
            className="px-3 py-1.5 bg-orange-600 hover:bg-orange-500 rounded-lg text-sm font-bold shadow-md transition-colors whitespace-nowrap"
          >
            Insertion
          </button>
          <button 
            onClick={() => handleRun("Merge Sort", generateMergeSort, MERGE_SORT_CODE, {
              timeComplexity: { best: "Ω(N log N)", avg: "Θ(N log N)", worst: "O(N log N)" },
              spaceComplexity: "O(N)"
            })} 
            className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-sm font-bold shadow-md transition-colors whitespace-nowrap"
          >
            Merge
          </button>
          <button 
            onClick={() => handleRun("Quick Sort", generateQuickSort, QUICK_SORT_CODE, {
              timeComplexity: { best: "Ω(N log N)", avg: "Θ(N log N)", worst: "O(N²)" },
              spaceComplexity: "O(log N)"
            })} 
            className="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 rounded-lg text-sm font-bold shadow-md transition-colors whitespace-nowrap"
          >
            Quick
          </button>
        </div>
      </div>
    </div>
  );
}
