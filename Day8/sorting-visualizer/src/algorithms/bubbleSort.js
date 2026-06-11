export function getBubbleSortAnimations(array) {
  const animations = [];
  if (array.length <= 1) return animations;
  const auxiliaryArray = array.slice();
  bubbleSortHelper(auxiliaryArray, animations);
  return animations;
}

function bubbleSortHelper(mainArray, animations) {
  const n = mainArray.length;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      // compare: highlight
      animations.push({ type: 'compare', indices: [j, j + 1] });
      
      if (mainArray[j] > mainArray[j + 1]) {
        // swap
        animations.push({ type: 'swap', indices: [j, j + 1], values: [mainArray[j + 1], mainArray[j]] });
        let temp = mainArray[j];
        mainArray[j] = mainArray[j + 1];
        mainArray[j + 1] = temp;
      }
      
      // uncompare: unhighlight
      animations.push({ type: 'uncompare', indices: [j, j + 1] });
    }
    // element is at its final position
    animations.push({ type: 'sorted', indices: [n - 1 - i] });
  }
  animations.push({ type: 'sorted', indices: [0] });
}
