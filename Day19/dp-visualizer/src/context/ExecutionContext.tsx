import React, { createContext, useContext, useState, useEffect } from 'react';
import type { ReactNode } from 'react';
import type { DPStep } from '../engine/FibonacciEngine';
import { generateFibonacciSteps, generateFibonacciTabulationSteps } from '../engine/FibonacciEngine';
import { generateLISSteps, LIS_CODE } from '../engine/LISEngine';
import { generateLCSSteps, LCS_CODE } from '../engine/LCSEngine';
import { generateKnapsackSteps, KNAPSACK_CODE } from '../engine/KnapsackEngine';

export type Topic = 'Fibonacci (Memoization)' | 'Fibonacci (Tabulation)' | 'LIS' | 'LCS' | 'Knapsack';

interface ExecutionState {
  currentTopic: Topic;
  setCurrentTopic: (topic: Topic) => void;
  code: string;
  setCode: (code: string) => void;
  isPlaying: boolean;
  setIsPlaying: (isPlaying: boolean) => void;
  speed: number;
  setSpeed: (speed: number) => void;
  currentStep: number;
  setCurrentStep: (step: number) => void;
  totalSteps: number;
  activeLine: number | null;
  stepData: DPStep | null;
  zoomLevel: number;
  setZoomLevel: (zoom: number | ((z: number) => number)) => void;
}

const ExecutionContext = createContext<ExecutionState | undefined>(undefined);

const FIB_MEMO_CODE = `def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(5))`;

const FIB_TAB_CODE = `def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]`;

export const ExecutionProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [currentTopic, setCurrentTopic] = useState<Topic>('Fibonacci (Memoization)');
  const [code, setCode] = useState<string>(FIB_MEMO_CODE);
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [speed, setSpeed] = useState<number>(1);
  const [currentStep, setCurrentStep] = useState<number>(0);
  const [zoomLevel, setZoomLevel] = useState<number>(1);
  
  const [steps, setSteps] = useState<DPStep[]>([]);

  useEffect(() => {
    setIsPlaying(false);
    setCurrentStep(0);
    
    if (currentTopic === 'Fibonacci (Memoization)') {
      setCode(FIB_MEMO_CODE);
      setSteps(generateFibonacciSteps(5));
    } else if (currentTopic === 'Fibonacci (Tabulation)') {
      setCode(FIB_TAB_CODE);
      setSteps(generateFibonacciTabulationSteps(5));
    } else if (currentTopic === 'LIS') {
      setCode(LIS_CODE);
      setSteps(generateLISSteps());
    } else if (currentTopic === 'LCS') {
      setCode(LCS_CODE);
      setSteps(generateLCSSteps());
    } else if (currentTopic === 'Knapsack') {
      setCode(KNAPSACK_CODE);
      setSteps(generateKnapsackSteps());
    }
  }, [currentTopic]);

  const totalSteps = Math.max(0, steps.length - 1);
  const stepData = steps[currentStep] || null;
  const activeLine = stepData?.activeLine || null;

  // Auto-play logic
  useEffect(() => {
    if (!isPlaying) return;
    
    if (currentStep >= totalSteps) {
      setIsPlaying(false);
      return;
    }
    
    const baseDelay = 1000;
    const delay = baseDelay / speed;
    
    const timer = setTimeout(() => {
      setCurrentStep(s => Math.min(s + 1, totalSteps));
    }, delay);
    
    return () => clearTimeout(timer);
  }, [isPlaying, currentStep, totalSteps, speed]);

  // Keyboard navigation logic
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't intercept if user is typing in an input/textarea
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) {
        return;
      }
      
      if (e.key === 'ArrowRight') {
        e.preventDefault();
        setCurrentStep(s => Math.min(s + 1, totalSteps));
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        setCurrentStep(s => Math.max(s - 1, 0));
      } else if (e.key === ' ') {
        e.preventDefault();
        setIsPlaying(p => !p);
      }
    };
    
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [totalSteps]);

  return (
    <ExecutionContext.Provider
      value={{
        currentTopic,
        setCurrentTopic,
        code,
        setCode,
        isPlaying,
        setIsPlaying,
        speed,
        setSpeed,
        currentStep,
        setCurrentStep,
        totalSteps,
        activeLine,
        stepData,
        zoomLevel,
        setZoomLevel,
      }}
    >
      {children}
    </ExecutionContext.Provider>
  );
};

export const useExecution = () => {
  const context = useContext(ExecutionContext);
  if (!context) {
    throw new Error('useExecution must be used within an ExecutionProvider');
  }
  return context;
};

