export function getBubbleSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  let n = array.length;
  animations.push({ type: 'line', line: 1 });
  for (let i = 0; i < n - 1; i++) {
    animations.push({ type: 'line', line: 2 });
    let swapped = false;
    animations.push({ type: 'line', line: 3 });
    for (let j = 0; j < n - i - 1; j++) {
      animations.push({ type: 'line', line: 4 });
      animations.push({ type: 'line', line: 5 });
      animations.push({ type: 'compare', indices: [j, j + 1] });
      animations.push({ type: 'uncompare', indices: [j, j + 1] });
      if (array[j] > array[j + 1]) {
        animations.push({ type: 'line', line: 7 });
        animations.push({ type: 'swap', indices: [j, j + 1], values: [array[j + 1], array[j]] });
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        swapped = true;
        animations.push({ type: 'line', line: 8 });
      }
    }
    animations.push({ type: 'line', line: 9 });
    if (!swapped) {
      animations.push({ type: 'line', line: 10 });
      break;
    }
  }
  animations.push({ type: 'line', line: 11 });
  
  // Mark all as sorted at the end
  for (let i = 0; i < array.length; i++) {
    animations.push({ type: 'sorted', indices: [i] });
  }
  return animations;
}
