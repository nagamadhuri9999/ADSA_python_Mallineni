import type { Edge, Node } from '@xyflow/react';
import type { CallStackFrame, TraceStep } from './useStore';

let stepIdCounter = 0;

export function generateQuickSortTraces(initialArray: number[]): TraceStep[] {
  const traces: TraceStep[] = [];
  const currentStack: CallStackFrame[] = [];
  const treeNodes: Node[] = [];
  const treeEdges: Edge[] = [];
  
  // Create root node
  const rootId = 'node-root';
  treeNodes.push({
    id: rootId,
    position: { x: 400, y: 50 },
    data: { label: `[${initialArray.join(', ')}]`, isActive: false, isCompleted: false },
    type: 'default'
  });

  const snapshot = (
    type: TraceStep['type'],
    array: number[],
    activeIndices: number[],
    activeLine: number,
    explanationTitle: string,
    explanationText: string,
    pivotIndex?: number,
    pointerIndices?: number[]
  ) => {
    traces.push({
      id: `step-${stepIdCounter++}`,
      type,
      array: [...array],
      activeIndices: [...activeIndices],
      callStack: JSON.parse(JSON.stringify(currentStack)),
      treeNodes: JSON.parse(JSON.stringify(treeNodes)),
      treeEdges: JSON.parse(JSON.stringify(treeEdges)),
      activeLine,
      explanationTitle,
      explanationText,
      pivotIndex,
      pointerIndices
    });
  };

  const partition = (arr: number[], low: number, high: number): number => {
    const frameId = `frame-partition-${low}-${high}`;
    
    currentStack.unshift({
      id: frameId,
      functionName: 'partition',
      parameters: `low=${low}, high=${high}`,
      localVars: `pivot=?, i=?`,
      status: 'Started'
    });

    snapshot('partition', arr, Array.from({ length: high - low + 1 }, (_, k) => low + k), 1, 'Calling Partition', `We need to partition the sub-array from index ${low} to ${high}.`);

    const pivot = arr[high];
    currentStack[0].localVars = `pivot=${pivot}, i=?`;
    snapshot('partition', arr, [high], 2, 'Selecting Pivot', `We choose the last element (${pivot}) as our pivot.`, high);

    let i = low - 1;
    currentStack[0].localVars = `pivot=${pivot}, i=${i}`;
    snapshot('partition', arr, [], 3, 'Initialize Pointers', `Pointer 'i' tracks the boundary of elements smaller than the pivot. It starts at ${i}.`, high, [i]);

    for (let j = low; j < high; j++) {
      currentStack[0].localVars = `pivot=${pivot}, i=${i}, j=${j}`;
      snapshot('compare', arr, [j], 6, 'Checking Element', `Is arr[j] (${arr[j]}) smaller than the pivot (${pivot})?`, high, [i, j]);
      
      if (arr[j] < pivot) {
        i++;
        currentStack[0].localVars = `pivot=${pivot}, i=${i}, j=${j}`;
        snapshot('partition', arr, [j], 7, 'Element is Smaller', `Yes! So we increment 'i' to ${i} to expand our "smaller than pivot" section.`, high, [i, j]);
        
        // Swap
        const temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        
        snapshot('swap', arr, [i, j], 8, 'Swapping Elements', `We swap arr[i] (${arr[i]}) and arr[j] (${arr[j]}) to keep smaller elements on the left.`, high, [i, j]);
      } else {
        snapshot('partition', arr, [j], 5, 'Element is Larger', `No. We do nothing and move 'j' forward.`, high, [i, j]);
      }
    }

    currentStack[0].localVars = `pivot=${pivot}, i=${i}`;
    snapshot('partition', arr, [i + 1, high], 10, 'Placing Pivot', `Partitioning loop finished. We swap the pivot into its final sorted position at index ${i + 1}.`, high, [i + 1]);
    
    // Final swap for pivot
    const temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    snapshot('swap', arr, [i + 1], 11, 'Pivot Placed', `The pivot (${pivot}) is now in its correct sorted position! Everything left is smaller, everything right is larger.`, i + 1, [i + 1]);

    currentStack.shift();
    return i + 1;
  };

  const quickSort = (
    arr: number[], 
    low: number, 
    high: number, 
    nodeId: string, 
    level: number, 
    xOffset: number
  ) => {
    const frameId = `frame-${low}-${high}`;
    
    currentStack.unshift({
      id: frameId,
      functionName: 'quick_sort',
      parameters: `low=${low}, high=${high}`,
      localVars: 'pi=?',
      status: 'Started'
    });

    const nodeIndex = treeNodes.findIndex(n => n.id === nodeId);
    if (nodeIndex !== -1) {
      treeNodes[nodeIndex].data.isActive = true;
    }

    snapshot('divide', arr, Array.from({ length: Math.max(0, high - low + 1) }, (_, i) => low + i), 13, 'Calling quick_sort', `We called quick_sort on bounds [${low}, ${high}].`);

    if (low < high) {
      currentStack[0].status = 'Partitioning';
      snapshot('divide', arr, [], 14, 'Valid Bounds', `low < high, so we proceed to partition this section.`);
      
      const pi = partition(arr, low, high);
      
      currentStack[0].localVars = `pi=${pi}`;
      currentStack[0].status = 'Divided';
      
      // Update current node to show partitioned state
      if (nodeIndex !== -1) {
        treeNodes[nodeIndex].data.label = `[${arr.slice(low, high + 1).join(', ')}]`;
        treeNodes[nodeIndex].data.isActive = false; // We branch out now
      }

      snapshot('divide', arr, [pi], 15, 'Partition Complete', `Partition returned pivot index ${pi}. We now recursively sort the left and right sides of the pivot.`);

      const ySpacing = 100;
      const xSpacing = 200 / (level + 1);
      
      const leftNodeId = `${nodeId}-L`;
      if (pi - 1 >= low) {
        treeNodes.push({
          id: leftNodeId,
          position: { x: xOffset - xSpacing, y: (level + 1) * ySpacing + 50 },
          data: { label: `[${arr.slice(low, pi).join(', ')}]`, isActive: false, isCompleted: false },
        });
        treeEdges.push({ id: `e-${nodeId}-${leftNodeId}`, source: nodeId, target: leftNodeId });
      }

      const rightNodeId = `${nodeId}-R`;
      if (pi + 1 <= high) {
        treeNodes.push({
          id: rightNodeId,
          position: { x: xOffset + xSpacing, y: (level + 1) * ySpacing + 50 },
          data: { label: `[${arr.slice(pi + 1, high + 1).join(', ')}]`, isActive: false, isCompleted: false },
        });
        treeEdges.push({ id: `e-${nodeId}-${rightNodeId}`, source: nodeId, target: rightNodeId });
      }

      // Recurse Left
      if (pi - 1 >= low) {
        currentStack[0].status = 'Waiting for Left';
        snapshot('divide', arr, [], 17, 'Recursing Left', `Calling quick_sort on the left sub-array [${low}, ${pi - 1}].`);
        quickSort(arr, low, pi - 1, leftNodeId, level + 1, xOffset - xSpacing);
      }

      // Recurse Right
      if (pi + 1 <= high) {
        currentStack[0].status = 'Waiting for Right';
        snapshot('divide', arr, [], 18, 'Recursing Right', `Calling quick_sort on the right sub-array [${pi + 1}, ${high}].`);
        quickSort(arr, pi + 1, high, rightNodeId, level + 1, xOffset + xSpacing);
      }

      // Mark this branch complete
      if (nodeIndex !== -1) {
        treeNodes[nodeIndex].data.isCompleted = true;
      }
      
    } else if (low === high) {
      // Base case for single element
      currentStack[0].status = 'Base Case';
      snapshot('base_case', arr, [low], 14, 'Base Case Reached', `Single element at index ${low} is already sorted.`);
      if (nodeIndex !== -1) {
        treeNodes[nodeIndex].data.isActive = false;
        treeNodes[nodeIndex].data.isCompleted = true;
      }
    }

    currentStack[0].status = 'Completed';
    currentStack.shift();
  };

  const workingArray = [...initialArray];
  quickSort(workingArray, 0, workingArray.length - 1, rootId, 0, 400);

  // Final snapshot
  snapshot('completed', workingArray, [], 22, 'Algorithm Finished', `The entire array has been successfully sorted using Quick Sort!`);

  return traces;
}
