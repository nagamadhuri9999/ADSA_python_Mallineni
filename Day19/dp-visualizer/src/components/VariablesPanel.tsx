import React from 'react';
import { useExecution } from '../context/ExecutionContext';

const VariablesPanel: React.FC = () => {
  const { stepData } = useExecution();
  
  const vars = stepData?.variables || {};
  const stack = [...(stepData?.callStack || [])].reverse();

  return (
    <div className="flex-1 flex flex-col bg-panel glass-panel h-full">
      <div className="h-8 border-b border-border flex items-center px-4 bg-black/5 shrink-0">
        <span className="text-xs font-medium uppercase tracking-wider opacity-70">Variables & Memory</span>
      </div>
      <div className="flex-1 p-4 overflow-auto text-sm font-mono">
        <div className="mb-4">
          <div className="text-xs text-accent mb-2 uppercase tracking-wider">Local Variables</div>
          <div className="grid grid-cols-2 gap-2">
            {Object.keys(vars).length === 0 && (
              <div className="opacity-50 text-xs italic">No variables</div>
            )}
            {Object.entries(vars).map(([k, v]) => (
              <div key={k} className="flex justify-between bg-black/5 px-2 py-1 rounded">
                <span className="opacity-70">{k}</span>
                <span className="font-semibold text-blue-500">{String(v)}</span>
              </div>
            ))}
          </div>
        </div>
        
        <div>
          <div className="text-xs text-accent mb-2 uppercase tracking-wider">Call Stack</div>
          <div className="flex flex-col gap-1">
            {stack.length === 0 && (
              <div className="opacity-50 text-xs italic">Stack is empty</div>
            )}
            {stack.map((frame, i) => (
              <div 
                key={frame.id + i} 
                className={`px-2 py-1.5 rounded text-xs flex justify-between transition-opacity ${
                  i === 0 ? 'bg-accent/10 border border-accent/20' : 'bg-black/5'
                }`}
                style={{ opacity: i === 0 ? 1 : Math.max(0.3, 1 - i * 0.2) }}
              >
                <span>{frame.func}</span>
                <span className="opacity-50">Line {frame.line}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default VariablesPanel;
