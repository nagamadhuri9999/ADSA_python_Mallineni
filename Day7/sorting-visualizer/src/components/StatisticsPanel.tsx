import { useStore } from '../store/useStore';

export default function StatisticsPanel() {
  const { comparisons, swaps, metrics, arraySize } = useStore();

  return (
    <div className="flex flex-col gap-4 text-sm">
      <div className="grid grid-cols-2 gap-3">
        <div className="bg-btn p-3 rounded-lg border border-border shadow-inner">
          <span className="text-secondary text-xs block uppercase font-bold tracking-wider mb-1">Comparisons</span>
          <span className="text-primary font-black text-xl">{comparisons}</span>
        </div>
        <div className="bg-btn p-3 rounded-lg border border-border shadow-inner">
          <span className="text-secondary text-xs block uppercase font-bold tracking-wider mb-1">Swaps</span>
          <span className="text-primary font-black text-xl">{swaps}</span>
        </div>
      </div>

      {metrics && (
        <div className="grid grid-cols-1 gap-2 text-xs font-mono">
          <div className="flex justify-between items-center bg-btn p-2 rounded">
            <span className="text-secondary">Array Size</span>
            <span className="text-blue-300">N = {arraySize}</span>
          </div>
          <div className="flex justify-between items-center bg-btn p-2 rounded">
            <span className="text-secondary">Best Case</span>
            <span className="text-green-400">{metrics.timeComplexity.best}</span>
          </div>
          <div className="flex justify-between items-center bg-btn p-2 rounded">
            <span className="text-secondary">Average Case</span>
            <span className="text-yellow-400">{metrics.timeComplexity.avg}</span>
          </div>
          <div className="flex justify-between items-center bg-btn p-2 rounded">
            <span className="text-secondary">Worst Case</span>
            <span className="text-red-400">{metrics.timeComplexity.worst}</span>
          </div>
          <div className="flex justify-between items-center bg-btn p-2 rounded mt-2 border-t border-border pt-2">
            <span className="text-secondary">Space Complexity</span>
            <span className="text-purple-400">{metrics.spaceComplexity}</span>
          </div>
        </div>
      )}
    </div>
  );
}
