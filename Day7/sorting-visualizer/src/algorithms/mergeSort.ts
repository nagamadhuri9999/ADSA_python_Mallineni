import type { AnimationFrame, ArrayElement } from '../store/useStore';

export function generateMergeSort(initialArray: ArrayElement[]): AnimationFrame[] {
  const frames: AnimationFrame[] = [];
  const array = [...initialArray.map(a => ({ ...a }))];
  const auxiliaryArray = [...initialArray.map(a => ({ ...a }))];
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

  function mergeSortHelper(startIdx: number, endIdx: number) {
    if (startIdx === endIdx) return;
    
    currentCallStack.push(`mergeSort(${startIdx}, ${endIdx})`);
    pushFrame(1, `Divide: Considering subarray from index ${startIdx} to ${endIdx}.`);
    
    const middleIdx = Math.floor((startIdx + endIdx) / 2);
    pushFrame(2, `Calculate mid point: ${middleIdx}.`);
    
    pushFrame(5, `Recursively sort the left half: [${startIdx} to ${middleIdx}].`);
    mergeSortHelper(startIdx, middleIdx);
    
    pushFrame(6, `Recursively sort the right half: [${middleIdx + 1} to ${endIdx}].`);
    mergeSortHelper(middleIdx + 1, endIdx);
    
    doMerge(startIdx, middleIdx, endIdx);
    currentCallStack.pop();
  }

  function doMerge(startIdx: number, middleIdx: number, endIdx: number) {
    currentCallStack.push(`merge(${startIdx}, ${middleIdx}, ${endIdx})`);
    pushFrame(7, `Merging two sorted halves: [${startIdx}-${middleIdx}] and [${middleIdx+1}-${endIdx}].`);
    
    for (let i = startIdx; i <= endIdx; i++) {
      auxiliaryArray[i] = { ...array[i] };
    }

    let i = startIdx;
    let j = middleIdx + 1;
    let k = startIdx;

    while (i <= middleIdx && j <= endIdx) {
      comparisons++;
      array[k].state = 'comparing';
      pushFrame(9, `Compare left element (${auxiliaryArray[i].value}) and right element (${auxiliaryArray[j].value}).`);
      
      if (auxiliaryArray[i].value <= auxiliaryArray[j].value) {
        pushFrame(10, `Left is smaller. Overwrite index ${k} with ${auxiliaryArray[i].value}.`);
        array[k] = { ...auxiliaryArray[i], state: 'swapping' };
        i++;
      } else {
        pushFrame(13, `Right is smaller. Overwrite index ${k} with ${auxiliaryArray[j].value}.`);
        array[k] = { ...auxiliaryArray[j], state: 'swapping' };
        j++;
      }
      swaps++;
      pushFrame(15, `Move to next position in main array.`);
      array[k].state = 'sorted';
      k++;
    }

    while (i <= middleIdx) {
      pushFrame(17, `Copy remaining elements from left half.`);
      array[k] = { ...auxiliaryArray[i], state: 'swapping' };
      swaps++;
      array[k].state = 'sorted';
      i++;
      k++;
    }
    
    currentCallStack.pop();
  }

  pushFrame(0, "Start Merge Sort.");
  mergeSortHelper(0, array.length - 1);

  frames.push({
    array: [...array],
    activeLine: 24,
    explanation: "Merge Sort finished. The array is fully merged and sorted.",
    callStack: [],
    comparisons,
    swaps,
    isComplete: true
  });

  return frames;
}

export const MERGE_SORT_CODE = `def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr`;
