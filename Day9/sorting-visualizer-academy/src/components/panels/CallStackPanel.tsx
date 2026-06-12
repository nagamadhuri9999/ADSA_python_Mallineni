import React, { useRef, useEffect } from 'react';
import { useStore } from '../../store/useStore';
import { motion, AnimatePresence } from 'framer-motion';

const CallStackPanel: React.FC = () => {
  const { traces, currentTraceIndex } = useStore();
  const currentStep = traces[currentTraceIndex];
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to top when stack changes
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = 0;
    }
  }, [currentStep?.callStack.length]);

  if (!currentStep) return null;

  const stack = currentStep.callStack;

  return (
    <div className="h-full flex flex-col" ref={scrollRef}>
      {stack.length === 0 ? (
        <div className="flex-1 flex items-center justify-center text-slate-400 text-sm italic">
          Stack is empty
        </div>
      ) : (
        <div className="flex flex-col gap-2">
          <AnimatePresence initial={false}>
            {stack.map((frame, index) => {
              const isTop = index === 0;
              return (
                <motion.div
                  key={frame.id}
                  initial={{ opacity: 0, x: 20, height: 0 }}
                  animate={{ opacity: 1, x: 0, height: 'auto' }}
                  exit={{ opacity: 0, scale: 0.95, transition: { duration: 0.2 } }}
                  className={`
                    rounded-lg border p-3 shadow-sm relative overflow-hidden
                    ${isTop 
                      ? 'bg-blue-50 border-blue-200 dark:bg-blue-900/20 dark:border-blue-800' 
                      : 'bg-white border-slate-200 dark:bg-slate-800 dark:border-slate-700 opacity-60'
                    }
                  `}
                >
                  {isTop && (
                    <div className="absolute top-0 right-0 bg-blue-500 text-white text-[10px] uppercase font-bold px-2 py-0.5 rounded-bl-lg">
                      TOP
                    </div>
                  )}
                  
                  <div className="font-mono text-sm font-bold text-slate-800 dark:text-slate-200 mb-1">
                    {frame.functionName}()
                  </div>
                  
                  <div className="text-xs font-mono text-slate-600 dark:text-slate-400 space-y-1">
                    <div><span className="opacity-50">Params:</span> {frame.parameters}</div>
                    <div><span className="opacity-50">Locals:</span> {frame.localVars}</div>
                  </div>
                  
                  <div className={`
                    mt-2 text-xs font-semibold uppercase tracking-wider
                    ${isTop ? 'text-blue-600 dark:text-blue-400' : 'text-slate-500'}
                  `}>
                    Status: {frame.status}
                  </div>
                </motion.div>
              );
            })}
          </AnimatePresence>
        </div>
      )}
    </div>
  );
};

export default CallStackPanel;
