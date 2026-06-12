import { useState } from 'react';
import DryRunPanel from './DryRunPanel';
import IntuitionPanel from './IntuitionPanel';
import StatisticsPanel from './StatisticsPanel';
import { Terminal, Brain, BarChart } from 'lucide-react';

export default function BottomPanel() {
  const [activeTab, setActiveTab] = useState<'dryrun' | 'intuition' | 'stats'>('dryrun');

  return (
    <div className="flex flex-col h-full bg-panel backdrop-blur-md rounded-xl shadow-panel border border-border overflow-hidden">
      {/* Tabs Header */}
      <div className="flex items-center gap-2 px-4 pt-3 pb-0 border-b border-border bg-btn/30">
        <button 
          onClick={() => setActiveTab('dryrun')}
          className={`flex items-center gap-2 px-4 py-2 text-sm font-bold rounded-t-lg transition-colors -mb-[1px] border-b-2 ${activeTab === 'dryrun' ? 'text-blue-500 border-blue-500' : 'text-secondary border-transparent hover:text-primary hover:bg-btn/50'}`}
        >
          <Terminal size={16} /> Dry Run Log
        </button>
        <button 
          onClick={() => setActiveTab('intuition')}
          className={`flex items-center gap-2 px-4 py-2 text-sm font-bold rounded-t-lg transition-colors -mb-[1px] border-b-2 ${activeTab === 'intuition' ? 'text-green-500 border-green-500' : 'text-secondary border-transparent hover:text-primary hover:bg-btn/50'}`}
        >
          <Brain size={16} /> Intuition & Analogy
        </button>
        <button 
          onClick={() => setActiveTab('stats')}
          className={`flex items-center gap-2 px-4 py-2 text-sm font-bold rounded-t-lg transition-colors -mb-[1px] border-b-2 ${activeTab === 'stats' ? 'text-yellow-500 border-yellow-500' : 'text-secondary border-transparent hover:text-primary hover:bg-btn/50'}`}
        >
          <BarChart size={16} /> Statistics & Complexity
        </button>
      </div>

      {/* Tab Content */}
      <div className="flex-1 p-4 overflow-y-auto">
        <div className={activeTab === 'dryrun' ? 'block h-full' : 'hidden'}>
          <DryRunPanel />
        </div>
        <div className={activeTab === 'intuition' ? 'block h-full' : 'hidden'}>
          <IntuitionPanel />
        </div>
        <div className={activeTab === 'stats' ? 'block h-full' : 'hidden'}>
          <StatisticsPanel />
        </div>
      </div>
    </div>
  );
}
