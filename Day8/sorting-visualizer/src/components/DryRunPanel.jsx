import React from 'react';
import { useStore } from '../store/useStore';
import { motion, AnimatePresence } from 'framer-motion';

export default function DryRunPanel() {
  const { explanation } = useStore();

  return (
    <div className="flex-1 text-slate-200 text-sm leading-relaxed font-medium">
      <AnimatePresence mode="wait">
        <motion.div
          key={explanation}
          initial={{ opacity: 0, y: 5 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -5 }}
          transition={{ duration: 0.2 }}
        >
          {explanation}
        </motion.div>
      </AnimatePresence>
    </div>
  );
}
