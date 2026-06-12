import type { AnimationFrame, ArrayElement } from '../store/useStore';

export function generateInsertionSort(initialArray: ArrayElement[]): AnimationFrame[] {
  const frames: AnimationFrame[] = [];
  const array = [...initialArray.map(a => ({ ...a }))];
  let comparisons = 0;
  let swaps = 0; // Writes in insertion sort
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

  array[0].state = 'sorted';
  pushFrame(1, "Assume the first element is already sorted.");

  for (let i = 1; i < n; i++) {
    pushFrame(2, `Look at the next unsorted element at index ${i}.`);
    
    const key = array[i];
    key.state = 'pivot';
    pushFrame(3, `Store ${key.value} as the 'key' to be inserted into the sorted portion.`);
    
    let j = i - 1;
    pushFrame(4, `Start comparing from right to left in the sorted portion.`);
    
    while (j >= 0) {
      comparisons++;
      array[j].state = 'comparing';
      pushFrame(6, `Is the sorted element ${array[j].value} greater than the key ${key.value}?`);
      
      if (array[j].value > key.value) {
        pushFrame(7, `Yes, ${array[j].value} > ${key.value}. Shift ${array[j].value} one position to the right.`);
        
        array[j + 1] = { ...array[j], state: 'swapping' };
        array[j].state = 'default';
        swaps++;
        pushFrame(7, `Element shifted.`);
        
        array[j + 1].state = 'sorted';
        j -= 1;
        pushFrame(8, `Move to the next element on the left.`);
      } else {
        array[j].state = 'sorted';
        pushFrame(6, `No, ${array[j].value} <= ${key.value}. We found the correct insertion spot.`);
        break;
      }
    }
    
    array[j + 1] = { ...key, state: 'sorted' };
    swaps++;
    pushFrame(10, `Insert the key ${key.value} at index ${j + 1}.`);
  }

  frames.push({
    array: [...array],
    activeLine: 12,
    explanation: "Insertion Sort finished. All elements are in the sorted portion.",
    callStack: [],
    comparisons,
    swaps,
    isComplete: true
  });

  return frames;
}

export const INSERTION_SORT_CODE = `def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr`;
