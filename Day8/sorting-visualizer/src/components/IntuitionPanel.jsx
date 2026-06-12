import React from 'react';
import { useStore } from '../store/useStore';

export default function IntuitionPanel() {
  const { callStack, algorithmName, comparisons, swaps } = useStore();

  const getIntuition = () => {
    switch (algorithmName) {
      case "Bubble Sort":
        return "Imagine bubbles in water. Larger bubbles rise to the top. Similarly, larger elements move towards the end after every pass.";
      case "Merge Sort":
        return "Divide & Conquer: Break the problem into smaller groups. Sort the small groups, then merge them back together in order.";
      default:
        return "Select an algorithm to see its intuition.";
    }
  };

  return (
    <div className="flex-1 flex flex-col gap-4 text-sm">
      
      {/* Metrics */}
      <div className="grid grid-cols-2 gap-2 bg-slate-900/50 p-3 rounded-lg border border-slate-700">
        <div>
          <span className="text-slate-500 text-xs block uppercase">Comparisons</span>
          <span className="text-white font-bold text-lg">{comparisons}</span>
        </div>
        <div>
          <span className="text-slate-500 text-xs block uppercase">Swaps / Writes</span>
          <span className="text-white font-bold text-lg">{swaps}</span>
        </div>
      </div>

      {/* Intuition Text */}
      <div className="text-slate-300 italic border-l-2 border-green-500 pl-3">
        "{getIntuition()}"
      </div>

      {/* Recursion Stack (Only if exists) */}
      {callStack.length > 0 && (
        <div className="mt-2 flex flex-col flex-1">
          <span className="text-xs font-bold text-slate-400 uppercase mb-1">Call Stack</span>
          <div className="bg-slate-900 rounded-lg p-2 font-mono text-xs text-yellow-300 flex-1 overflow-y-auto">
            {callStack.map((call, idx) => (
              <div key={idx} className={`${idx === callStack.length - 1 ? 'font-bold text-yellow-400' : 'text-yellow-600'}`}>
                {'> '.repeat(idx)}{call}
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
