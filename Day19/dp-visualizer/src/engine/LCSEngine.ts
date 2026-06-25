import type { DPStep } from './FibonacciEngine';

export const LCS_CODE = `def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]`;

export function generateLCSSteps(text1: string = "abcde", text2: string = "ace"): DPStep[] {
  const steps: DPStep[] = [];
  const m = text1.length;
  const n = text2.length;
  
  // Initialize DP array
  const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
  
  const cloneState = (): DPStep => ({
    activeLine: 1,
    variables: {},
    explanation: { title: '', text: [] },
    visualType: 'array2d',
    array2d: {
      name: 'dp',
      data: dp.map(row => [...row]),
      activeCell: undefined,
      compareCells: [],
      updatedCells: [],
      rowLabels: ['""', ...text1.split('')],
      colLabels: ['""', ...text2.split('')]
    }
  });

  const addStep = (
    activeLine: number, 
    variables: Record<string, string | number | null>, 
    title: string, 
    text: string[], 
    arrayState: { active?: [number, number], compare?: [number, number][], updated?: [number, number][] } = {}
  ) => {
    const step = cloneState();
    step.activeLine = activeLine;
    step.variables = variables;
    step.explanation = { title, text };
    if (step.array2d) {
      step.array2d.activeCell = arrayState.active;
      step.array2d.compareCells = arrayState.compare || [];
      step.array2d.updatedCells = arrayState.updated || [];
    }
    steps.push(step);
  };

  addStep(1, { text1: `"${text1}"`, text2: `"${text2}"` }, `Initialize LCS`, [`We want to find the length of the longest common subsequence between "${text1}" and "${text2}".`]);

  addStep(2, { m, n }, `Length variables`, [`m = ${m}, n = ${n}`]);

  addStep(3, { m, n }, `Initialize DP Matrix`, [`Create a matrix of size ${m + 1} x ${n + 1} initialized with 0s.`, `The extra row and column handle base cases (empty strings).`]);

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      addStep(4, { i, j }, `Loop Iteration`, [`Comparing text1[${i-1}] ('${text1[i-1]}') with text2[${j-1}] ('${text2[j-1]}').`], { active: [i, j] });

      addStep(7, { i, j, 'text1[i-1]': text1[i-1], 'text2[j-1]': text2[j-1] }, `Check Equality`, [`Is '${text1[i-1]}' == '${text2[j-1]}'?`], { active: [i, j] });

      if (text1[i - 1] === text2[j - 1]) {
        addStep(8, { i, j }, `Characters Match`, [`Since characters match, we add 1 to the result of the sequences without these characters (diagonal).`, `dp[${i}][${j}] = 1 + dp[${i-1}][${j-1}]`], { active: [i, j], compare: [[i-1, j-1]] });
        
        dp[i][j] = 1 + dp[i - 1][j - 1];
        
        addStep(8, { i, j, 'dp[i][j]': dp[i][j] }, `Update Cell`, [`dp[${i}][${j}] = ${dp[i][j]}`], { active: [i, j], updated: [[i, j]], compare: [[i-1, j-1]] });
      } else {
        addStep(10, { i, j }, `Characters Differ`, [`Since characters don't match, we take the max of excluding one character or the other (top or left).`, `dp[${i}][${j}] = max(dp[${i-1}][${j}], dp[${i}][${j-1}])`], { active: [i, j], compare: [[i-1, j], [i, j-1]] });
        
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        
        addStep(10, { i, j, 'dp[i][j]': dp[i][j] }, `Update Cell`, [`dp[${i}][${j}] = max(${dp[i - 1][j]}, ${dp[i][j - 1]}) = ${dp[i][j]}`], { active: [i, j], updated: [[i, j]], compare: [[i-1, j], [i, j-1]] });
      }
    }
  }

  addStep(12, { result: dp[m][n] }, `Return Final Result`, [`The loop has finished.`, `The longest common subsequence length is in the bottom-right cell: ${dp[m][n]}.`], { active: [m, n] });

  return steps;
}
