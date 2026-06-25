import React from 'react';
import { Folder } from 'lucide-react';

const Sidebar: React.FC = () => {

  const topics = [
    {
      id: 'fundamentals',
      name: '1. DP Fundamentals',
      subtopics: ['Introduction', 'Overlapping Subproblems', 'Optimal Substructure']
    },
    {
      id: 'memoization',
      name: '2. Memoization',
      subtopics: ['Fibonacci', 'Call Stack', 'Recursive Tree']
    },
    {
      id: 'tabulation',
      name: '3. Tabulation',
      subtopics: ['Fibonacci', 'DP Array', 'Space Optimization']
    },
    {
      id: 'lis',
      name: '4. LIS',
      subtopics: ['O(N²)', 'O(N log N)']
    }
  ];

  return (
    <div className="w-64 border-r border-border bg-panel glass-panel flex flex-col shrink-0">
      <div className="p-4 border-b border-border font-medium text-sm text-accent uppercase tracking-wider">
        Dynamic Programming
      </div>
      
      <div className="flex-1 overflow-y-auto p-2">
        {topics.map((topic) => (
          <div key={topic.id} className="mb-2">
            <div className="flex items-center gap-2 p-2 hover:bg-black/5 rounded cursor-pointer text-sm font-medium">
              <Folder size={16} className="text-accent" />
              {topic.name}
            </div>
            
            <div className="pl-6 flex flex-col gap-1 mt-1">
              {topic.subtopics.map((sub) => (
                <div 
                  key={sub}
                  className={`flex items-center gap-2 p-1.5 pl-3 rounded text-sm cursor-pointer transition-colors
                    ${(topic.id === 'memoization' && sub === 'Fibonacci') ? 'bg-accent/10 text-accent' : 'hover:bg-black/5 opacity-70 hover:opacity-100'}
                  `}
                >
                  <div className="w-1.5 h-1.5 rounded-full bg-current opacity-50" />
                  {sub}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      
      {/* Complexity Dashboard Summary */}
      <div className="p-4 border-t border-border bg-black/5">
        <div className="text-xs font-semibold uppercase tracking-wider mb-3 opacity-70">Complexity</div>
        <div className="flex justify-between items-center text-sm mb-2">
          <span>Time:</span>
          <code className="bg-black/10 px-1.5 py-0.5 rounded text-accent">O(N)</code>
        </div>
        <div className="flex justify-between items-center text-sm">
          <span>Space:</span>
          <code className="bg-black/10 px-1.5 py-0.5 rounded text-accent">O(N)</code>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
