import React from 'react';
import { useStore } from '../../store/useStore';
import { motion } from 'framer-motion';

const AlgorithmPanel: React.FC = () => {
  const { traces, currentTraceIndex, algorithm } = useStore();
  const currentStep = traces[currentTraceIndex];

  if (!currentStep) return null;

  const array = currentStep.array;
  const activeIndices = currentStep.activeIndices;
  
  // Find the max value to calculate heights proportionally
  const maxValue = Math.max(...array, 1);

  return (
    <div className="h-full w-full flex flex-col p-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-bold text-slate-800 dark:text-slate-200">
          Array State
        </h2>
        <div className="flex gap-4">
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-blue-500"></div>
            <span className="text-sm text-slate-600 dark:text-slate-400">Active</span>
          </div>
          
          {algorithm === 'quick' && (
            <>
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full bg-purple-500"></div>
                <span className="text-sm text-slate-600 dark:text-slate-400">Pivot</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 rounded-full bg-amber-500"></div>
                <span className="text-sm text-slate-600 dark:text-slate-400">Pointers</span>
              </div>
            </>
          )}

          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-emerald-500"></div>
            <span className="text-sm text-slate-600 dark:text-slate-400">Sorted</span>
          </div>
        </div>
      </div>

      <div className="flex-1 flex items-end justify-center gap-2 pb-10">
        {array.map((value, idx) => {
          const isActive = activeIndices.includes(idx);
          const isCompleted = currentStep.type === 'completed';
          
          let bgColor = 'bg-slate-300 dark:bg-slate-700'; // Default
          if (isCompleted) bgColor = 'bg-emerald-500';
          else if (currentStep.pivotIndex === idx) bgColor = 'bg-purple-500';
          else if (currentStep.pointerIndices?.includes(idx)) bgColor = 'bg-amber-500';
          else if (isActive) bgColor = 'bg-blue-500';
          
          return (
            <motion.div
              key={idx} // In a real app we'd use stable IDs for array items to animate swaps perfectly
              layout
              transition={{ type: 'spring', stiffness: 300, damping: 20 }}
              className={`relative flex flex-col justify-end w-12 sm:w-16 ${bgColor} rounded-t-md overflow-hidden shadow-sm`}
              style={{ height: `${(value / maxValue) * 100}%` }}
            >
              <div className="absolute bottom-2 left-0 right-0 text-center text-white font-bold text-lg drop-shadow-md">
                {value}
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
};

export default AlgorithmPanel;
