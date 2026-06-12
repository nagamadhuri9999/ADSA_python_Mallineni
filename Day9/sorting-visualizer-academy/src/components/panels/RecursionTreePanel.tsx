import React, { useMemo } from 'react';
import { useStore } from '../../store/useStore';
import { 
  ReactFlow, 
  Background, 
  Controls, 
  Handle,
  Position
} from '@xyflow/react';
import type { NodeProps } from '@xyflow/react';
import '@xyflow/react/dist/style.css';

// Custom Node Component to style the tree nodes
const TreeNode = ({ data }: NodeProps) => {
  const isActive = data.isActive;
  const isCompleted = data.isCompleted;
  
  let borderColor = 'border-slate-300 dark:border-slate-600';
  let bgColor = 'bg-white dark:bg-slate-800';
  let textColor = 'text-slate-700 dark:text-slate-300';
  let shadow = 'shadow-sm';

  if (isActive) {
    borderColor = 'border-blue-500';
    bgColor = 'bg-blue-50 dark:bg-blue-900/30';
    textColor = 'text-blue-700 dark:text-blue-300';
    shadow = 'shadow-md shadow-blue-500/20';
  } else if (isCompleted) {
    borderColor = 'border-emerald-500';
    bgColor = 'bg-emerald-50 dark:bg-emerald-900/30';
    textColor = 'text-emerald-700 dark:text-emerald-300';
  }

  return (
    <div className={`px-4 py-2 rounded-lg border-2 ${borderColor} ${bgColor} ${textColor} ${shadow} font-mono font-bold min-w-[80px] text-center transition-colors duration-300`}>
      <Handle type="target" position={Position.Top} className="opacity-0" />
      {data.label as string}
      <Handle type="source" position={Position.Bottom} className="opacity-0" />
    </div>
  );
};

const nodeTypes = {
  default: TreeNode,
};

const RecursionTreePanel: React.FC = () => {
  const { traces, currentTraceIndex, theme } = useStore();
  const currentStep = traces[currentTraceIndex];

  // We memoize the edges to add custom styling
  const edges = useMemo(() => {
    if (!currentStep) return [];
    return currentStep.treeEdges.map(edge => ({
      ...edge,
      animated: true,
      style: { stroke: theme === 'dark' ? '#475569' : '#cbd5e1', strokeWidth: 2 }
    }));
  }, [currentStep?.treeEdges, theme]);

  if (!currentStep) return null;

  return (
    <ReactFlow 
      nodes={currentStep.treeNodes}
      edges={edges}
      nodeTypes={nodeTypes}
      fitView
      fitViewOptions={{ padding: 0.2 }}
      minZoom={0.1}
      colorMode={theme}
      nodesDraggable={false}
      nodesConnectable={false}
      elementsSelectable={false}
    >
      <Background color={theme === 'dark' ? '#334155' : '#e2e8f0'} gap={16} />
      <Controls showInteractive={false} />
    </ReactFlow>
  );
};

export default RecursionTreePanel;
