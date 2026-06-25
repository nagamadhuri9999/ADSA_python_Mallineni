import React from 'react';
import { Play, Pause, SkipBack, SkipForward, FastForward, Rewind } from 'lucide-react';
import { useExecution } from '../context/ExecutionContext';

const ControlsPanel: React.FC = () => {
  const { isPlaying, setIsPlaying, currentStep, setCurrentStep, totalSteps, speed, setSpeed } = useExecution();

  return (
    <div className="h-16 border-t border-border bg-panel glass-panel flex items-center px-6 shrink-0 relative z-20">
      <div className="flex-1 flex items-center gap-4">
        {/* Step Slider */}
        <div className="text-xs font-mono opacity-50 w-12 text-right">{currentStep}</div>
        <div className="flex-1 max-w-xl flex items-center relative group">
          <div className="absolute w-full h-1.5 bg-black/10 rounded-full overflow-hidden">
            <div 
              className="h-full bg-accent rounded-full transition-all duration-300" 
              style={{ width: `${totalSteps > 0 ? (currentStep / totalSteps) * 100 : 0}%` }} 
            />
          </div>
          <input 
            type="range" 
            min="0" 
            max={totalSteps} 
            value={currentStep}
            onChange={(e) => setCurrentStep(parseInt(e.target.value))}
            className="w-full absolute opacity-0 cursor-pointer h-4"
          />
          {/* Thumb */}
          <div 
            className="w-3 h-3 bg-white border-2 border-accent rounded-full absolute -ml-1.5 shadow transform transition-all group-hover:scale-125 duration-300"
            style={{ left: `${totalSteps > 0 ? (currentStep / totalSteps) * 100 : 0}%` }} 
          />
        </div>
        <div className="text-xs font-mono opacity-50 w-12">{totalSteps}</div>
      </div>
      
      <div className="flex items-center gap-3 mx-8">
        <button onClick={() => setCurrentStep(0)} className="p-2 hover:bg-black/5 rounded-full transition-colors opacity-70 hover:opacity-100">
          <SkipBack size={20} />
        </button>
        <button onClick={() => setCurrentStep(Math.max(0, currentStep - 1))} className="p-2 hover:bg-black/5 rounded-full transition-colors opacity-70 hover:opacity-100">
          <Rewind size={20} />
        </button>

        
        <button 
          className="p-3 bg-accent text-white rounded-full hover:bg-accent/90 transition-colors shadow-lg shadow-accent/20"
          onClick={() => setIsPlaying(!isPlaying)}
        >
          {isPlaying ? <Pause size={24} fill="currentColor" /> : <Play size={24} fill="currentColor" className="ml-1" />}
        </button>
        
        <button onClick={() => setCurrentStep(Math.min(totalSteps, currentStep + 1))} className="p-2 hover:bg-black/5 rounded-full transition-colors opacity-70 hover:opacity-100">
          <FastForward size={20} />
        </button>
        <button onClick={() => setCurrentStep(totalSteps)} className="p-2 hover:bg-black/5 rounded-full transition-colors opacity-70 hover:opacity-100">
          <SkipForward size={20} />
        </button>
      </div>
      
      <div className="flex-1 flex items-center justify-end gap-2">
        <div className="text-xs uppercase tracking-wider font-semibold opacity-50 mr-2">Speed</div>
        {[0.25, 0.5, 1, 2, 4].map(s => (
          <button 
            key={s}
            onClick={() => setSpeed(s)}
            className={`px-2 py-1 rounded text-xs font-mono transition-colors ${
              speed === s 
                ? 'bg-accent/20 text-accent font-bold border border-accent/50' 
                : 'hover:bg-black/5 opacity-70 border border-transparent'
            }`}
          >
            {s}x
          </button>
        ))}
      </div>
    </div>
  );
};

export default ControlsPanel;
