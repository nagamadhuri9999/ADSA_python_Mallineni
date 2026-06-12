import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import Header from './Header';
import ArrayVisualizer from './ArrayVisualizer';
import CodePanel from './CodePanel';
import BottomPanel from './BottomPanel';

export default function Dashboard() {
  return (
    <div className="flex flex-col h-screen p-2 sm:p-4 gap-2 sm:gap-4 bg-base transition-colors duration-300">
      <Header />
      
      <div className="flex-1 flex flex-col gap-2 sm:gap-4 min-h-0">
        
        {/* Top: Side-by-side Resizable Panels */}
        <div className="flex-[5] min-h-0">
          <PanelGroup orientation="horizontal" id="dashboard-split" className="h-full">
            <Panel defaultSize={65} minSize={30} className="bg-panel backdrop-blur-md rounded-xl shadow-panel border border-border flex flex-col p-4 sm:p-6">
              <h2 className="text-xs font-bold text-secondary mb-2 uppercase tracking-wider">Visualization Area</h2>
              <div className="flex-1 flex items-end justify-center min-h-0">
                <ArrayVisualizer />
              </div>
            </Panel>

            <PanelResizeHandle className="w-4 flex items-center justify-center group cursor-col-resize outline-none">
              <div className="w-1 h-8 rounded-full bg-border group-hover:bg-blue-500 group-active:bg-blue-600 transition-colors" />
            </PanelResizeHandle>

            <Panel defaultSize={35} minSize={20} className="bg-panel backdrop-blur-md rounded-xl shadow-panel border border-border flex flex-col p-4">
              <h2 className="text-xs font-bold text-purple-400 mb-3 uppercase tracking-wider flex-shrink-0">Code Execution</h2>
              <div className="flex-1 overflow-y-auto min-h-0 -mx-4 px-4 scrollbar-thin scrollbar-thumb-border scrollbar-track-transparent">
                <CodePanel />
              </div>
            </Panel>
          </PanelGroup>
        </div>

        {/* Bottom: Explanation Tabs */}
        <div className="flex-[3] min-h-0">
          <BottomPanel />
        </div>

      </div>
    </div>
  );
}
