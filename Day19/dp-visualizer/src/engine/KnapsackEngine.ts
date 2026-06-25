import type { DPStep } from './FibonacciEngine';

export const KNAPSACK_CODE = `def knapSack(W, wt, val, n):
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][W]`;

export function generateKnapsackSteps(W: number = 5, wt: number[] = [1, 2, 3], val: number[] = [10, 15, 40], n: number = 3): DPStep[] {
  const steps: DPStep[] = [];
  
  // Initialize DP array
  const dp: number[][] = Array(n + 1).fill(0).map(() => Array(W + 1).fill(0));
  
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
      rowLabels: ['Item 0', ...val.map((v, i) => `Item ${i+1} (w:${wt[i]}, v:${v})`)],
      colLabels: Array.from({ length: W + 1 }, (_, i) => `Cap ${i}`)
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

  addStep(1, { W, n, 'wt': `[${wt.join(', ')}]`, 'val': `[${val.join(', ')}]` }, `Initialize 0/1 Knapsack`, [`We want to maximize value without exceeding capacity ${W}.`]);

  addStep(2, { W, n }, `Initialize DP Matrix`, [`Create a matrix of size ${n + 1} x ${W + 1} initialized with 0s.`, `Rows represent items we can pick from. Columns represent current capacity.`]);

  for (let i = 1; i <= n; i++) {
    for (let w = 1; w <= W; w++) {
      addStep(4, { i, w, 'wt[i-1]': wt[i-1], 'val[i-1]': val[i-1] }, `Loop Iteration`, [`Checking item ${i} (weight: ${wt[i-1]}, value: ${val[i-1]}) at capacity ${w}.`], { active: [i, w] });

      addStep(6, { i, w, 'wt[i-1]': wt[i-1] }, `Check Capacity`, [`Can the current item fit in the knapsack?`, `Is wt[${i-1}] <= w? (${wt[i-1]} <= ${w})`], { active: [i, w] });

      if (wt[i - 1] <= w) {
        addStep(7, { i, w, 'wt[i-1]': wt[i-1] }, `Item Fits`, [`The item fits. We can choose to take it or leave it.`, `Leave it: dp[${i-1}][${w}] = ${dp[i-1][w]}`, `Take it: val[${i-1}] + dp[${i-1}][${w} - ${wt[i-1]}] = ${val[i-1]} + ${dp[i-1][w-wt[i-1]]}`], { active: [i, w], compare: [[i-1, w], [i-1, w - wt[i-1]]] });
        
        dp[i][w] = Math.max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
        
        addStep(7, { i, w, 'dp[i][w]': dp[i][w] }, `Update Cell (Max)`, [`dp[${i}][${w}] = max(${val[i-1]} + ${dp[i-1][w-wt[i-1]]}, ${dp[i-1][w]}) = ${dp[i][w]}`], { active: [i, w], updated: [[i, w]], compare: [[i-1, w], [i-1, w - wt[i-1]]] });
      } else {
        addStep(9, { i, w, 'wt[i-1]': wt[i-1] }, `Item Too Heavy`, [`The item is too heavy (${wt[i-1]} > ${w}). We must leave it.`, `We carry over the value from the previous row: dp[${i-1}][${w}]`], { active: [i, w], compare: [[i-1, w]] });
        
        dp[i][w] = dp[i - 1][w];
        
        addStep(9, { i, w, 'dp[i][w]': dp[i][w] }, `Update Cell (Carry Over)`, [`dp[${i}][${w}] = ${dp[i - 1][w]}`], { active: [i, w], updated: [[i, w]], compare: [[i-1, w]] });
      }
    }
  }

  addStep(11, { result: dp[n][W] }, `Return Final Result`, [`The loop has finished.`, `The maximum value achievable is in the bottom-right cell: ${dp[n][W]}.`], { active: [n, W] });

  return steps;
}
