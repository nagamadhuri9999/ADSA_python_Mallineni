import React from 'react';
import TopBar from './TopBar';
import ArrayBar from './ArrayBar';
import DryRunPanel from './DryRunPanel';
import CodePanel from './CodePanel';
import IntuitionPanel from './IntuitionPanel';

export default function Dashboard() {
  return (
    <div className="flex flex-col h-screen p-4 gap-4">
      {/* Top Bar */}
      <TopBar />
      
      {/* Main Content Grid */}
      <div className="flex-1 grid grid-cols-12 grid-rows-2 gap-4 min-h-0">
        
        {/* Array Visualization (Top Half - Full Width) */}
        <div className="col-span-12 row-span-1 bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-6 flex flex-col">
          <h2 className="text-sm font-bold text-slate-400 mb-2 uppercase tracking-wider">Array Visualization</h2>
          <div className="flex-1 flex items-end justify-center">
            <ArrayBar />
          </div>
        </div>

        {/* Bottom Half - 3 Columns */}
        <div className="col-span-12 row-span-1 grid grid-cols-3 gap-4 min-h-0">
          
          {/* Dry Run / Console Panel */}
          <div className="col-span-1 bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-4 flex flex-col overflow-y-auto">
            <h2 className="text-sm font-bold text-blue-400 mb-3 uppercase tracking-wider">Dry Run</h2>
            <DryRunPanel />
          </div>

          {/* Code Panel */}
          <div className="col-span-1 bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-4 flex flex-col overflow-y-auto">
            <h2 className="text-sm font-bold text-purple-400 mb-3 uppercase tracking-wider">Code Execution</h2>
            <CodePanel />
          </div>

          {/* Intuition & Complexity Panel */}
          <div className="col-span-1 bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-4 flex flex-col overflow-y-auto">
            <h2 className="text-sm font-bold text-green-400 mb-3 uppercase tracking-wider">Intuition & Complexity</h2>
            <IntuitionPanel />
          </div>
          
        </div>
      </div>
    </div>
  );
}
