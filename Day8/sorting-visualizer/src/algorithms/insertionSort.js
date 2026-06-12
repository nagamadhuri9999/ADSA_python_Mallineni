export function getInsertionSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  let n = array.length;
  animations.push({ type: 'line', line: 1 });
  for (let i = 1; i < n; i++) {
    animations.push({ type: 'line', line: 2 });
    let key = array[i];
    animations.push({ type: 'line', line: 3 });
    let j = i - 1;
    animations.push({ type: 'line', line: 4 });
    
    animations.push({ type: 'line', line: 6 });
    while (j >= 0 && array[j] > key) {
      animations.push({ type: 'compare', indices: [j, i] });
      animations.push({ type: 'uncompare', indices: [j, i] });
      
      animations.push({ type: 'line', line: 7 });
      animations.push({ type: 'swap', indices: [j + 1, j + 1], values: [array[j], array[j]] });
      array[j + 1] = array[j];
      j -= 1;
      animations.push({ type: 'line', line: 8 });
      animations.push({ type: 'line', line: 6 });
    }
    animations.push({ type: 'line', line: 9 });
    animations.push({ type: 'swap', indices: [j + 1, j + 1], values: [key, key] });
    array[j + 1] = key;
  }
  animations.push({ type: 'line', line: 10 });

  // Mark all as sorted at the end
  for (let i = 0; i < array.length; i++) {
    animations.push({ type: 'sorted', indices: [i] });
  }
  return animations;
}
