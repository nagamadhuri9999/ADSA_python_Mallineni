import React from 'react';
import { Moon, Sun, Play, ZoomIn, ZoomOut } from 'lucide-react';
import { useExecution } from '../context/ExecutionContext';
import type { Topic } from '../context/ExecutionContext';

interface HeaderProps {
  isDarkMode: boolean;
  setIsDarkMode: (val: boolean) => void;
}

const Header: React.FC<HeaderProps> = ({ isDarkMode, setIsDarkMode }) => {
  const { currentTopic, setCurrentTopic, setZoomLevel, zoomLevel } = useExecution();

  return (
    <header className="h-14 border-b border-border flex items-center justify-between px-4 glass-panel shrink-0 z-10 relative">
      <div className="flex items-center gap-4">
        <div className="font-bold text-lg tracking-tight text-accent flex items-center gap-2">
          <div className="w-6 h-6 rounded bg-accent/20 flex items-center justify-center">
            <span className="text-sm">DP</span>
          </div>
          Visualizer
        </div>
        
        <div className="h-6 w-px bg-border mx-2" />
        
        <select 
          value={currentTopic}
          onChange={(e) => setCurrentTopic(e.target.value as Topic)}
          className="bg-transparent border border-border rounded px-3 py-1 text-sm outline-none focus:border-accent"
        >
          <option value="Fibonacci (Memoization)">Fibonacci (Memoization)</option>
          <option value="Fibonacci (Tabulation)">Fibonacci (Tabulation)</option>
          <option value="LIS">Longest Increasing Subsequence</option>
          <option value="LCS">Longest Common Subsequence</option>
          <option value="Knapsack">0/1 Knapsack</option>
        </select>

        <select className="bg-transparent border border-border rounded px-3 py-1 text-sm outline-none focus:border-accent">
          <option>Python</option>
          <option>Java</option>
          <option>C++</option>
          <option>JavaScript</option>
        </select>
      </div>
      
      <div className="flex items-center gap-2">
        <button className="p-2 hover:bg-black/5 rounded-md transition-colors text-sm flex items-center gap-2 text-accent">
          <Play size={16} /> Replay
        </button>
        
        <div className="h-6 w-px bg-border mx-2" />
        
        <div className="flex items-center gap-1 bg-black/5 rounded-md px-1">
          <button 
            onClick={() => setZoomLevel(z => Math.max(0.5, z - 0.1))}
            className="p-1 hover:bg-black/10 rounded transition-colors"
            title="Zoom Out"
          >
            <ZoomOut size={16} />
          </button>
          <span className="text-xs font-mono w-10 text-center opacity-80">{Math.round(zoomLevel * 100)}%</span>
          <button 
            onClick={() => setZoomLevel(z => Math.min(2.5, z + 0.1))}
            className="p-1 hover:bg-black/10 rounded transition-colors"
            title="Zoom In"
          >
            <ZoomIn size={16} />
          </button>
        </div>

        <div className="h-6 w-px bg-border mx-2" />
        
        <button 
          onClick={() => setIsDarkMode(!isDarkMode)}
          className="p-2 hover:bg-black/5 rounded-md transition-colors"
          title="Toggle Theme"
        >
          {isDarkMode ? <Sun size={18} /> : <Moon size={18} />}
        </button>
      </div>
    </header>
  );
};

export default Header;
