export function getSelectionSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  let n = array.length;
  animations.push({ type: 'line', line: 1 });
  for (let i = 0; i < n - 1; i++) {
    animations.push({ type: 'line', line: 2 });
    let min_idx = i;
    animations.push({ type: 'line', line: 3 });
    for (let j = i + 1; j < n; j++) {
      animations.push({ type: 'line', line: 4 });
      animations.push({ type: 'compare', indices: [min_idx, j] });
      animations.push({ type: 'uncompare', indices: [min_idx, j] });
      animations.push({ type: 'line', line: 5 });
      if (array[j] < array[min_idx]) {
        min_idx = j;
        animations.push({ type: 'line', line: 6 });
      }
    }
    animations.push({ type: 'line', line: 8 });
    animations.push({ type: 'swap', indices: [i, min_idx], values: [array[min_idx], array[i]] });
    let temp = array[i];
    array[i] = array[min_idx];
    array[min_idx] = temp;
  }
  animations.push({ type: 'line', line: 9 });

  // Mark all as sorted at the end
  for (let i = 0; i < array.length; i++) {
    animations.push({ type: 'sorted', indices: [i] });
  }
  return animations;
}
