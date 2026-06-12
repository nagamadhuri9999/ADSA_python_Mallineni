import React, { useEffect } from 'react';
import Dashboard from './components/Dashboard';
import { useStore } from './store/useStore';

function App() {
  const { generateArray, isPlaying, stepForward, speed, mode } = useStore();

  useEffect(() => {
    generateArray();
  }, [generateArray]);

  // Automatic Playback Loop
  useEffect(() => {
    let timerId;
    if (isPlaying) {
      // In 'learn' mode, we might want to pause after every step and wait for user input, 
      // but for now we just play slower.
      const actualSpeed = mode === 'learn' ? speed * 2 : speed;
      timerId = setTimeout(() => {
        stepForward();
      }, actualSpeed);
    }
    return () => clearTimeout(timerId);
  }, [isPlaying, stepForward, speed, mode]);

  // Keyboard controls
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'ArrowRight') {
        useStore.setState({ isPlaying: false });
        useStore.getState().stepForward();
      } else if (e.key === 'ArrowLeft') {
        useStore.setState({ isPlaying: false });
        useStore.getState().stepBackward();
      } else if (e.key === ' ') {
        e.preventDefault();
        useStore.getState().playPause();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="w-full h-screen bg-slate-900 text-slate-100 font-sans overflow-hidden">
      <Dashboard />
    </div>
  );
}

export default App;
