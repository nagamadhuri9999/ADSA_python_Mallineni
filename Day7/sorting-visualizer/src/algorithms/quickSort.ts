import type { AnimationFrame, ArrayElement } from '../store/useStore';

export function generateQuickSort(initialArray: ArrayElement[]): AnimationFrame[] {
  const frames: AnimationFrame[] = [];
  const array = [...initialArray.map(a => ({ ...a }))];
  let comparisons = 0;
  let swaps = 0;
  let currentCallStack: string[] = [];

  const pushFrame = (activeLine: number, explanation: string) => {
    frames.push({
      array: array.map(a => ({ ...a })),
      activeLine,
      explanation,
      callStack: [...currentCallStack],
      comparisons,
      swaps
    });
  };

  function partition(low: number, high: number): number {
    currentCallStack.push(`partition(${low}, ${high})`);
    
    const pivot = array[high];
    pivot.state = 'pivot';
    pushFrame(7, `Choose the last element (${pivot.value}) as the pivot.`);
    
    let i = low - 1;
    pushFrame(8, `Initialize pointer 'i' to track the boundary of elements smaller than the pivot.`);
    
    for (let j = low; j < high; j++) {
      array[j].state = 'comparing';
      comparisons++;
      pushFrame(10, `Compare ${array[j].value} with pivot ${pivot.value}.`);
      
      if (array[j].value < pivot.value) {
        i++;
        pushFrame(11, `Since ${array[j].value} < ${pivot.value}, increment i to ${i} and swap.`);
        
        array[i].state = 'swapping';
        array[j].state = 'swapping';
        pushFrame(12, `Swapping elements ${array[i].value} and ${array[j].value}.`);
        
        const temp = array[i];
        array[i] = array[j];
        array[j] = temp;
        swaps++;
        
        array[i].state = 'default';
        array[j].state = 'default';
      } else {
        array[j].state = 'default';
      }
    }
    
    pushFrame(13, `Iteration complete. Swap the pivot to its correct sorted position at i + 1 (${i + 1}).`);
    array[i + 1].state = 'swapping';
    array[high].state = 'swapping';
    
    const temp = array[i + 1];
    array[i + 1] = array[high];
    array[high] = temp;
    swaps++;
    
    array[i + 1].state = 'sorted';
    pushFrame(14, `Pivot ${array[i + 1].value} is now in its final sorted position.`);
    
    currentCallStack.pop();
    return i + 1;
  }

  function quickSortHelper(low: number, high: number) {
    if (low < high) {
      currentCallStack.push(`quickSort(${low}, ${high})`);
      pushFrame(2, `Call partition on subarray [${low}-${high}].`);
      
      const pi = partition(low, high);
      
      pushFrame(3, `Recursively Quick Sort the left partition [${low}-${pi - 1}].`);
      quickSortHelper(low, pi - 1);
      
      pushFrame(4, `Recursively Quick Sort the right partition [${pi + 1}-${high}].`);
      quickSortHelper(pi + 1, high);
      
      currentCallStack.pop();
    } else if (low === high) {
      array[low].state = 'sorted';
      pushFrame(1, `Base case: Single element at ${low} is inherently sorted.`);
    }
  }

  pushFrame(0, "Start Quick Sort.");
  quickSortHelper(0, array.length - 1);

  array.forEach(a => a.state = 'sorted');
  frames.push({
    array: [...array],
    activeLine: 5,
    explanation: "Quick Sort finished. The array is fully sorted.",
    callStack: [],
    comparisons,
    swaps,
    isComplete: true
  });

  return frames;
}

export const QUICK_SORT_CODE = `def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1`;
