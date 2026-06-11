export function getSelectionSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  const mainArray = array.slice();
  const n = mainArray.length;
  for (let i = 0; i < n - 1; i++) {
    let minIdx = i;
    animations.push({ type: 'compare', indices: [minIdx, minIdx] });
    for (let j = i + 1; j < n; j++) {
      animations.push({ type: 'compare', indices: [minIdx, j] });
      animations.push({ type: 'uncompare', indices: [minIdx, j] });
      if (mainArray[j] < mainArray[minIdx]) {
        minIdx = j;
      }
    }
    animations.push({ type: 'swap', indices: [i, minIdx], values: [mainArray[minIdx], mainArray[i]] });
    let temp = mainArray[i];
    mainArray[i] = mainArray[minIdx];
    mainArray[minIdx] = temp;
    animations.push({ type: 'sorted', indices: [i] });
  }
  animations.push({ type: 'sorted', indices: [n - 1] });
  return animations;
}
