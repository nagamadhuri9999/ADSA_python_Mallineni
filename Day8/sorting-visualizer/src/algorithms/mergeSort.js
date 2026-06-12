export function getMergeSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) {
      animations.push({ type: 'line', line: 1 });
      return animations;
  }
  const auxiliaryArray = array.slice();
  animations.push({ type: 'line', line: 0 });
  animations.push({ type: 'line', line: 1 });
  mergeSortHelper(array, 0, array.length - 1, auxiliaryArray, animations);
  
  animations.push({ type: 'line', line: 24 });
  // Mark all as sorted at the end
  for (let i = 0; i < array.length; i++) {
    animations.push({ type: 'sorted', indices: [i] });
  }
  
  return animations;
}

function mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray, animations) {
  if (startIdx === endIdx) return;
  const middleIdx = Math.floor((startIdx + endIdx) / 2);
  animations.push({ type: 'line', line: 2 });
  animations.push({ type: 'line', line: 3 });
  animations.push({ type: 'line', line: 4 });
  
  animations.push({ type: 'line', line: 5 });
  mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray, animations);
  
  animations.push({ type: 'line', line: 6 });
  mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray, animations);
  
  doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray, animations);
}

function doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray, animations) {
  let k = startIdx;
  let i = startIdx;
  let j = middleIdx + 1;
  animations.push({ type: 'line', line: 7 });
  
  animations.push({ type: 'line', line: 8 });
  while (i <= middleIdx && j <= endIdx) {
    animations.push({ type: 'compare', indices: [i, j] });
    animations.push({ type: 'uncompare', indices: [i, j] });
    animations.push({ type: 'line', line: 9 });
    if (auxiliaryArray[i] <= auxiliaryArray[j]) {
      animations.push({ type: 'line', line: 10 });
      animations.push({ type: 'swap', indices: [k, k], values: [auxiliaryArray[i], auxiliaryArray[i]] });
      mainArray[k] = auxiliaryArray[i];
      
      animations.push({ type: 'line', line: 11 });
      i++;
    } else {
      animations.push({ type: 'line', line: 13 });
      animations.push({ type: 'swap', indices: [k, k], values: [auxiliaryArray[j], auxiliaryArray[j]] });
      mainArray[k] = auxiliaryArray[j];
      
      animations.push({ type: 'line', line: 14 });
      j++;
    }
    animations.push({ type: 'line', line: 15 });
    k++;
    animations.push({ type: 'line', line: 8 });
  }
  
  animations.push({ type: 'line', line: 16 });
  while (i <= middleIdx) {
    animations.push({ type: 'compare', indices: [i, i] });
    animations.push({ type: 'uncompare', indices: [i, i] });
    
    animations.push({ type: 'line', line: 17 });
    animations.push({ type: 'swap', indices: [k, k], values: [auxiliaryArray[i], auxiliaryArray[i]] });
    mainArray[k] = auxiliaryArray[i];
    
    animations.push({ type: 'line', line: 18 });
    i++;
    animations.push({ type: 'line', line: 19 });
    k++;
    animations.push({ type: 'line', line: 16 });
  }
  
  animations.push({ type: 'line', line: 20 });
  while (j <= endIdx) {
    animations.push({ type: 'compare', indices: [j, j] });
    animations.push({ type: 'uncompare', indices: [j, j] });
    
    animations.push({ type: 'line', line: 21 });
    animations.push({ type: 'swap', indices: [k, k], values: [auxiliaryArray[j], auxiliaryArray[j]] });
    mainArray[k] = auxiliaryArray[j];
    
    animations.push({ type: 'line', line: 22 });
    j++;
    animations.push({ type: 'line', line: 23 });
    k++;
    animations.push({ type: 'line', line: 20 });
  }
}
