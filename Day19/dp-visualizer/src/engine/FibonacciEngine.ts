export interface DPStep {
  activeLine: number;
  variables: Record<string, string | number | null>;
  memo?: Record<number, number | string>;
  callStack?: { id: string; func: string; line: number }[];
  explanation: {
    title: string;
    text: React.ReactNode[];
    insight?: string;
  };
  visualType: 'tree' | 'array1d' | 'array2d';
  tree?: {
    nodes: Record<string, { id: string; val: number; status: 'active' | 'done' | 'cache-hit' | 'pending'; parentId: string | null }>;
    edges: { source: string; target: string }[];
  };
  array1d?: {
    name: string;
    data: (number | string | null)[];
    activeIndices?: number[];
    compareIndices?: number[];
    updatedIndices?: number[];
    labels?: string[];
  };
  array2d?: {
    name: string;
    data: (number | string | null)[][];
    rowLabels?: string[];
    colLabels?: string[];
    activeCell?: [number, number];
    compareCells?: [number, number][];
    updatedCells?: [number, number][];
  };
}

export function generateFibonacciSteps(n: number): DPStep[] {
  const steps: DPStep[] = [];
  let nextNodeId = 0;
  
  const memo: Record<number, number> = {};
  const callStack: { id: string; func: string; line: number; val: number }[] = [];
  
  const nodes: Record<string, { id: string; val: number; status: 'active' | 'done' | 'cache-hit' | 'pending'; parentId: string | null }> = {};
  const edges: { source: string; target: string }[] = [];

  const cloneState = (): DPStep => ({
    activeLine: 1,
    variables: {},
    memo: { ...memo },
    callStack: callStack.map(s => ({ id: s.id, func: s.func, line: s.line })),
    explanation: { title: '', text: [] },
    visualType: 'tree',
    tree: {
      nodes: JSON.parse(JSON.stringify(nodes)),
      edges: JSON.parse(JSON.stringify(edges))
    }
  });

  const addStep = (
    activeLine: number, 
    variables: Record<string, string | number | null>, 
    title: string, 
    text: string[], 
    insight?: string
  ) => {
    const step = cloneState();
    step.activeLine = activeLine;
    step.variables = variables;
    step.explanation = { title, text, insight };
    steps.push(step);
  };

  function fib(num: number, parentId: string | null): number {
    const id = `node-${nextNodeId++}`;
    nodes[id] = { id, val: num, status: 'active', parentId };
    if (parentId) edges.push({ source: parentId, target: id });
    
    callStack.push({ id, func: `fib(${num})`, line: 7, val: num });
    
    addStep(1, { n: num }, `Calling fib(${num})`, [`Starting evaluation of fib(${num}).`, `First, check if ${num} is in the memo dictionary.`]);

    if (num in memo) {
      nodes[id].status = 'cache-hit';
      addStep(2, { n: num }, `Cache Hit!`, [`${num} is found in memo! Returning ${memo[num]} instantly.`], `This is where DP shines! Instead of recalculating, we return the cached value in O(1) time.`);
      callStack.pop();
      return memo[num];
    }

    addStep(4, { n: num }, `Checking Base Case`, [`Is ${num} <= 1?`]);

    if (num <= 1) {
      addStep(5, { n: num }, `Base Case Reached`, [`${num} is a base case. Returning ${num}.`]);
      nodes[id].status = 'done';
      callStack.pop();
      return num;
    }

    addStep(7, { n: num }, `Recursive Case`, [`We need to calculate fib(${num-1}) and fib(${num-2}).`, `We start by expanding the left subtree: fib(${num-1}).`]);

    // Update callstack line to show we are paused waiting for left child
    callStack[callStack.length - 1].line = 7;
    
    const left = fib(num - 1, id);

    addStep(7, { n: num, left }, `Returned from left subtree`, [`fib(${num-1}) evaluated to ${left}.`, `Now we will evaluate the right subtree: fib(${num-2}).`]);
    
    const right = fib(num - 2, id);

    addStep(7, { n: num, left, right }, `Calculating Result`, [`fib(${num-1}) = ${left}, fib(${num-2}) = ${right}.`, `Result is ${left} + ${right} = ${left + right}.`]);
    
    const res = left + right;
    
    addStep(8, { n: num, res }, `Updating Memo`, [`We save memo[${num}] = ${res} so we don't recalculate it later.`]);
    memo[num] = res;
    
    nodes[id].status = 'done';
    
    addStep(9, { n: num, res }, `Returning Result`, [`Returning ${res}.`]);
    
    callStack.pop();
    return res;
  }

  fib(n, null);
  
  // Final step
  addStep(8, { n }, `Return fib(${n})`, [`The final result is ${memo[n]}.`, `The top-down recursion is complete.`]);
  
  return steps;
}

export function generateFibonacciTabulationSteps(n: number): DPStep[] {
  const steps: DPStep[] = [];
  const dp: (number | null)[] = Array(n + 1).fill(null);
  
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
      labels: Array.from({ length: n + 1 }, (_, i) => String(i))
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

  addStep(1, { n }, `Initialize Tabulation`, [`We want to compute fib(${n}) using a bottom-up approach.`, `We start by creating an array of size ${n + 1}.`]);
  
  addStep(2, { n }, `Base Case: n <= 1`, [`First, we handle base cases. If n <= 1, return n.`]);
  if (n <= 1) {
    addStep(3, { n }, `Return Base Case`, [`n is ${n}, which is <= 1, so we return ${n}.`]);
    return steps;
  }

  dp[0] = 0;
  dp[1] = 0; // Will be set to 1 in next step for visualization
  addStep(4, { n, 'dp[0]': dp[0] }, `Initialize DP Array`, [`We create an array 'dp' of size ${n + 1} initialized with 0s.`]);

  dp[1] = 1;
  addStep(5, { n, 'dp[1]': dp[1] }, `Base Cases in DP`, [`We set dp[1] = 1. The base cases dp[0]=0 and dp[1]=1 are now ready.`], { active: [1], updated: [1] });

  for (let i = 2; i <= n; i++) {
    addStep(6, { n, i }, `Loop iteration i=${i}`, [`We iterate from 2 to ${n}. Current i=${i}.`, `We will calculate dp[${i}] using dp[${i-1}] and dp[${i-2}].`], { compare: [i-1, i-2] });
    
    dp[i] = (dp[i-1] as number) + (dp[i-2] as number);
    
    addStep(7, { n, i, 'dp[i]': dp[i] }, `Calculate dp[${i}]`, [`dp[${i}] = dp[${i-1}] + dp[${i-2}]`, `dp[${i}] = ${dp[i-1]} + ${dp[i-2]} = ${dp[i]}`], { active: [i], updated: [i], compare: [i-1, i-2] });
  }

  addStep(8, { n }, `Return dp[${n}]`, [`The loop has finished. We return dp[${n}] which is ${dp[n]}.`, `This is the final answer!`], { active: [n] });

  return steps;
}
