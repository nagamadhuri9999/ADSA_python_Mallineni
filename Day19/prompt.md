# Build an Interactive Dynamic Programming (DP) Visualization Platform

Build a **modern educational website** that teaches **Dynamic Programming** through **highly interactive visualizations**, **step-by-step execution**, **animations**, and **algorithm simulations**.

The website should feel like a combination of **VisuAlgo**, **Python Tutor**, **AlgoMonster**, and **LeetCode Explore**, but significantly more interactive and beginner friendly. The objective is to make students understand **why every DP state changes**, not just show the final answer.

## General Requirements
Create a responsive web application using:
* React (with TypeScript)
* Vite (for tooling)
* Tailwind CSS (for styling and layout)
* Framer Motion (for all animations and layout transitions)
* Monaco Editor (for a premium code viewer)
* `react-use-measure` / SVG (for dynamic layouts)

## Design Aesthetics (CRITICAL)
- **Premium Look & Feel:** The interface must look visually stunning and premium right from the start. Use glassmorphism effects (backdrop-blur, semi-transparent backgrounds), vibrant accent colors, and deep gradients.
- **Theme Support:** Implement a flawless Light and Dark mode using pure CSS variables (e.g., `--bg`, `--panel`, `--text`, `--accent`). Ensure text readability and high-contrast accents in both themes.
- **Animations:** Everything must animate smoothly using Framer Motion. Elements should gracefully scale and slide in, layout changes should use `layout` props to avoid jumping, and active/updated states must have micro-interactions (e.g. glowing rings, scale changes).
- **Global Layout:** Use a resizable three-panel layout (Sidebar, Code Editor, Visualization Canvas).
- **Interactivity:** The global canvas should support scrolling, keyboard arrow-key navigation (Left/Right to step through, Spacebar to play/pause), and global zooming (Ctrl + mouse wheel or trackpad pinch).

## Features & Implementation Specifications

### 1. The Algorithm Engine (State Management)
Create an execution engine context (`ExecutionContext.tsx`) that acts like a debugger. It must:
- Pre-compute all states (memo arrays, DP matrices, recursion trees) for the given problem upfront.
- Manage playback state (`currentStep`, `isPlaying`, `speed`, `zoomLevel`).
- Bind global keyboard event listeners to step forward (`ArrowRight`), backward (`ArrowLeft`), and toggle auto-play (`Space`).
- Map each step to the exact line of code currently being executed.

### 2. Algorithms to Support
Implement five distinct DP modules:
1. **Fibonacci (Memoization):** Show the top-down recursive call stack. Render a dynamic tree structure.
2. **Fibonacci (Tabulation):** Show bottom-up array filling (1D Array).
3. **Longest Increasing Subsequence (LIS):** Show 1D Array manipulation and nested loops comparing array indices.
4. **Longest Common Subsequence (LCS):** Show 2D Matrix manipulation.
5. **0/1 Knapsack:** Show 2D Matrix manipulation with weights and values.

### 3. Visualization Canvas Components
Create three primary visualization components inside the main canvas:

#### A. Recursive Tree Visualizer
- Takes in a state object of nodes and edges representing the call stack.
- **Layout Calculation:** Automatically compute the X and Y coordinates of nodes based on their depth and sibling count.
- **SVG Edges:** Render animated `<motion.line>` SVG paths connecting parents to children.
- **Nodes:** Render nodes with states like `active` (glowing accent), `cache-hit` (yellow), and `done` (green).
- **Memoization Dictionary:** Render a floating "Memo Dictionary" panel fixed to the top right. It should display key-value pairs of cached results, entering the screen via Framer Motion.
- **Mouse Panning:** Wrap the entire tree (SVG + Nodes) in a `<motion.div drag>` component so the user can freely click and drag the tree around when it gets too large.

#### B. 1D Array Visualizer
- Render a horizontal array of square boxes.
- Support `activeIndices`, `compareIndices`, and `updatedIndices`.
- Highlight elements with distinct colors (e.g., emerald for updated, amber for compare, accent for active).
- Ensure elements use `<AnimatePresence mode="popLayout">` so that the array can grow gracefully.

#### C. 2D Matrix Visualizer
- Render a grid/table for classic 2D DP problems.
- Label the rows and columns properly (e.g., string characters for LCS, items/capacity for Knapsack).
- Highlight the exact `activeCell`, `compareCells` (cells looked up to derive the current cell), and `updatedCells`.
- Transitions should use standard Framer Motion layout animations.

### 4. Code Editor Panel
- Integrate `@monaco-editor/react`.
- When a step is executed, visually highlight the active line of code to map the conceptual state back to the programmatic implementation.

### 5. UI Layout details
- Top Header: Includes the title, a Theme Toggle button, and standard playback controls (Play/Pause, Step Back, Step Forward, Speed 1x/2x/4x slider).
- Left Sidebar: A list of clickable topics switching the current DP algorithm.
- Center Panel: The Monaco code viewer.
- Right Panel: The Visualization Canvas (Tree, 1D, or 2D).

The final product must not look like a standard hackathon project. It must look and feel like a paid, enterprise-grade educational tool.
