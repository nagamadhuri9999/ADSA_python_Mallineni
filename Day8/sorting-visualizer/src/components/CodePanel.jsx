import React, { useEffect, useRef } from 'react';
import { useStore } from '../store/useStore';

export default function CodePanel() {
  const { codeSnippet, activeLine } = useStore();
  const containerRef = useRef(null);
  
  useEffect(() => {
    // Auto-scroll to active line
    if (containerRef.current && activeLine >= 0) {
      const activeEl = containerRef.current.querySelector('.active-code-line');
      if (activeEl) {
        activeEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, [activeLine]);

  if (!codeSnippet) {
    return <div className="text-slate-500 text-sm italic">Select an algorithm to view code.</div>;
  }

  const lines = codeSnippet.split('\n');

  return (
    <div ref={containerRef} className="flex-1 font-mono text-xs overflow-y-auto">
      {lines.map((line, idx) => (
        <div 
          key={idx} 
          className={`px-2 py-0.5 rounded transition-colors duration-150 whitespace-pre ${activeLine === idx ? 'bg-purple-500/30 border-l-2 border-purple-400 text-white' : 'text-slate-300 border-l-2 border-transparent'}`}
        >
          <span className="text-slate-600 mr-4 select-none">{idx + 1}</span>
          {line}
        </div>
      ))}
    </div>
  );
}
