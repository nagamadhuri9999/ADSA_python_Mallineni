import React from 'react';
import { useStore } from '../store/useStore';
import { motion } from 'framer-motion';

export default function ArrayBar() {
  const { array, colors } = useStore();

  return (
    <div className="flex items-end justify-center w-full h-full gap-1 p-4">
      {array.map((value, idx) => (
        <motion.div
          layout
          transition={{ type: "spring", stiffness: 300, damping: 25 }}
          key={idx} // We ideally want unique IDs but index is okay for basic visualizer if we layout animate carefully
          className="w-full max-w-[40px] flex items-end justify-center rounded-t-md shadow-sm border border-black/10"
          style={{
            height: `${(value / 500) * 100}%`,
            backgroundColor: colors[idx],
          }}
        >
          <span className="text-[10px] font-bold text-slate-900 pb-1 -rotate-90 origin-bottom">
            {value}
          </span>
        </motion.div>
      ))}
    </div>
  );
}
