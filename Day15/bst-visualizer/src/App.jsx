import React, { useState, useEffect, useRef, useMemo } from 'react';
import { Play, Pause, SkipBack, SkipForward, RotateCcw, Sun, Moon } from 'lucide-react';
import { Panel, Group, Separator } from 'react-resizable-panels';
import { BSTSimulator, calculateNodePositions } from './bstLogic';

export default function App() {
  const [simulator] = useState(() => new BSTSimulator());
  const [frames, setFrames] = useState([]);
  const [currentFrameIdx, setCurrentFrameIdx] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState(800);
  const [inputValue, setInputValue] = useState('');
  const [theme, setTheme] = useState('dark');

  const currentFrame = frames[currentFrameIdx] || {
    root: null,
    callStack: [],
    highlightNodeId: null,
    highlightEdgeId: null,
    activeCodeLine: -1,
    explanation: "Welcome to the BST Visualizer. Enter a value to insert or search.",
    stateColor: "default",
    outputArray: []
  };

  const handleInsert = () => {
    if (!inputValue) return;
    const newFrames = simulator.insert(inputValue);
    if (newFrames && newFrames.length > 0) {
      setFrames([...newFrames]);
      setCurrentFrameIdx(0);
      setIsPlaying(true);
    }
    setInputValue('');
  };

  const handleSearch = () => {
    if (!inputValue) return;
    const newFrames = simulator.search(inputValue);
    if (newFrames && newFrames.length > 0) {
      setFrames([...newFrames]);
      setCurrentFrameIdx(0);
      setIsPlaying(true);
    }
    setInputValue('');
  };

  const handleBuildArray = () => {
    if (!inputValue) return;
    const newFrames = simulator.buildFromArray(inputValue);
    if (newFrames && newFrames.length > 0) {
      setFrames([...newFrames]);
      setCurrentFrameIdx(0);
      setIsPlaying(true);
    }
    setInputValue('');
  };

  const handleRandomTree = () => {
    const randomArr = Array.from({length: 7}, () => Math.floor(Math.random() * 90) + 10).join(', ');
    const newFrames = simulator.buildFromArray(randomArr);
    if (newFrames && newFrames.length > 0) {
      setFrames([...newFrames]);
      setCurrentFrameIdx(0);
      setIsPlaying(true);
    }
  };

  const handleTraversal = (type) => {
    let newFrames;
    if (type === 'inorder') newFrames = simulator.traverseInorder();
    if (type === 'preorder') newFrames = simulator.traversePreorder();
    if (type === 'postorder') newFrames = simulator.traversePostorder();
    
    if (newFrames && newFrames.length > 0) {
      setFrames([...newFrames]);
      setCurrentFrameIdx(0);
      setIsPlaying(true);
    }
  };

  const handleReset = () => {
    simulator.root = null;
    setFrames([]);
    setCurrentFrameIdx(0);
    setIsPlaying(false);
  };

  // Playback Loop
  useEffect(() => {
    let timer;
    if (isPlaying && currentFrameIdx < frames.length - 1) {
      timer = setTimeout(() => {
        setCurrentFrameIdx(prev => prev + 1);
      }, speed);
    } else if (currentFrameIdx >= frames.length - 1) {
      setIsPlaying(false);
    }
    return () => clearTimeout(timer);
  }, [isPlaying, currentFrameIdx, frames.length, speed]);

  // Keyboard controls
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.target.tagName.toLowerCase() === 'input') return;
      if (e.key === 'ArrowRight') setCurrentFrameIdx(p => Math.min(frames.length - 1, p + 1));
      if (e.key === 'ArrowLeft') setCurrentFrameIdx(p => Math.max(0, p - 1));
      if (e.key === ' ') { e.preventDefault(); setIsPlaying(p => !p); }
      if (e.key === 'r') handleReset();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [frames.length]);

  // Theme toggler
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  return (
    <div className="app-container">
      <div className="header">
        <h2>Premium BST Visualizer</h2>
        <div className="controls-bar">
          <input 
            type="text" 
            placeholder="e.g. 50 or 10,20,30" 
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleInsert()}
          />
          <button className="primary" onClick={handleInsert}>Insert</button>
          <button onClick={handleSearch}>Search</button>
          <button onClick={handleBuildArray}>Build Array</button>
          <button onClick={handleRandomTree}>Random Tree</button>
          <button onClick={() => handleTraversal('inorder')}>Inorder</button>
          <button onClick={() => handleTraversal('preorder')}>Preorder</button>
          <button onClick={() => handleTraversal('postorder')}>Postorder</button>
          
          <div style={{width: '10px'}}></div>
          
          <button onClick={() => setCurrentFrameIdx(0)} disabled={frames.length === 0} title="Start">
             <SkipBack size={16} />
          </button>
          <button onClick={() => setIsPlaying(!isPlaying)} disabled={frames.length === 0}>
            {isPlaying ? <Pause size={16} /> : <Play size={16} />}
          </button>
          <button onClick={() => setCurrentFrameIdx(frames.length - 1)} disabled={frames.length === 0} title="End">
            <SkipForward size={16} />
          </button>
          <button onClick={handleReset}><RotateCcw size={16} /></button>
          
          <input 
            type="range" 
            min="100" max="2000" 
            value={2100 - speed} 
            onChange={(e) => setSpeed(2100 - Number(e.target.value))} 
            title="Animation Speed"
          />

          <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')} title="Toggle Theme" style={{marginLeft: 'auto'}}>
            {theme === 'dark' ? <Sun size={16} /> : <Moon size={16} />}
          </button>
        </div>
      </div>

      <div style={{ flex: 1, minHeight: 0 }}>
        <Group direction="horizontal">
          <Panel defaultSize={75} minSize={50}>
            <Group direction="vertical">
              <Panel defaultSize={40} minSize={20}>
                <Group direction="horizontal">
                  <Panel defaultSize={40} minSize={20}>
                    <CallStackViewer callStack={currentFrame.callStack} />
                  </Panel>
                  <Separator className="resize-handle" />
                  <Panel defaultSize={60} minSize={20}>
                    <CodeExecutionViewer activeLine={currentFrame.activeCodeLine} operationType={currentFrame.operationType || 'insert'} />
                  </Panel>
                </Group>
              </Panel>
              
              <Separator className="resize-handle horizontal" />
              
              <Panel defaultSize={60} minSize={30}>
                <Group direction="horizontal">
                  <Panel defaultSize={65} minSize={30}>
                    <div className="glass-panel" style={{ height: '100%', padding: 0 }}>
                      <TreeCanvas frame={currentFrame} />
                    </div>
                  </Panel>
                  <Separator className="resize-handle" />
                  <Panel defaultSize={35} minSize={20}>
                     <RecursiveTreeViewer callStack={currentFrame.callStack} operationType={currentFrame.operationType || 'insert'} />
                  </Panel>
                </Group>
              </Panel>
            </Group>
          </Panel>

          <Separator className="resize-handle" />

          <Panel defaultSize={25} minSize={15}>
            <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: '16px' }}>
              <div className="glass-panel" style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                <h3>Explanation & Output</h3>
                <p style={{ marginTop: '12px', fontSize: '15px', lineHeight: '1.6', color: 'var(--text-primary)' }}>
                  {currentFrame.explanation}
                </p>
                
                {currentFrame.outputArray && currentFrame.outputArray.length > 0 && (
                  <div style={{ marginTop: '16px', padding: '12px', background: 'var(--bg-secondary)', borderRadius: '8px', borderLeft: '4px solid var(--accent-primary)' }}>
                    <strong>Traversal Output:</strong>
                    <div style={{ marginTop: '8px', fontFamily: 'monospace', color: 'var(--text-primary)', wordBreak: 'break-all' }}>
                      {currentFrame.outputArray.join(' → ')}
                    </div>
                  </div>
                )}

                {frames.length > 0 && (
                  <div style={{ marginTop: 'auto', paddingTop: '16px', fontSize: '12px', color: 'var(--text-secondary)' }}>
                    Step {currentFrameIdx + 1} of {frames.length}
                  </div>
                )}
              </div>
              
              <ComplexityDashboard />
            </div>
          </Panel>
        </Group>
      </div>
    </div>
  );
}

// ------------------------------------------------------------------
// Sub-components
// ------------------------------------------------------------------

function CallStackViewer({ callStack }) {
  return (
    <div className="glass-panel" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <h3>Call Stack</h3>
      <div style={{ marginTop: '12px', flex: 1, overflowY: 'auto' }}>
        {callStack.length === 0 ? (
          <div style={{ color: 'var(--text-secondary)', fontSize: '13px' }}>Stack is empty.</div>
        ) : (
          [...callStack].reverse().map((call, i) => (
            <div key={i} className={`stack-frame ${i === 0 ? 'active' : ''}`}>
              {call}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

function CodeExecutionViewer({ activeLine, operationType }) {
  const codes = {
    insert: `def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root`.split('\n'),
    
    search: `def search(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)`.split('\n'),
    
    inorder: `def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)`.split('\n'),
    
    preorder: `def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)`.split('\n'),
    
    postorder: `def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)`.split('\n')
  };

  const code = codes[operationType] || codes['insert'];

  return (
    <div className="glass-panel" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <h3>Execution: {operationType}()</h3>
      <div style={{ marginTop: '12px', background: 'var(--bg-primary)', padding: '8px', borderRadius: '8px', flex: 1, overflowY: 'auto' }}>
        {code.map((line, i) => (
          <div key={i} className={`code-line ${activeLine === i + 1 ? 'active' : ''}`}>
            {line}
          </div>
        ))}
      </div>
    </div>
  );
}

function RecursiveTreeViewer({ callStack, operationType }) {
  return (
    <div className="glass-panel" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <h3>Recursive Tree</h3>
      <div style={{ marginTop: '12px', flex: 1, overflowY: 'auto', fontFamily: 'monospace', fontSize: '13px', color: 'var(--text-secondary)' }}>
        {callStack.length === 0 ? (
          <div>No active recursion.</div>
        ) : (
          callStack.map((call, i) => (
            <div key={i} style={{ 
              marginLeft: `${i * 16}px`, 
              color: i === callStack.length - 1 ? 'var(--node-current)' : 'inherit',
              borderLeft: '1px solid var(--border-color)',
              paddingLeft: '8px',
              position: 'relative'
            }}>
              <span style={{ position: 'absolute', left: 0, top: '8px', width: '8px', height: '1px', background: 'var(--border-color)'}}></span>
              {call}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

function TreeCanvas({ frame }) {
  const containerRef = useRef(null);
  const [dimensions, setDimensions] = useState({ width: 600, height: 600 });

  useEffect(() => {
    if (containerRef.current) {
      setDimensions({
        width: containerRef.current.clientWidth,
        height: containerRef.current.clientHeight
      });
    }
  }, []);

  const { nodes, edges } = useMemo(() => {
    return calculateNodePositions(frame.root, dimensions.width, dimensions.height);
  }, [frame.root, dimensions]);

  // Color mapping
  const getColor = (nodeId, isCurrentColor) => {
    if (nodeId === frame.highlightNodeId) return `var(--node-${frame.stateColor})`;
    return `var(--node-default)`;
  };

  return (
    <div ref={containerRef} style={{ width: '100%', height: '100%' }}>
      <svg width={dimensions.width} height={dimensions.height}>
        {/* Edges */}
        {edges.map(edge => (
          <line
            key={edge.id}
            x1={edge.x1} y1={edge.y1} x2={edge.x2} y2={edge.y2}
            stroke={edge.id === frame.highlightEdgeId ? `var(--node-${frame.stateColor})` : 'var(--border-color)'}
            strokeWidth={edge.id === frame.highlightEdgeId ? 4 : 2}
            className="tree-edge"
          />
        ))}
        {/* Nodes */}
        {nodes.map(node => (
          <g key={node.id} className="tree-node" transform={`translate(${node.x}, ${node.y})`}>
            <circle
              r={18}
              fill="var(--bg-primary)"
              stroke={getColor(node.id, true)}
              strokeWidth={node.id === frame.highlightNodeId ? 4 : 2}
            />
            <text
              textAnchor="middle"
              dominantBaseline="central"
              fill="var(--text-primary)"
              fontSize="14px"
              fontWeight="bold"
            >
              {node.val}
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}

function ComplexityDashboard() {
  return (
    <div className="glass-panel" style={{ height: 'auto' }}>
      <h3>Complexity</h3>
      <table style={{ width: '100%', marginTop: '12px', fontSize: '13px', textAlign: 'left', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '1px solid var(--border-color)' }}>
            <th style={{ paddingBottom: '8px' }}>Op</th>
            <th style={{ paddingBottom: '8px' }}>Average</th>
            <th style={{ paddingBottom: '8px' }}>Worst</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style={{ paddingTop: '8px' }}>Search</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-current)' }}>O(log N)</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-delete)' }}>O(N)</td>
          </tr>
          <tr>
            <td style={{ paddingTop: '8px' }}>Insert</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-current)' }}>O(log N)</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-delete)' }}>O(N)</td>
          </tr>
          <tr>
            <td style={{ paddingTop: '8px' }}>Delete</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-current)' }}>O(log N)</td>
            <td style={{ paddingTop: '8px', color: 'var(--node-delete)' }}>O(N)</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
