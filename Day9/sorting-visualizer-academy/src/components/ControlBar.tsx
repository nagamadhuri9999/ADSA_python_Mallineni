import React, { useEffect } from 'react';
import { useStore } from '../store/useStore';
import { Play, Pause, StepForward, StepBack, RotateCcw, Shuffle, Sun, Moon } from 'lucide-react';

const ControlBar: React.FC = () => {
  const { 
    currentTraceIndex, traces, nextStep, prevStep, 
    isPlaying, setIsPlaying, playbackSpeed, setPlaybackSpeed,
    theme, toggleTheme, generateNewArray,
    algorithm, setAlgorithm
  } = useStore();

  // Playback effect
  useEffect(() => {
    let interval: number;
    if (isPlaying && currentTraceIndex < traces.length - 1) {
      interval = setInterval(() => {
        nextStep();
      }, playbackSpeed);
    } else if (currentTraceIndex >= traces.length - 1) {
      setIsPlaying(false);
    }
    return () => clearInterval(interval);
  }, [isPlaying, currentTraceIndex, playbackSpeed, nextStep, traces.length]);

  // Keyboard controls
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight') nextStep();
      if (e.key === 'ArrowLeft') prevStep();
      if (e.key === ' ') {
        e.preventDefault();
        setIsPlaying(!isPlaying);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [nextStep, prevStep, isPlaying, setIsPlaying]);

  const handleReset = () => {
    setIsPlaying(false);
    useStore.getState().setCurrentTraceIndex(0);
  };

  const handleRandomize = () => {
    setIsPlaying(false);
    generateNewArray(10);
  };

  return (
    <div className="flex items-center justify-between px-4 h-full">
      <div className="flex items-center space-x-4">
        <h1 className="font-bold text-lg bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-purple-500">
          Sorting Academy
        </h1>
        
        <select 
          value={algorithm}
          onChange={(e) => {
            setIsPlaying(false);
            setAlgorithm(e.target.value as 'merge' | 'quick');
          }}
          className="bg-slate-100 dark:bg-slate-800 border-none text-sm font-semibold rounded-lg px-3 py-1.5 focus:ring-2 focus:ring-blue-500 outline-none"
        >
          <option value="merge">Merge Sort</option>
          <option value="quick">Quick Sort</option>
        </select>
      </div>

      <div className="flex items-center space-x-4">
        {/* Progress Tracker */}
        <div className="text-xs font-mono text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-3 py-1 rounded-full">
          Step: {traces.length > 0 ? currentTraceIndex + 1 : 0} / {traces.length}
        </div>

        {/* Controls */}
        <div className="flex bg-slate-100 dark:bg-slate-800 p-1 rounded-lg">
          <button onClick={prevStep} disabled={currentTraceIndex === 0} className="p-2 hover:bg-white dark:hover:bg-slate-700 rounded-md disabled:opacity-50 transition-colors">
            <StepBack size={16} />
          </button>
          
          <button onClick={() => setIsPlaying(!isPlaying)} className="p-2 hover:bg-white dark:hover:bg-slate-700 rounded-md transition-colors mx-1">
            {isPlaying ? <Pause size={16} className="text-blue-500" /> : <Play size={16} className="text-blue-500" />}
          </button>
          
          <button onClick={nextStep} disabled={currentTraceIndex >= traces.length - 1} className="p-2 hover:bg-white dark:hover:bg-slate-700 rounded-md disabled:opacity-50 transition-colors">
            <StepForward size={16} />
          </button>
        </div>

        {/* Speed Slider */}
        <div className="flex items-center space-x-2">
          <span className="text-xs text-slate-500 uppercase tracking-wider font-semibold">Speed</span>
          <input 
            type="range" 
            min="100" max="2000" step="100"
            // Reverse direction logically (lower value = faster interval)
            value={2100 - playbackSpeed} 
            onChange={(e) => setPlaybackSpeed(2100 - Number(e.target.value))}
            className="w-24 accent-blue-500"
          />
        </div>

        {/* Utilities */}
        <div className="flex items-center space-x-2 border-l border-slate-200 dark:border-slate-700 pl-4">
          <button onClick={handleReset} title="Reset" className="p-2 hover:bg-slate-200 dark:hover:bg-slate-800 rounded-lg transition-colors">
            <RotateCcw size={18} />
          </button>
          <button onClick={handleRandomize} title="Random Array" className="p-2 hover:bg-slate-200 dark:hover:bg-slate-800 rounded-lg transition-colors">
            <Shuffle size={18} />
          </button>
          <button onClick={toggleTheme} title="Toggle Theme" className="p-2 hover:bg-slate-200 dark:hover:bg-slate-800 rounded-lg transition-colors">
            {theme === 'dark' ? <Sun size={18} /> : <Moon size={18} />}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ControlBar;
