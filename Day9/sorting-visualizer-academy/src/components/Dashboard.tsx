import React, { useEffect } from 'react';
// @ts-ignore
import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import { useStore } from '../store/useStore';
import { generateMergeSortTraces } from '../store/traceEngine';
import { generateQuickSortTraces } from '../store/quickSortEngine';

import ControlBar from './ControlBar';
import AlgorithmPanel from './panels/AlgorithmPanel';
import CodePanel from './panels/CodePanel';
import CallStackPanel from './panels/CallStackPanel';
import RecursionTreePanel from './panels/RecursionTreePanel';
import IntuitionPanel from './panels/IntuitionPanel';

const Dashboard: React.FC = () => {
  const { array, setArray, setTraces, algorithm } = useStore();

  // On mount, set initial array
  useEffect(() => {
    if (array.length === 0) {
      setArray([5, 4, 3, 1, 2]);
    }
  }, [setArray, array.length]);

  // When array or algorithm changes, generate new traces
  useEffect(() => {
    if (array.length === 0) return;
    
    const generatedTraces = algorithm === 'merge' 
      ? generateMergeSortTraces(array)
      : generateQuickSortTraces(array);
      
    setTraces(generatedTraces);
  }, [array, algorithm, setTraces]);

  return (
    <div className="h-screen w-full flex flex-col bg-slate-50 dark:bg-slate-950 overflow-hidden">
      {/* Top Toolbar (Fixed) */}
      <div className="h-14 border-b border-slate-200 dark:border-slate-800 shrink-0 z-20 bg-white dark:bg-slate-900 shadow-sm">
        <ControlBar />
      </div>

      {/* Main Scrollable Content */}
      <div className="flex-1 overflow-y-auto scroll-smooth">
        
        {/* ROW 1: Code & Stack (Huge Window Height to force scroll) */}
        <div className="w-full h-[80vh] p-4">
          <PanelGroup orientation="horizontal">
            <Panel defaultSize={50} minSize={30}>
              <div className="h-full w-full pr-2">
                <div className="h-full w-full bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden flex flex-col">
                  <div className="h-8 shrink-0 border-b border-slate-200 dark:border-slate-800 flex items-center px-3 text-xs font-semibold uppercase tracking-wider text-slate-500">
                    Code Execution
                  </div>
                  <div className="flex-1 overflow-auto">
                    <CodePanel />
                  </div>
                </div>
              </div>
            </Panel>
            
            <PanelResizeHandle className="ResizeHandle" />
            
            <Panel defaultSize={50} minSize={30}>
              <div className="h-full w-full pl-2">
                <div className="h-full w-full bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden flex flex-col">
                  <div className="h-8 shrink-0 border-b border-slate-200 dark:border-slate-800 flex items-center px-3 text-xs font-semibold uppercase tracking-wider text-slate-500">
                    Call Stack
                  </div>
                  <div className="flex-1 overflow-auto p-4">
                    <CallStackPanel />
                  </div>
                </div>
              </div>
            </Panel>
          </PanelGroup>
        </div>

        {/* ROW 2: Visualization & Tree */}
        <div className="w-full h-[80vh] p-4 border-t border-slate-200 dark:border-slate-800 bg-slate-100 dark:bg-slate-900/50">
          <PanelGroup orientation="horizontal">
            <Panel defaultSize={50} minSize={30}>
              <div className="h-full w-full pr-2">
                <div className="h-full w-full bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden flex flex-col">
                  <div className="flex-1">
                    <AlgorithmPanel />
                  </div>
                </div>
              </div>
            </Panel>

            <PanelResizeHandle className="ResizeHandle" />

            <Panel defaultSize={50} minSize={30}>
              <div className="h-full w-full pl-2">
                <div className="h-full w-full bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden flex flex-col">
                  <div className="h-8 shrink-0 border-b border-slate-200 dark:border-slate-800 flex items-center px-3 text-xs font-semibold uppercase tracking-wider text-slate-500">
                    Recursion Tree
                  </div>
                  <div className="flex-1 overflow-hidden relative">
                    <RecursionTreePanel />
                  </div>
                </div>
              </div>
            </Panel>
          </PanelGroup>
        </div>

      </div>

      {/* Bottom Sticky Intuition Panel */}
      <div className="h-32 shrink-0 border-t border-blue-200 dark:border-slate-700 bg-blue-50 dark:bg-slate-800 z-20 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
        <div className="h-full w-full p-4 overflow-y-auto">
          <IntuitionPanel />
        </div>
      </div>

    </div>
  );
};

export default Dashboard;
