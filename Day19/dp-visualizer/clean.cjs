const fs = require('fs');
const path = require('path');

function replaceClasses(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      replaceClasses(fullPath);
    } else if (fullPath.endsWith('.tsx')) {
      let content = fs.readFileSync(fullPath, 'utf8');
      
      // Remove specific redundant dark classes
      content = content.replace(/ dark:bg-panel-dark/g, '');
      content = content.replace(/ dark:border-border-dark/g, '');
      content = content.replace(/ dark:bg-border-dark/g, '');
      content = content.replace(/ dark:text-text-h-dark/g, '');
      content = content.replace(/ dark:bg-white\/5/g, '');
      content = content.replace(/ dark:bg-white\/10/g, '');
      content = content.replace(/ dark:hover:bg-white\/5/g, '');
      content = content.replace(/ dark:hover:bg-white\/10/g, '');
      
      // Add 'glass-panel' to bg-panel occurrences unless already there
      content = content.replace(/bg-panel(?![A-Za-z0-9_-])/g, 'bg-panel glass-panel');
      content = content.replace(/glass-panel glass-panel/g, 'glass-panel');
      
      fs.writeFileSync(fullPath, content);
    }
  }
}

replaceClasses(path.join(__dirname, 'src'));
console.log("Cleanup complete");
