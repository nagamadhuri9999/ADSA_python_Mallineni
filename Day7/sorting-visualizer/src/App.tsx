import { useEffect } from 'react';
import Dashboard from './components/Dashboard';
import { useStore } from './store/useStore';

function App() {
  const generateArray = useStore(state => state.generateArray);
  const isPlaying = useStore(state => state.isPlaying);
  const stepForward = useStore(state => state.stepForward);
  const stepBackward = useStore(state => state.stepBackward);
  const playPause = useStore(state => state.playPause);
  const speed = useStore(state => state.speed);
  const mode = useStore(state => state.mode);

  const theme = useStore(state => state.theme);

  useEffect(() => {
    generateArray();
  }, [generateArray]);

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  // Automatic Playback Loop
  useEffect(() => {
    let timerId: ReturnType<typeof setTimeout>;
    if (isPlaying) {
      // In 'learn' mode, slow down significantly to allow reading
      const actualSpeed = mode === 'learn' ? speed * 3 : speed;
      timerId = setTimeout(() => {
        stepForward();
      }, actualSpeed);
    }
    return () => clearTimeout(timerId);
  }, [isPlaying, stepForward, speed, mode]);

  // Keyboard controls
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight') {
        useStore.setState({ isPlaying: false });
        stepForward();
      } else if (e.key === 'ArrowLeft') {
        useStore.setState({ isPlaying: false });
        stepBackward();
      } else if (e.key === ' ') {
        e.preventDefault();
        playPause();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [stepForward, stepBackward, playPause]);

  return (
    <div className="w-full h-screen bg-base text-primary overflow-hidden font-sans transition-colors duration-300">
      <Dashboard />
    </div>
  );
}

export default App;
