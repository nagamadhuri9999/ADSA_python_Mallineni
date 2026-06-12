import React from 'react';
import { useStore } from '../../store/useStore';

const MERGE_SORT_CODE = [
  /* 1 */ "def merge(left, right):",
  /* 2 */ "  result = []",
  /* 3 */ "",
  /* 4 */ "  i = 0",
  /* 5 */ "  j = 0",
  /* 6 */ "",
  /* 7 */ "  while i < len(left) and j < len(right):",
  /* 8 */ "      if left[i] <= right[j]:",
  /* 9 */ "          result.append(left[i])",
  /* 10 */ "          i += 1",
  /* 11 */ "      else:",
  /* 12 */ "          result.append(right[j])",
  /* 13 */ "          j += 1",
  /* 14 */ "",
  /* 15 */ "  result.extend(left[i:])",
  /* 16 */ "  result.extend(right[j:])",
  /* 17 */ "",
  /* 18 */ "  return result",
  /* 19 */ "",
  /* 20 */ "def merge_sort(nums):",
  /* 21 */ "  if len(nums) <= 1:",
  /* 22 */ "      return nums",
  /* 23 */ "",
  /* 24 */ "  mid = len(nums) // 2",
  /* 25 */ "",
  /* 26 */ "  left = merge_sort(nums[:mid])",
  /* 27 */ "  right = merge_sort(nums[mid:])",
  /* 28 */ "",
  /* 29 */ "  return merge(left, right)"
];

const QUICK_SORT_CODE = [
  /* 1 */ "def partition(arr, low, high):",
  /* 2 */ "    pivot = arr[high]",
  /* 3 */ "    i = low - 1",
  /* 4 */ "",
  /* 5 */ "    for j in range(low, high):",
  /* 6 */ "        if arr[j] < pivot:",
  /* 7 */ "            i += 1",
  /* 8 */ "            arr[i], arr[j] = arr[j], arr[i]",
  /* 9 */ "",
  /* 10 */ "    arr[i + 1], arr[high] = arr[high], arr[i + 1]",
  /* 11 */ "    return i + 1",
  /* 12 */ "",
  /* 13 */ "def quick_sort(arr, low, high):",
  /* 14 */ "    if low < high:",
  /* 15 */ "        pi = partition(arr, low, high)",
  /* 16 */ "",
  /* 17 */ "        quick_sort(arr, low, pi - 1)",
  /* 18 */ "        quick_sort(arr, pi + 1, high)"
];

const CodePanel: React.FC = () => {
  const { traces, currentTraceIndex, algorithm } = useStore();
  const currentStep = traces[currentTraceIndex];
  const activeLine = currentStep?.activeLine || 0;

  const codeLines = algorithm === 'merge' ? MERGE_SORT_CODE : QUICK_SORT_CODE;

  const renderCode = (lines: string[]) => {
    return lines.map((line, idx) => {
      const lineNum = idx + 1;
      const isActive = lineNum === activeLine;
      
      return (
        <div 
          key={lineNum}
          className={`flex px-4 py-0.5 font-mono text-sm ${
            isActive 
              ? 'bg-blue-500/20 text-blue-700 dark:text-blue-300 border-l-2 border-blue-500' 
              : 'text-slate-600 dark:text-slate-400 border-l-2 border-transparent'
          }`}
        >
          <span className="w-6 shrink-0 text-right mr-4 select-none opacity-50 text-xs flex items-center justify-end">
            {lineNum}
          </span>
          <pre className="m-0 whitespace-pre">
            {line}
          </pre>
        </div>
      );
    });
  };

  return (
    <div className="py-2">
      {renderCode(codeLines)}
    </div>
  );
};

export default CodePanel;
