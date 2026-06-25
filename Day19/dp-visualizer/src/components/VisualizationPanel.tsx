import React, { useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useExecution } from '../context/ExecutionContext';

const TreeVisualizer: React.FC<{ stepData: any }> = ({ stepData }) => {
  const treeNodes = Object.values(stepData.tree?.nodes || {});
  const treeEdges = stepData.tree?.edges || [];
  const memo = stepData.memo || {};
  
  // Compute tree layout
  const childrenMap: Record<string, string[]> = {};
  const nodeMap: Record<string, any> = {};
  let rootId: string | null = null;
  
  treeNodes.forEach((n: any) => {
    childrenMap[n.id] = [];
    nodeMap[n.id] = n;
  });
  
  treeNodes.forEach((n: any) => {
    if (n.parentId && childrenMap[n.parentId]) {
      childrenMap[n.parentId].push(n.id);
    } else if (!n.parentId) {
      rootId = n.id;
    }
  });

  const coords: Record<string, { x: number, y: number }> = {};
  let leafX = 0;
  
  const assignCoords = (id: string, depth: number) => {
    const nodeChildren = childrenMap[id];
    if (nodeChildren.length === 0) {
      coords[id] = { x: leafX * 80, y: depth * 80 };
      leafX++;
    } else {
      let sumX = 0;
      nodeChildren.forEach(childId => {
        assignCoords(childId, depth + 1);
        sumX += coords[childId].x;
      });
      coords[id] = { x: sumX / nodeChildren.length, y: depth * 80 };
    }
  };
  
  if (rootId) {
    assignCoords(rootId, 0);
    // Center root at 0
    const offsetX = coords[rootId].x;
    Object.keys(coords).forEach(k => coords[k].x -= offsetX);
  }

  const containerRef = useRef<HTMLDivElement>(null);

  return (
    <>
      {/* Memo Dictionary */}
      <div className="absolute top-4 right-4 bg-panel glass-panel p-4 rounded-lg border border-border text-sm shadow-xl min-w-[200px] z-50">
        <div className="font-semibold mb-3 flex items-center justify-between">
          <span className="text-accent uppercase tracking-wider text-xs">Memo Dictionary</span>
          <span className="bg-black/10 dark:bg-white/10 px-2 py-0.5 rounded text-xs">{Object.keys(memo).length} entries</span>
        </div>
        <div className="flex flex-wrap gap-2">
          {Object.keys(memo).length === 0 && (
            <span className="opacity-50 italic text-xs">Empty</span>
          )}
          {Object.entries(memo).map(([k, v]) => (
            <motion.div 
              key={k}
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              className="bg-accent/10 border border-accent/30 px-2 py-1 rounded font-mono text-xs flex gap-2 w-full justify-between items-center"
            >
              <span className="opacity-70">memo[{k}]</span>
              <span className="font-bold text-accent">{v as React.ReactNode}</span>
            </motion.div>
          ))}
        </div>
      </div>

      <div ref={containerRef} className="relative w-full h-full flex items-center justify-center overflow-hidden cursor-grab active:cursor-grabbing">
        {treeNodes.length === 0 && (
          <div className="opacity-50 absolute">Press Play to start visualization</div>
        )}

        <motion.div 
          drag 
          dragConstraints={containerRef}
          dragElastic={0.2}
          className="relative w-[600px] h-[400px]"
        >
          <svg className="absolute inset-0 w-full h-full pointer-events-none" style={{ overflow: 'visible' }}>
            <g transform="translate(300, 50)">
              {treeEdges.map((edge: any) => {
                const src = coords[edge.source];
                const tgt = coords[edge.target];
                if (!src || !tgt) return null;
                
                return (
                  <motion.line
                    key={`${edge.source}-${edge.target}`}
                    initial={{ pathLength: 0, opacity: 0 }}
                    animate={{ pathLength: 1, opacity: 1 }}
                    transition={{ duration: 0.3 }}
                    x1={src.x}
                    y1={src.y}
                    x2={tgt.x}
                    y2={tgt.y}
                    stroke="var(--accent)"
                    strokeWidth="2"
                    strokeOpacity="0.4"
                  />
                );
              })}
            </g>
          </svg>
          
          <div className="absolute top-[50px] left-[300px]">
            {treeNodes.map((node: any) => {
              const { x = 0, y = 0 } = coords[node.id] || {};
              
              const getStatusColor = (status: string) => {
                switch(status) {
                  case 'active': return 'border-accent bg-accent/20 text-accent ring-4 ring-accent/20 shadow-[0_0_15px_rgba(var(--accent),0.5)]';
                  case 'done': return 'border-success bg-success/20 text-success';
                  case 'cache-hit': return 'border-warning bg-warning/20 text-warning ring-2 ring-warning/50';
                  default: return 'border-border bg-panel glass-panel text-foreground/70';
                }
              };
              
              return (
                <motion.div
                  key={node.id}
                  initial={{ opacity: 0, scale: 0.5 }}
                  animate={{ opacity: 1, scale: 1, x: x - 28, y: y - 28 }}
                  className={`absolute flex flex-col items-center justify-center w-14 h-14 rounded-full border-2 ${getStatusColor(node.status)} transition-colors duration-300 z-10`}
                >
                  <span className="text-xs opacity-70 absolute -top-5">fib</span>
                  <span className="font-bold text-lg">{node.val}</span>
                </motion.div>
              );
            })}
          </div>
        </motion.div>
      </div>
    </>
  );
};

const Array1DVisualizer: React.FC<{ stepData: any }> = ({ stepData }) => {
  const arrayData = stepData.array1d;
  if (!arrayData) return null;

  return (
    <div className="flex flex-col items-center justify-center w-full h-full gap-8">
      <div className="text-xl font-bold text-accent opacity-80">{arrayData.name}</div>
      <div className="flex flex-wrap items-center justify-center gap-2 max-w-full overflow-x-auto p-4">
        <AnimatePresence mode="popLayout">
          {arrayData.data.map((val: any, idx: number) => {
            const isActive = arrayData.activeIndices?.includes(idx);
            const isCompare = arrayData.compareIndices?.includes(idx);
            const isUpdated = arrayData.updatedIndices?.includes(idx);

            let borderClass = 'border-border bg-black/5';
            if (isActive) borderClass = 'border-accent bg-accent/20 ring-4 ring-accent/30 scale-110 z-10 shadow-lg';
            else if (isCompare) borderClass = 'border-amber-500 bg-amber-500/20 ring-2 ring-amber-500/50 z-10';
            else if (isUpdated) borderClass = 'border-emerald-500 bg-emerald-500/20 ring-2 ring-emerald-500/50 z-10';

            return (
              <motion.div
                key={`cell-${idx}`}
                layout
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className={`flex flex-col items-center transition-all duration-300`}
              >
                <span className="text-xs opacity-50 mb-2">{arrayData.labels?.[idx] ?? idx}</span>
                <div className={`w-14 h-14 md:w-16 md:h-16 flex items-center justify-center text-lg font-bold border-2 rounded-lg ${borderClass}`}>
                  {val === null ? '-' : val}
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>
    </div>
  );
};

const Array2DVisualizer: React.FC<{ stepData: any }> = ({ stepData }) => {
  const arrayData = stepData.array2d;
  if (!arrayData) return null;

  return (
    <div className="flex flex-col items-center justify-center w-full h-full gap-6">
      <div className="text-xl font-bold text-accent opacity-80">{arrayData.name}</div>
      <div className="max-w-full max-h-full overflow-auto p-4">
        <table className="border-collapse">
          <thead>
            <tr>
              <th className="p-2"></th>
              {arrayData.colLabels?.map((label: string, idx: number) => (
                <th key={`col-${idx}`} className="p-2 text-xs opacity-50 font-normal">{label}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {arrayData.data.map((row: any[], i: number) => (
              <tr key={`row-${i}`}>
                <th className="p-2 text-xs opacity-50 font-normal text-right pr-4">{arrayData.rowLabels?.[i]}</th>
                {row.map((val: any, j: number) => {
                  const isActive = arrayData.activeCell?.[0] === i && arrayData.activeCell?.[1] === j;
                  const isCompare = arrayData.compareCells?.some(([ci, cj]: [number, number]) => ci === i && cj === j);
                  const isUpdated = arrayData.updatedCells?.some(([ui, uj]: [number, number]) => ui === i && uj === j);

                  let borderClass = 'border-border/50 bg-black/5';
                  let contentClass = 'text-foreground/70';
                  
                  if (isActive) {
                    borderClass = 'border-accent bg-accent/20 shadow-[0_0_10px_rgba(var(--accent),0.5)] scale-110 z-10 relative';
                    contentClass = 'text-accent font-bold';
                  } else if (isCompare) {
                    borderClass = 'border-amber-500/80 bg-amber-500/20 z-10 relative';
                    contentClass = 'text-amber-500 font-bold';
                  } else if (isUpdated) {
                    borderClass = 'border-emerald-500/80 bg-emerald-500/20 z-10 relative';
                    contentClass = 'text-emerald-500 font-bold';
                  }

                  return (
                    <td key={`cell-${i}-${j}`} className="p-1">
                      <motion.div
                        layout
                        className={`w-10 h-10 md:w-12 md:h-12 flex items-center justify-center border rounded ${borderClass} transition-all duration-300`}
                      >
                        <span className={contentClass}>{val === null ? '-' : val}</span>
                      </motion.div>
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

const VisualizationPanel: React.FC = () => {
  const { stepData } = useExecution();
  
  if (!stepData) return <div className="flex-1 bg-panel glass-panel h-full"></div>;

  return (
    <div className="flex-1 flex flex-col bg-panel glass-panel relative overflow-hidden h-full">
      <div className="h-10 border-b border-border flex items-center px-4 justify-between bg-black/5 shrink-0">
        <span className="text-sm font-medium opacity-80">
          {stepData.visualType === 'tree' ? 'Recursive Tree' : 
           stepData.visualType === 'array1d' ? '1D DP Array' : '2D DP Matrix'}
        </span>
      </div>
      
      {/* Visualization Canvas Area */}
      <div className="flex-1 p-4 md:p-8 overflow-auto flex items-center justify-center relative bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-black/5 to-transparent dark:from-white/5 dark:to-transparent">
        <AnimatePresence mode="wait">
          {stepData.visualType === 'tree' && <TreeVisualizer key="tree" stepData={stepData} />}
          {stepData.visualType === 'array1d' && <Array1DVisualizer key="array1d" stepData={stepData} />}
          {stepData.visualType === 'array2d' && <Array2DVisualizer key="array2d" stepData={stepData} />}
        </AnimatePresence>
      </div>
    </div>
  );
};

export default VisualizationPanel;
