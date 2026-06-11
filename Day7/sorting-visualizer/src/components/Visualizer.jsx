import React, { useState, useEffect, useRef } from 'react';
import { getBubbleSortAnimations } from '../algorithms/bubbleSort';
import { getSelectionSortAnimations } from '../algorithms/selectionSort';
import { getInsertionSortAnimations } from '../algorithms/insertionSort';

const PRIMARY_COLOR = 'rgba(255, 255, 255, 0.8)';
const SECONDARY_COLOR = '#ff4b4b'; // Red for comparisons
const SORTED_COLOR = '#4caf50'; // Green for sorted

const BUBBLE_SORT_CODE = `def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr`;

const SELECTION_SORT_CODE = `def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap elements
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr`;

const INSERTION_SORT_CODE = `def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Shift elements
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr`;

export default function Visualizer() {
  const [initialArray, setInitialArray] = useState([]);
  const [states, setStates] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  
  const [animationSpeed, setAnimationSpeed] = useState(300);
  const [arraySize, setArraySize] = useState(15);
  const [activeCode, setActiveCode] = useState(BUBBLE_SORT_CODE);
  const containerRef = useRef(null);

  useEffect(() => {
    resetArray();
  }, [arraySize]);

  // Handle Keyboard Events for manual stepping
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (states.length === 0) return;
      
      if (e.key === 'ArrowRight') {
        setIsPlaying(false);
        setCurrentStep(prev => Math.min(prev + 1, states.length - 1));
      } else if (e.key === 'ArrowLeft') {
        setIsPlaying(false);
        setCurrentStep(prev => Math.max(prev - 1, 0));
      } else if (e.key === ' ') {
        e.preventDefault(); // Prevent page scroll on spacebar
        setIsPlaying(prev => {
          if (!prev && currentStep >= states.length - 1) {
             setCurrentStep(0); // Restart if at the end
             return true;
          }
          return !prev;
        });
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [states, currentStep]);

  // Automatic Playback Loop
  useEffect(() => {
    let timerId;
    if (isPlaying && currentStep < states.length - 1) {
      timerId = setTimeout(() => {
        setCurrentStep(prev => prev + 1);
      }, animationSpeed);
    } else if (currentStep >= states.length - 1) {
      setIsPlaying(false);
    }
    return () => clearTimeout(timerId);
  }, [isPlaying, currentStep, states, animationSpeed]);

  const resetArray = () => {
    setIsPlaying(false);
    const newArray = [];
    for (let i = 0; i < arraySize; i++) {
      newArray.push(randomIntFromInterval(50, 450));
    }
    setInitialArray(newArray);
    
    // Set baseline state
    setStates([{
      array: newArray,
      colors: new Array(newArray.length).fill(PRIMARY_COLOR)
    }]);
    setCurrentStep(0);
  };

  const computeStates = (animations) => {
    const computedStates = [];
    let currentArray = [...initialArray];
    let currentColors = new Array(currentArray.length).fill(PRIMARY_COLOR);
    
    computedStates.push({ array: [...currentArray], colors: [...currentColors] });

    for (let anim of animations) {
      let nextArray = [...currentArray];
      let nextColors = [...currentColors];

      if (anim.type === 'compare') {
        if(anim.indices[0] !== undefined) nextColors[anim.indices[0]] = SECONDARY_COLOR;
        if(anim.indices[1] !== undefined) nextColors[anim.indices[1]] = SECONDARY_COLOR;
      } else if (anim.type === 'uncompare') {
        if (anim.indices[0] !== undefined && nextColors[anim.indices[0]] !== SORTED_COLOR) nextColors[anim.indices[0]] = PRIMARY_COLOR;
        if (anim.indices[1] !== undefined && nextColors[anim.indices[1]] !== SORTED_COLOR) nextColors[anim.indices[1]] = PRIMARY_COLOR;
      } else if (anim.type === 'swap') {
        nextArray[anim.indices[0]] = anim.values[0];
        nextArray[anim.indices[1]] = anim.values[1];
        // Distinct color for swapping
        if(anim.indices[0] !== undefined) nextColors[anim.indices[0]] = '#eab308'; // Gold
        if(anim.indices[1] !== undefined) nextColors[anim.indices[1]] = '#eab308'; // Gold
      } else if (anim.type === 'sorted') {
        if(anim.indices[0] !== undefined) nextColors[anim.indices[0]] = SORTED_COLOR;
      }
      
      computedStates.push({ array: nextArray, colors: nextColors });
      currentArray = nextArray;
      currentColors = nextColors;
    }
    
    setStates(computedStates);
    setCurrentStep(0);
    setIsPlaying(true);
  };

  const runAlgorithm = (algorithmFn, codeStr) => {
    setActiveCode(codeStr);
    const animations = algorithmFn(initialArray);
    computeStates(animations);
  };

  const currentState = states[currentStep] || { 
    array: initialArray, 
    colors: new Array(initialArray.length).fill(PRIMARY_COLOR) 
  };

  return (
    <div className="visualizer-container" ref={containerRef}>
      <header className="toolbar">
        <div style={{display: 'flex', flexDirection: 'column'}}>
          <h1 className="title">Sorting Visualizer</h1>
          <span style={{fontSize: '0.75rem', color: '#94a3b8', marginTop: '4px'}}>
            Press <strong>Space</strong> to Play/Pause • <strong>Arrows ⬅️ ➡️</strong> to Step
          </span>
        </div>
        
        <div className="controls">
          <button onClick={resetArray}>Generate New Array</button>
          
          <div className="slider-container">
            <label>Size</label>
            <input 
              type="range" 
              min="5" 
              max="50" 
              value={arraySize}
              onChange={(e) => setArraySize(Number(e.target.value))}
            />
          </div>

          <div className="slider-container">
            <label>Speed (delay ms)</label>
            <input 
              type="range" 
              min="10" 
              max="1000" 
              value={animationSpeed}
              onChange={(e) => setAnimationSpeed(Number(e.target.value))}
            />
          </div>
          
          <button 
            style={{background: isPlaying ? 'rgba(239, 68, 68, 0.2)' : 'rgba(34, 197, 94, 0.2)'}}
            onClick={() => setIsPlaying(!isPlaying)}
          >
            {isPlaying ? '⏸ Pause' : '▶️ Play'}
          </button>

          <div className="algorithms">
            <button onClick={() => runAlgorithm(getBubbleSortAnimations, BUBBLE_SORT_CODE)}>Bubble Sort</button>
            <button onClick={() => runAlgorithm(getSelectionSortAnimations, SELECTION_SORT_CODE)}>Selection Sort</button>
            <button onClick={() => runAlgorithm(getInsertionSortAnimations, INSERTION_SORT_CODE)}>Insertion Sort</button>
          </div>
        </div>
      </header>

      <div className="main-content">
        <div className="array-container">
          {currentState.array.map((value, idx) => (
            <div
              className="array-bar"
              key={idx}
              style={{
                height: `${value}px`,
                backgroundColor: currentState.colors[idx],
              }}
            >
              <span className="bar-value">{value}</span>
            </div>
          ))}
        </div>
        
        <div className="code-container">
          <h3 className="code-title">Algorithm Logic</h3>
          <pre><code className="code-block">{activeCode}</code></pre>
        </div>
      </div>
    </div>
  );
}

function randomIntFromInterval(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
