import type { DPStep } from './FibonacciEngine';

export const LIS_CODE = `def lengthOfLIS(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)`;

export function generateLISSteps(nums: number[] = [10, 9, 2, 5, 3, 7, 101, 18]): DPStep[] {
  const steps: DPStep[] = [];
  const n = nums.length;
  const dp: (number | null)[] = Array(n).fill(null);
  
  const cloneState = (): DPStep => ({
    activeLine: 1,
    variables: {},
    explanation: { title: '', text: [] },
    visualType: 'array1d',
    array1d: {
      name: 'dp',
      data: [...dp],
      activeIndices: [],
      compareIndices: [],
      updatedIndices: [],
      labels: nums.map(String)
    }
  });

  const addStep = (
    activeLine: number, 
    variables: Record<string, string | number | null>, 
    title: string, 
    text: string[], 
    arrayState: { active?: number[], compare?: number[], updated?: number[] } = {}
  ) => {
    const step = cloneState();
    step.activeLine = activeLine;
    step.variables = variables;
    step.explanation = { title, text };
    if (step.array1d) {
      step.array1d.activeIndices = arrayState.active || [];
      step.array1d.compareIndices = arrayState.compare || [];
      step.array1d.updatedIndices = arrayState.updated || [];
    }
    steps.push(step);
  };

  addStep(1, { nums: `[${nums.join(', ')}]` }, `Initialize LIS`, [`We want to find the length of the longest increasing subsequence.`, `We initialize a DP array.`]);

  if (n === 0) {
    addStep(2, { nums: '[]' }, `Base Case`, [`The array is empty, return 0.`]);
    return steps;
  }

  for (let i = 0; i < n; i++) dp[i] = 1;
  
  addStep(3, { 'len(nums)': n }, `Initialize DP Array`, [`We create an array 'dp' of size ${n}, initialized with 1s.`, `Every element is an increasing subsequence of length 1 by itself.`]);

  for (let i = 1; i < n; i++) {
    addStep(4, { i, 'nums[i]': nums[i] }, `Outer Loop i=${i}`, [`We iterate i from 1 to ${n - 1}. Current element nums[${i}] = ${nums[i]}.`], { active: [i] });
    
    for (let j = 0; j < i; j++) {
      addStep(5, { i, j, 'nums[i]': nums[i], 'nums[j]': nums[j] }, `Inner Loop j=${j}`, [`Compare nums[${i}] (${nums[i]}) with nums[${j}] (${nums[j]}).`], { active: [i], compare: [j] });
      
      addStep(6, { i, j, 'nums[i]': nums[i], 'nums[j]': nums[j] }, `Check Condition`, [`Is nums[${i}] > nums[${j}]? (${nums[i]} > ${nums[j]})`], { active: [i], compare: [j] });
      
      if (nums[i] > nums[j]) {
        addStep(7, { i, j, 'dp[i]': dp[i], 'dp[j]': dp[j] }, `Update dp[${i}]`, [`Since ${nums[i]} > ${nums[j]}, we can extend the subsequence ending at j.`, `dp[${i}] = max(dp[${i}], dp[${j}] + 1) = max(${dp[i]}, ${dp[j]} + 1)`], { active: [i], compare: [j] });
        
        dp[i] = Math.max(dp[i] as number, (dp[j] as number) + 1);
        
        addStep(7, { i, j, 'dp[i]': dp[i] }, `dp[${i}] Updated`, [`dp[${i}] is now ${dp[i]}.`], { active: [i], updated: [i], compare: [j] });
      } else {
        addStep(6, { i, j }, `Condition False`, [`${nums[i]} is not greater than ${nums[j]}, so we cannot extend the subsequence.`], { active: [i], compare: [j] });
      }
    }
  }

  const result = Math.max(...(dp as number[]));
  addStep(8, { result }, `Return Maximum`, [`The loop has finished. The length of the longest increasing subsequence is the maximum value in the dp array: ${result}.`]);

  return steps;
}
