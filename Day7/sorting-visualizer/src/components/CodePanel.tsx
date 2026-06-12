import { useEffect, useRef } from 'react';
import { useStore } from '../store/useStore';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';

export default function CodePanel() {
  const { codeSnippet, activeLine } = useStore();
  const containerRef = useRef<HTMLDivElement>(null);

  // Auto-scroll active line into view
  useEffect(() => {
    if (containerRef.current && activeLine >= 0) {
      const lineEls = containerRef.current.querySelectorAll('.react-syntax-highlighter-line');
      if (lineEls && lineEls[activeLine]) {
        lineEls[activeLine].scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, [activeLine]);

  if (!codeSnippet) {
    return <div className="text-secondary text-sm italic">Select an algorithm to view code.</div>;
  }

  return (
    <div ref={containerRef} className="flex-1 overflow-y-auto text-sm">
      <SyntaxHighlighter
        language="python"
        style={vscDarkPlus}
        customStyle={{ margin: 0, padding: 0, background: 'transparent' }}
        showLineNumbers={true}
        wrapLines={true}
        lineProps={(lineNumber) => {
          const isActive = lineNumber - 1 === activeLine;
          return {
            className: `react-syntax-highlighter-line ${isActive ? 'bg-purple-500/30 border-l-2 border-purple-400' : ''}`,
            style: { display: 'block', padding: '0 8px' }
          };
        }}
      >
        {codeSnippet}
      </SyntaxHighlighter>
    </div>
  );
}
