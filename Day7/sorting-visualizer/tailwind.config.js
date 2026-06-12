/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        base: 'var(--bg-base)',
        panel: 'var(--bg-panel)',
        border: 'var(--border-panel)',
        primary: 'var(--text-primary)',
        secondary: 'var(--text-secondary)',
        btn: 'var(--btn-bg)',
        'btn-hover': 'var(--btn-hover)'
      },
      boxShadow: {
        panel: 'var(--shadow-panel)'
      }
    },
  },
  plugins: [],
}
