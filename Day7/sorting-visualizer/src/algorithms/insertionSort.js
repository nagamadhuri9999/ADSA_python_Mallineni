export function getInsertionSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  const mainArray = array.slice();
  const n = mainArray.length;
  animations.push({ type: 'sorted', indices: [0] });
  for (let i = 1; i < n; i++) {
    let key = mainArray[i];
    let j = i - 1;
    animations.push({ type: 'compare', indices: [i, j] });
    while (j >= 0 && mainArray[j] > key) {
      animations.push({ type: 'compare', indices: [j + 1, j] });
      animations.push({ type: 'swap', indices: [j + 1, j], values: [mainArray[j], mainArray[j+1]] });
      animations.push({ type: 'uncompare', indices: [j + 1, j] });
      
      mainArray[j + 1] = mainArray[j];
      j = j - 1;
    }
    mainArray[j + 1] = key;
    for(let k=0; k<=i; k++) {
        animations.push({ type: 'sorted', indices: [k] });
    }
  }
  return animations;
}
