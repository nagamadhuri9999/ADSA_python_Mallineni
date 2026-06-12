import type { Edge, Node } from '@xyflow/react';
import type { CallStackFrame, TraceStep } from './useStore';

let stepIdCounter = 0;

export function generateMergeSortTraces(initialArray: number[]): TraceStep[] {
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

  // Deep copy helper to snapshot state
  const snapshot = (
    type: TraceStep['type'],
    array: number[],
    activeIndices: number[],
    activeLine: number,
    explanationTitle: string,
    explanationText: string
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
      explanationText
    });
  };

  const mergeSort = (
    arr: number[], 
    startIndex: number, 
    endIndex: number, 
    nodeId: string, 
    level: number, 
    xOffset: number
  ) => {
    const frameId = `frame-${startIndex}-${endIndex}`;
    
    // Push to stack
    currentStack.unshift({
      id: frameId,
      functionName: 'mergeSort',
      parameters: `nums=[${arr.slice(startIndex, endIndex).join(', ')}]`,
      localVars: 'mid=?',
      status: 'Started'
    });
    
    // Update Node to Active
    const nodeIndex = treeNodes.findIndex(n => n.id === nodeId);
    if (nodeIndex !== -1) {
      treeNodes[nodeIndex].data.isActive = true;
    }

    // Trace: Function start
    snapshot('divide', arr, Array.from({ length: endIndex - startIndex }, (_, i) => startIndex + i), 20, 'Calling mergeSort', `We have called merge_sort on the sub-array [${arr.slice(startIndex, endIndex).join(', ')}].`);

    // Base Case Check
    if (endIndex - startIndex <= 1) {
      currentStack[0].status = 'Base Case Reached';
      snapshot('base_case', arr, [startIndex], 22, 'Base Case Reached', `The array length is 1. A single element is naturally sorted. We return it.`);
      
      // Complete Node
      if (nodeIndex !== -1) {
        treeNodes[nodeIndex].data.isActive = false;
        treeNodes[nodeIndex].data.isCompleted = true;
      }
      
      // Pop Stack
      currentStack.shift();
      return;
    }

    const mid = Math.floor((startIndex + endIndex) / 2);
    currentStack[0].localVars = `mid=${mid - startIndex}`;
    currentStack[0].status = 'Dividing';

    snapshot('divide', arr, Array.from({ length: endIndex - startIndex }, (_, i) => startIndex + i), 24, 'Calculating Midpoint', `We split the array at index ${mid - startIndex}.`);

    // Create Left and Right Nodes
    const leftNodeId = `${nodeId}-L`;
    const rightNodeId = `${nodeId}-R`;
    const ySpacing = 100;
    const xSpacing = 200 / (level + 1);

    treeNodes.push({
      id: leftNodeId,
      position: { x: treeNodes[nodeIndex].position.x - xSpacing, y: treeNodes[nodeIndex].position.y + ySpacing },
      data: { label: `[${arr.slice(startIndex, mid).join(', ')}]`, isActive: false, isCompleted: false },
    });
    treeEdges.push({ id: `e-${nodeId}-${leftNodeId}`, source: nodeId, target: leftNodeId });

    treeNodes.push({
      id: rightNodeId,
      position: { x: treeNodes[nodeIndex].position.x + xSpacing, y: treeNodes[nodeIndex].position.y + ySpacing },
      data: { label: `[${arr.slice(mid, endIndex).join(', ')}]`, isActive: false, isCompleted: false },
    });
    treeEdges.push({ id: `e-${nodeId}-${rightNodeId}`, source: nodeId, target: rightNodeId });

    // Recurse Left
    currentStack[0].status = 'Waiting for Left';
    snapshot('divide', arr, [], 26, 'Recursing Left', `We recursively call merge_sort on the left half.`);
    mergeSort(arr, startIndex, mid, leftNodeId, level + 1, xOffset - xSpacing);

    // Recurse Right
    currentStack[0].status = 'Waiting for Right';
    snapshot('divide', arr, [], 27, 'Recursing Right', `Left half is fully sorted. Now we recursively call merge_sort on the right half.`);
    mergeSort(arr, mid, endIndex, rightNodeId, level + 1, xOffset + xSpacing);

    // Merge
    currentStack[0].status = 'Merging';
    snapshot('merge', arr, [], 29, 'Merging Halves', `Both halves are sorted. Now we merge them back together in order.`);
    
    // Perform actual merge in place for the trace (visuals still need in-place to render easily)
    const leftArray = arr.slice(startIndex, mid);
    const rightArray = arr.slice(mid, endIndex);
    let i = 0, j = 0, k = startIndex;

    while (i < leftArray.length && j < rightArray.length) {
      snapshot('compare', arr, [startIndex + i, mid + j], 8, 'Comparing Elements', `Comparing ${leftArray[i]} and ${rightArray[j]}.`);
      
      if (leftArray[i] <= rightArray[j]) {
        arr[k] = leftArray[i];
        i++;
        k++;
        snapshot('swap', arr, [k - 1], 9, 'Element Appended', `Left element is smaller, appending to result array.`);
      } else {
        arr[k] = rightArray[j];
        j++;
        k++;
        snapshot('swap', arr, [k - 1], 12, 'Element Appended', `Right element is smaller, appending to result array.`);
      }
    }

    while (i < leftArray.length) {
      snapshot('compare', arr, [startIndex + i], 15, 'Copying Remaining Left', `Left array has remaining elements, extending result.`);
      arr[k] = leftArray[i];
      i++;
      k++;
      snapshot('swap', arr, [k - 1], 15, 'Element Appended', `Copied remaining left element.`);
    }

    while (j < rightArray.length) {
      snapshot('compare', arr, [mid + j], 16, 'Copying Remaining Right', `Right array has remaining elements, extending result.`);
      arr[k] = rightArray[j];
      j++;
      k++;
      snapshot('swap', arr, [k - 1], 16, 'Element Appended', `Copied remaining right element.`);
    }

    // Complete Node
    const finalNodeIndex = treeNodes.findIndex(n => n.id === nodeId);
    if (finalNodeIndex !== -1) {
      treeNodes[finalNodeIndex].data.isActive = false;
      treeNodes[finalNodeIndex].data.isCompleted = true;
      treeNodes[finalNodeIndex].data.label = `[${arr.slice(startIndex, endIndex).join(', ')}]`;
    }

    currentStack[0].status = 'Completed';
    snapshot('completed', arr, Array.from({ length: endIndex - startIndex }, (_, x) => startIndex + x), 18, 'Merge Complete', `The merged array is returned!`);
    
    // Pop Stack
    currentStack.shift();
  };

  const workingArray = [...initialArray];
  mergeSort(workingArray, 0, workingArray.length, rootId, 0, 400);

  // Final snapshot
  snapshot('completed', workingArray, [], 22, 'Algorithm Finished', `The entire array has been successfully sorted using Merge Sort!`);

  return traces;
}
