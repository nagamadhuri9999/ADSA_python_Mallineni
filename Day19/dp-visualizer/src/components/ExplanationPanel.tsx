import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useExecution } from '../context/ExecutionContext';

const ExplanationPanel: React.FC = () => {
  const { stepData, currentStep } = useExecution();
  
  if (!stepData) return <div className="flex-1 bg-panel glass-panel h-full"></div>;

  const exp = stepData.explanation;

  return (
    <div className="flex-1 flex flex-col bg-panel glass-panel h-full relative overflow-hidden">
      <div className="h-8 border-b border-border flex items-center px-4 bg-black/5 shrink-0">
        <span className="text-xs font-medium uppercase tracking-wider opacity-70">Explanation</span>
      </div>
      <div className="flex-1 p-6 overflow-auto">
        <AnimatePresence mode="wait">
          <motion.div
            key={`step-${currentStep}`}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="flex flex-col gap-4"
          >
            <h3 className="text-lg font-semibold text-accent">{exp.title}</h3>
            
            <div className="p-4 bg-black/5 rounded-lg border border-border text-sm leading-relaxed flex flex-col gap-2">
              {exp.text.map((t, i) => (
                <p key={i}>{t}</p>
              ))}
            </div>
            
            {exp.insight && (
              <div className="flex items-start gap-3 p-3 bg-blue-500/10 border border-blue-500/20 rounded-lg mt-2">
                <div className="text-blue-500 mt-0.5">💡</div>
                <div className="text-sm">
                  <span className="font-semibold text-blue-400">Insight:</span> {exp.insight}
                </div>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>
    </div>
  );
};

export default ExplanationPanel;
