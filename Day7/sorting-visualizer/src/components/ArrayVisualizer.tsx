import { useStore } from '../store/useStore';
import { motion, AnimatePresence } from 'framer-motion';

const getPremiumStyle = (state: string) => {
  switch (state) {
    case 'comparing': 
      return { background: 'linear-gradient(to top, #dc2626, #f87171)', boxShadow: '0 0 15px rgba(239, 68, 68, 0.5)' };
    case 'swapping': 
      return { background: 'linear-gradient(to top, #d97706, #fcd34d)', boxShadow: '0 0 15px rgba(245, 158, 11, 0.5)' };
    case 'sorted': 
      return { background: 'linear-gradient(to top, #16a34a, #4ade80)', boxShadow: '0 0 15px rgba(34, 197, 94, 0.5)' };
    case 'pivot': 
      return { background: 'linear-gradient(to top, #9333ea, #c084fc)', boxShadow: '0 0 15px rgba(168, 85, 247, 0.5)' };
    case 'minimum': 
      return { background: 'linear-gradient(to top, #2563eb, #60a5fa)', boxShadow: '0 0 15px rgba(59, 130, 246, 0.5)' };
    default: 
      return { background: 'linear-gradient(to top, #475569, #94a3b8)', boxShadow: 'none' };
  }
};

export default function ArrayVisualizer() {
  const { array } = useStore();

  if (array.length === 0) return null;

  const maxVal = Math.max(...array.map(a => a.value), 1);

  return (
    <div className="flex items-end justify-center w-full h-full gap-[2px] sm:gap-1 px-2">
      <AnimatePresence>
        {array.map((item) => {
          const style = getPremiumStyle(item.state);
          return (
            <motion.div
              layout
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ 
                type: "spring", 
                stiffness: 150, 
                damping: 15,
                mass: 1,
                bounce: 0.2
              }}
              key={item.id}
              className="w-full max-w-[40px] flex items-end justify-center rounded-t-md border-t border-white/20 transition-all duration-150"
              style={{
                height: `${Math.max((item.value / maxVal) * 95, 5)}%`,
                background: style.background,
                boxShadow: style.boxShadow,
              }}
            >
              {array.length <= 35 && (
                <span 
                  className={`font-black select-none ${array.length <= 15 ? 'text-sm mb-2' : 'text-[10px] pb-2 -rotate-90 origin-bottom tracking-wider'}`}
                  style={{ 
                    color: 'rgba(255,255,255,0.95)', 
                    textShadow: '0px 1px 3px rgba(0,0,0,0.9)' 
                  }}
                >
                  {item.value}
                </span>
              )}
            </motion.div>
          );
        })}
      </AnimatePresence>
    </div>
  );
}
