import React from 'react';
import { useStore } from '../../store/useStore';
import { motion, AnimatePresence } from 'framer-motion';
import { Lightbulb } from 'lucide-react';

const IntuitionPanel: React.FC = () => {
  const { traces, currentTraceIndex } = useStore();
  const currentStep = traces[currentTraceIndex];

  if (!currentStep) return null;

  return (
    <div className="h-full flex flex-col justify-center max-w-4xl mx-auto">
      <AnimatePresence mode="wait">
        <motion.div
          key={currentTraceIndex}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.3 }}
          className="flex gap-4"
        >
          <div className="mt-1 shrink-0">
            <div className="w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900/50 flex items-center justify-center">
              <Lightbulb className="text-blue-500 dark:text-blue-400" size={20} />
            </div>
          </div>
          
          <div>
            <h3 className="text-xl font-bold text-slate-800 dark:text-slate-100 mb-2">
              {currentStep.explanationTitle}
            </h3>
            <p className="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
              {currentStep.explanationText}
            </p>
            
            {/* Context chips */}
            <div className="mt-4 flex gap-2">
              <span className="px-3 py-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-full text-xs font-medium text-slate-500 dark:text-slate-400 shadow-sm">
                Action: {currentStep.type.toUpperCase()}
              </span>
              {currentStep.activeIndices.length > 0 && (
                <span className="px-3 py-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-full text-xs font-medium text-blue-500 dark:text-blue-400 shadow-sm">
                  Focus: Indices [{currentStep.activeIndices.join(', ')}]
                </span>
              )}
            </div>
          </div>
        </motion.div>
      </AnimatePresence>
    </div>
  );
};

export default IntuitionPanel;
