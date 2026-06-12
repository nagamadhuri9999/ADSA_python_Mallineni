import { useEffect } from 'react';
import Dashboard from './components/Dashboard';
import { useStore } from './store/useStore';

function App() {
  const { theme } = useStore();

  // Apply dark mode class to html element
  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [theme]);

  return (
    <div className="w-screen h-screen">
      <Dashboard />
    </div>
  );
}

export default App;
