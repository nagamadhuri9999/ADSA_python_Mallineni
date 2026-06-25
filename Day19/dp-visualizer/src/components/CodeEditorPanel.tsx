import React, { useRef, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { useExecution } from '../context/ExecutionContext';
import type { editor } from 'monaco-editor';

const CodeEditorPanel: React.FC = () => {
  const { code, setCode, activeLine } = useExecution();
  const editorRef = useRef<editor.IStandaloneCodeEditor | null>(null);
  const decorationsRef = useRef<editor.IEditorDecorationsCollection | null>(null);

  const handleEditorDidMount = (editor: editor.IStandaloneCodeEditor) => {
    editorRef.current = editor;
    decorationsRef.current = editor.createDecorationsCollection([]);
  };

  useEffect(() => {
    if (editorRef.current && decorationsRef.current) {
      if (activeLine !== null) {
        decorationsRef.current.set([{
          range: new (window as any).monaco.Range(activeLine, 1, activeLine, 1),
          options: {
            isWholeLine: true,
            className: 'myLineDecoration',
            marginClassName: 'myLineDecoration'
          }
        }]);
        editorRef.current.revealLineInCenter(activeLine);
      } else {
        decorationsRef.current.set([]);
      }
    }
  }, [activeLine]);

  return (
    <div className="flex-1 flex flex-col bg-panel glass-panel h-full relative">
      <div className="h-10 border-b border-border flex items-center px-4 bg-black/5 shrink-0">
        <span className="text-sm font-medium opacity-80">fibonacci_memo.py</span>
      </div>
      <div className="flex-1 relative code-editor-container">
        <Editor
          height="100%"
          defaultLanguage="python"
          theme="vs-dark"
          value={code}
          onChange={(val) => setCode(val || '')}
          onMount={handleEditorDidMount}
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            lineHeight: 24,
            padding: { top: 16 },
            scrollBeyondLastLine: false,
            smoothScrolling: true,
            cursorBlinking: "smooth",
            fontFamily: "var(--font-mono)",
            readOnly: true, // Readonly during visualization
          }}
        />
        
        {/* CSS for custom line highlight animation */}
        <style>{`
          .myLineDecoration {
            background: var(--accent-bg);
            box-shadow: inset 3px 0 0 0 var(--accent);
          }
        `}</style>
      </div>
    </div>
  );
};

export default CodeEditorPanel;
