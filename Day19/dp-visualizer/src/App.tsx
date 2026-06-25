import { useState, useEffect } from 'react';
import { useExecution } from './context/ExecutionContext';
import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import CodeEditorPanel from './components/CodeEditorPanel';
import VisualizationPanel from './components/VisualizationPanel';
import ControlsPanel from './components/ControlsPanel';
import VariablesPanel from './components/VariablesPanel';
import ExplanationPanel from './components/ExplanationPanel';
import { ExecutionProvider } from './context/ExecutionContext';

// Custom resize handle component
const ResizeHandle = ({ horizontal = false }) => (
  <PanelResizeHandle className={`relative flex items-center justify-center bg-border transition-colors hover:bg-accent/50 dark:hover:bg-accent/50 group ${horizontal ? 'h-full w-[3px] mx-[-1px] cursor-col-resize z-10' : 'w-full h-[3px] my-[-1px] cursor-row-resize z-10'}`}>
    <div className={`bg-transparent transition-colors group-hover:bg-accent ${horizontal ? 'w-full h-8 rounded-full' : 'h-full w-8 rounded-full'}`} />
  </PanelResizeHandle>
);

function App() {
  const [isDarkMode, setIsDarkMode] = useState(true);

  // Apply dark mode class to html element
  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDarkMode]);

  return (
    <ExecutionProvider>
      <AppContent isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
    </ExecutionProvider>
  );
}

const AppContent: React.FC<{ isDarkMode: boolean, setIsDarkMode: (val: boolean) => void }> = ({ isDarkMode, setIsDarkMode }) => {
  const { zoomLevel, setZoomLevel } = useExecution();
  
  useEffect(() => {
    const handleWheel = (e: WheelEvent) => {
      if (e.ctrlKey) {
        e.preventDefault(); // Prevent native browser zoom
        // e.deltaY is negative when zooming in (scrolling up/pinching out)
        // e.deltaY is positive when zooming out (scrolling down/pinching in)
        const zoomChange = e.deltaY * -0.001; 
        setZoomLevel((prevZoom: number) => {
          const newZoom = prevZoom + zoomChange;
          return Math.max(0.5, Math.min(2.5, newZoom)); // Clamp between 0.5 and 2.5
        });
      }
    };

    // We must pass { passive: false } to allow e.preventDefault() on touchpads
    window.addEventListener('wheel', handleWheel, { passive: false });
    return () => {
      window.removeEventListener('wheel', handleWheel);
    };
  }, [setZoomLevel]);

  return (
    <div 
      className="h-screen w-screen overflow-hidden flex flex-col bg-background text-foreground transition-colors duration-300"
      style={{ fontSize: `${zoomLevel}rem` } as React.CSSProperties}
    >
      <Header isDarkMode={isDarkMode} setIsDarkMode={setIsDarkMode} />
      
      <div className="flex-1 flex overflow-hidden">
        <PanelGroup orientation="horizontal">
          <Panel defaultSize={20} minSize={15} maxSize={30}>
            <Sidebar />
          </Panel>
          
          <ResizeHandle horizontal />
          
          <Panel defaultSize={80} minSize={50}>
            <PanelGroup orientation="vertical">
              <Panel defaultSize={65} minSize={30}>
                <PanelGroup orientation="horizontal">
                  <Panel defaultSize={35} minSize={20}>
                    <CodeEditorPanel />
                  </Panel>
                  
                  <ResizeHandle horizontal />
                  
                  <Panel defaultSize={65} minSize={30}>
                    <VisualizationPanel />
                  </Panel>
                </PanelGroup>
              </Panel>
              
              <ResizeHandle />
              
              <Panel defaultSize={35} minSize={20}>
                <PanelGroup orientation="horizontal">
                  <Panel defaultSize={40} minSize={20}>
                    <VariablesPanel />
                  </Panel>
                  
                  <ResizeHandle horizontal />
                  
                  <Panel defaultSize={60} minSize={30}>
                    <ExplanationPanel />
                  </Panel>
                </PanelGroup>
              </Panel>
            </PanelGroup>
          </Panel>
        </PanelGroup>
      </div>
      
      <ControlsPanel />
    </div>
  );
};

export default App;
