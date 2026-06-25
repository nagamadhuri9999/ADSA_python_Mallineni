# Dynamic Programming Visualizer

A premium, interactive platform for visualizing Dynamic Programming algorithms. This application features an execution engine that steps through DP algorithms, mapping code execution directly to visual data structures (Recursive Trees, 1D Arrays, 2D Matrices).

**Live Demo:** [https://dp-visualizer-seven.vercel.app](https://dp-visualizer-seven.vercel.app)

## Features
- **Supported Algorithms:** Fibonacci (Memoization), Fibonacci (Tabulation), Longest Increasing Subsequence (LIS), Longest Common Subsequence (LCS), and 0/1 Knapsack.
- **Interactive Visualizations:**
  - **Recursive Tree Canvas:** Draggable trees with animated SVG edges and floating memoization dictionaries.
  - **1D / 2D Arrays:** Matrix layouts showing exactly which cells are actively updating or being compared.
- **Step-By-Step Playback:** Navigate back and forth through DP states using UI controls or keyboard shortcuts (`Space` to play/pause, `ArrowRight`/`ArrowLeft` to step).
- **Global Zoom:** Use `Ctrl + Scroll` or trackpad pinch to zoom in and out of the canvas.
- **Dark & Light Mode:** Full glassmorphism UI support for both themes.

## Tech Stack
- React + TypeScript
- Vite
- Tailwind CSS
- Framer Motion
- Monaco Editor (`@monaco-editor/react`)

## Run Locally
1. Install dependencies: `npm install`
2. Start development server: `npm run dev`
