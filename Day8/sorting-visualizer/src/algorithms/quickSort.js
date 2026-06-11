export function getQuickSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  quickSortHelper(array, 0, array.length - 1, animations);
  
  // Mark all as sorted at the end
  for (let i = 0; i < array.length; i++) {
    animations.push({ type: 'sorted', indices: [i] });
  }
  
  return animations;
}

function quickSortHelper(mainArray, startIdx, endIdx, animations) {
  if (startIdx < endIdx) {
    const pivotIdx = partition(mainArray, startIdx, endIdx, animations);
    // Pivot is now in its sorted position
    animations.push({ type: 'sorted', indices: [pivotIdx] });
    
    quickSortHelper(mainArray, startIdx, pivotIdx - 1, animations);
    quickSortHelper(mainArray, pivotIdx + 1, endIdx, animations);
  } else if (startIdx === endIdx) {
      animations.push({ type: 'sorted', indices: [startIdx] });
  }
}

function partition(mainArray, startIdx, endIdx, animations) {
  const pivotValue = mainArray[endIdx];
  let pivotIdx = startIdx;
  for (let i = startIdx; i < endIdx; i++) {
    animations.push({ type: 'compare', indices: [i, endIdx] });
    animations.push({ type: 'uncompare', indices: [i, endIdx] });
    if (mainArray[i] < pivotValue) {
      if (i !== pivotIdx) {
          animations.push({ type: 'swap', indices: [i, pivotIdx], values: [mainArray[pivotIdx], mainArray[i]] });
      }
      let temp = mainArray[i];
      mainArray[i] = mainArray[pivotIdx];
      mainArray[pivotIdx] = temp;
      pivotIdx++;
    }
  }
  if (pivotIdx !== endIdx) {
      animations.push({ type: 'swap', indices: [pivotIdx, endIdx], values: [mainArray[endIdx], mainArray[pivotIdx]] });
  }
  let temp = mainArray[pivotIdx];
  mainArray[pivotIdx] = mainArray[endIdx];
  mainArray[endIdx] = temp;
  return pivotIdx;
}
