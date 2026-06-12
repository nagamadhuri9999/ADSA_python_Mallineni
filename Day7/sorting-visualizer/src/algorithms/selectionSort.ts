import type { AnimationFrame, ArrayElement } from '../store/useStore';

export function generateSelectionSort(initialArray: ArrayElement[]): AnimationFrame[] {
  const frames: AnimationFrame[] = [];
  const array = [...initialArray.map(a => ({ ...a }))];
  let comparisons = 0;
  let swaps = 0;
  const n = array.length;

  const pushFrame = (activeLine: number, explanation: string) => {
    frames.push({
      array: array.map(a => ({ ...a })),
      activeLine,
      explanation,
      callStack: [],
      comparisons,
      swaps
    });
  };

  pushFrame(1, "Initialize array length n.");
  
  for (let i = 0; i < n - 1; i++) {
    pushFrame(2, `Pass ${i + 1}: Find the minimum element in the remaining unsorted array.`);
    let min_idx = i;
    array[min_idx].state = 'minimum';
    pushFrame(3, `Assume the first unsorted element (${array[min_idx].value}) is the minimum.`);
    
    for (let j = i + 1; j < n; j++) {
      pushFrame(4, `Examine element at index ${j}.`);
      
      array[j].state = 'comparing';
      comparisons++;
      pushFrame(5, `Compare current element (${array[j].value}) with current minimum (${array[min_idx].value}).`);
      
      if (array[j].value < array[min_idx].value) {
        array[min_idx].state = 'default';
        min_idx = j;
        array[min_idx].state = 'minimum';
        pushFrame(6, `Found a new minimum! Update min_idx to ${j}.`);
      } else {
        array[j].state = 'default';
      }
    }
    
    pushFrame(8, `End of pass. The absolute minimum is ${array[min_idx].value}. Swap it with the first unsorted position.`);
    if (min_idx !== i) {
      array[i].state = 'swapping';
      array[min_idx].state = 'swapping';
      pushFrame(9, `Swapping ${array[i].value} and ${array[min_idx].value}.`);
      
      const temp = array[i];
      array[i] = array[min_idx];
      array[min_idx] = temp;
      swaps++;
    }
    
    array[i].state = 'sorted';
    if (min_idx !== i) array[min_idx].state = 'default';
    pushFrame(10, `The element ${array[i].value} is now locked in its final sorted position.`);
  }

  // The last element is inherently sorted
  array[n - 1].state = 'sorted';
  pushFrame(11, "Algorithm complete. The array is fully sorted.");
  
  frames.push({
    array: [...array],
    activeLine: 12,
    explanation: "Selection Sort finished.",
    callStack: [],
    comparisons,
    swaps,
    isComplete: true
  });

  return frames;
}

export const SELECTION_SORT_CODE = `def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr`;
