import { useStore } from '../store/useStore';

export default function IntuitionPanel() {
  const { algorithmName, callStack } = useStore();

  const getIntuition = () => {
    switch (algorithmName) {
      case "Bubble Sort":
        return "Imagine bubbles in water. Larger bubbles rise to the top. Similarly, larger elements slowly move towards the end of the array after every pass.";
      case "Selection Sort":
        return "Imagine finding the shortest student in a classroom and placing them at the front of the line.";
      case "Insertion Sort":
        return "Imagine arranging playing cards in your hand. You pick up a card and place it in the correct sorted position among the cards you already hold.";
      case "Merge Sort":
        return "Divide & Conquer: Break the big problem into smaller problems. Sort the small pieces, then merge them back together in order.";
      case "Quick Sort":
        return "Choose a leader (pivot). Put smaller values on one side, and larger values on the other side.";
      default:
        return "Select an algorithm to view its intuition and analogy.";
    }
  };

  return (
    <div className="flex-1 flex flex-col gap-4 text-sm">
      <div className="text-primary italic border-l-2 border-green-500 pl-3 leading-relaxed">
        "{getIntuition()}"
      </div>

      {/* Recursion Stack */}
      {callStack && callStack.length > 0 && (
        <div className="mt-2 flex flex-col flex-1 max-h-[150px]">
          <span className="text-xs font-bold text-secondary uppercase mb-1">Call Stack</span>
          <div className="bg-slate-900 rounded-lg p-2 font-mono text-xs text-yellow-300 flex-1 overflow-y-auto shadow-inner border border-slate-700">
            {callStack.map((call, idx) => (
              <div key={idx} className={`${idx === callStack.length - 1 ? 'font-bold text-yellow-400' : 'text-yellow-600/70'}`}>
                {'> '.repeat(idx)}{call}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
