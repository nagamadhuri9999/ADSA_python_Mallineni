import type { AnimationFrame, ArrayElement } from '../store/useStore';

export function generateBubbleSort(initialArray: ArrayElement[]): AnimationFrame[] {
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
    pushFrame(2, `Pass ${i + 1}: Start iterating up to the unsorted boundary.`);
    let swapped = false;
    pushFrame(3, "Assume the array is sorted (swapped = False).");
    
    for (let j = 0; j < n - i - 1; j++) {
      pushFrame(4, `Examine elements at index ${j} and ${j+1}.`);
      
      array[j].state = 'comparing';
      array[j+1].state = 'comparing';
      comparisons++;
      pushFrame(5, `Compare ${array[j].value} and ${array[j+1].value}.`);
      
      if (array[j].value > array[j + 1].value) {
        array[j].state = 'swapping';
        array[j+1].state = 'swapping';
        pushFrame(6, `Since ${array[j].value} > ${array[j+1].value}, we need to swap them.`);
        
        // Swap
        const temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        swaps++;
        swapped = true;
        pushFrame(7, "Swapped!");
      } else {
        pushFrame(5, `Since ${array[j].value} <= ${array[j+1].value}, they are in correct order.`);
      }
      
      array[j].state = 'default';
      array[j+1].state = 'default';
    }
    
    array[n - i - 1].state = 'sorted';
    pushFrame(8, `The largest remaining element (${array[n - i - 1].value}) has bubbled to its correct sorted position.`);
    
    if (!swapped) {
      pushFrame(9, "No swaps were made in this pass. The array is fully sorted!");
      break;
    }
  }

  // Mark all as sorted
  array.forEach(a => a.state = 'sorted');
  frames.push({
    array: [...array],
    activeLine: 11,
    explanation: "Algorithm complete. The array is sorted.",
    callStack: [],
    comparisons,
    swaps,
    isComplete: true
  });

  return frames;
}
