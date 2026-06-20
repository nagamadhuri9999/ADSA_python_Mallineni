// bstLogic.js
// Handles the data structure and generates animation frames for the visualizer.

export class TreeNode {
  constructor(val) {
    this.val = parseInt(val, 10);
    this.left = null;
    this.right = null;
    this.id = Math.random().toString(36).substr(2, 9); // Unique ID for React keys and SVG rendering
  }
}

export class BSTSimulator {
  constructor() {
    this.root = null;
    this.frames = [];
    this.callStack = [];
  }

  // Clones the tree to store a snapshot
  cloneTree(node) {
    if (!node) return null;
    const newNode = { ...node };
    newNode.left = this.cloneTree(node.left);
    newNode.right = this.cloneTree(node.right);
    return newNode;
  }

  addFrame(highlightNodeId = null, highlightEdgeId = null, activeCodeLine = -1, explanation = "", stateColor = "default", outputArray = null, operationType = "insert") {
    this.frames.push({
      root: this.cloneTree(this.root),
      callStack: [...this.callStack],
      highlightNodeId,
      highlightEdgeId,
      activeCodeLine,
      explanation,
      stateColor, // 'default', 'current', 'new', 'compare', 'recursive', 'delete'
      outputArray: outputArray ? [...outputArray] : (this.frames.length > 0 ? [...this.frames[this.frames.length - 1].outputArray] : []),
      operationType
    });
  }

  clearFrames() {
    this.frames = [];
  }

  // --- INSERT ---
  insert(val) {
    this.clearFrames();
    const value = parseInt(val, 10);
    if (isNaN(value)) return;
    
    this.callStack.push(`insert(${value})`);
    this.addFrame(null, null, 1, `Starting insertion of ${value}.`, "new", null, "insert");

    if (!this.root) {
      this.root = new TreeNode(value);
      this.addFrame(this.root.id, null, 3, `Tree is empty. Creating root node ${value}.`, "new", null, "insert");
      this.callStack.pop();
      return this.frames;
    }

    this._insertNode(this.root, value, null);
    this.callStack.pop();
    this.addFrame(null, null, 8, `Insertion of ${value} completed.`, "default", null, "insert");
    return this.frames;
  }

  _insertNode(node, val, parentId) {
    this.addFrame(node.id, null, 4, `Comparing ${val} with current node ${node.val}.`, "compare", null, "insert");

    if (val < node.val) {
      this.addFrame(node.id, null, 5, `${val} < ${node.val}. Moving to left subtree.`, "recursive", null, "insert");
      if (!node.left) {
        node.left = new TreeNode(val);
        this.addFrame(node.left.id, `${node.id}-${node.left.id}`, 5, `Left child is empty. Created new node ${val}.`, "new", null, "insert");
      } else {
        this.callStack.push(`insert(${val}) -> left`);
        this._insertNode(node.left, val, node.id);
        this.callStack.pop();
      }
    } else if (val > node.val) {
      this.addFrame(node.id, null, 7, `${val} > ${node.val}. Moving to right subtree.`, "recursive", null, "insert");
      if (!node.right) {
        node.right = new TreeNode(val);
        this.addFrame(node.right.id, `${node.id}-${node.right.id}`, 7, `Right child is empty. Created new node ${val}.`, "new", null, "insert");
      } else {
        this.callStack.push(`insert(${val}) -> right`);
        this._insertNode(node.right, val, node.id);
        this.callStack.pop();
      }
    } else {
      this.addFrame(node.id, null, 4, `${val} already exists in the tree.`, "compare", null, "insert");
    }
  }

  // --- SEARCH ---
  search(val) {
    this.clearFrames();
    const value = parseInt(val, 10);
    if (isNaN(value)) return;

    this.callStack.push(`search(${value})`);
    this.addFrame(null, null, 1, `Starting search for ${value}.`, "default", null, "search");

    let curr = this.root;
    while (curr) {
      this.addFrame(curr.id, null, 2, `Comparing ${value} with ${curr.val}.`, "compare", null, "search");
      if (curr.val === value) {
        this.addFrame(curr.id, null, 3, `Found ${value}!`, "current", null, "search");
        this.callStack.pop();
        return this.frames;
      } else if (value < curr.val) {
        this.addFrame(curr.id, null, 4, `${value} < ${curr.val}. Moving Left.`, "recursive", null, "search");
        curr = curr.left;
      } else {
        this.addFrame(curr.id, null, 6, `${value} > ${curr.val}. Moving Right.`, "recursive", null, "search");
        curr = curr.right;
      }
    }

    this.addFrame(null, null, 3, `Value ${value} not found in the tree.`, "delete", null, "search");
    this.callStack.pop();
    return this.frames;
  }

  // --- BUILD FROM ARRAY ---
  buildFromArray(arr) {
    this.root = null; // reset
    this.clearFrames();
    const cleanArr = arr.split(',').map(s => s.trim()).filter(s => s !== '').map(Number).filter(n => !isNaN(n));
    if (cleanArr.length === 0) return this.frames;
    
    // For bulk build we don't animate every single insertion deeply to save memory, 
    // but the user wants full animation, so let's animate them sequentially.
    const allFrames = [];
    for (const val of cleanArr) {
      this.insert(val);
      allFrames.push(...this.frames);
    }
    this.frames = allFrames;
    return this.frames;
  }

  // --- TRAVERSALS ---
  traverseInorder() {
    this.clearFrames();
    this.callStack.push(`inorder(root)`);
    this.addFrame(null, null, 1, `Starting Inorder Traversal (Left, Root, Right).`, "default", [], "inorder");
    const output = [];
    this._inorder(this.root, output);
    this.callStack.pop();
    this.addFrame(null, null, 0, `Inorder Traversal completed! Result: ${output.join(', ')}`, "current", output, "inorder");
    return this.frames;
  }

  _inorder(node, output) {
    if (!node) {
      this.addFrame(null, null, 3, `Node is None. Returning.`, "default", output, "inorder");
      return;
    }
    this.callStack.push(`inorder(${node.val})`);
    
    this.addFrame(node.id, null, 4, `Inorder: Moving to left child of ${node.val}.`, "recursive", output, "inorder");
    this._inorder(node.left, output);
    
    output.push(node.val);
    this.addFrame(node.id, null, 5, `Inorder: Visiting node ${node.val}. Adding to output.`, "current", output, "inorder");
    
    this.addFrame(node.id, null, 6, `Inorder: Moving to right child of ${node.val}.`, "recursive", output, "inorder");
    this._inorder(node.right, output);
    
    this.callStack.pop();
  }

  traversePreorder() {
    this.clearFrames();
    this.callStack.push(`preorder(root)`);
    this.addFrame(null, null, 1, `Starting Preorder Traversal (Root, Left, Right).`, "default", [], "preorder");
    const output = [];
    this._preorder(this.root, output);
    this.callStack.pop();
    this.addFrame(null, null, 0, `Preorder Traversal completed! Result: ${output.join(', ')}`, "current", output, "preorder");
    return this.frames;
  }

  _preorder(node, output) {
    if (!node) {
      this.addFrame(null, null, 3, `Node is None. Returning.`, "default", output, "preorder");
      return;
    }
    this.callStack.push(`preorder(${node.val})`);
    
    output.push(node.val);
    this.addFrame(node.id, null, 4, `Preorder: Visiting node ${node.val} first. Adding to output.`, "current", output, "preorder");
    
    this.addFrame(node.id, null, 5, `Preorder: Moving to left child of ${node.val}.`, "recursive", output, "preorder");
    this._preorder(node.left, output);
    
    this.addFrame(node.id, null, 6, `Preorder: Moving to right child of ${node.val}.`, "recursive", output, "preorder");
    this._preorder(node.right, output);
    
    this.callStack.pop();
  }

  traversePostorder() {
    this.clearFrames();
    this.callStack.push(`postorder(root)`);
    this.addFrame(null, null, 1, `Starting Postorder Traversal (Left, Right, Root).`, "default", [], "postorder");
    const output = [];
    this._postorder(this.root, output);
    this.callStack.pop();
    this.addFrame(null, null, 0, `Postorder Traversal completed! Result: ${output.join(', ')}`, "current", output, "postorder");
    return this.frames;
  }

  _postorder(node, output) {
    if (!node) {
      this.addFrame(null, null, 3, `Node is None. Returning.`, "default", output, "postorder");
      return;
    }
    this.callStack.push(`postorder(${node.val})`);
    
    this.addFrame(node.id, null, 4, `Postorder: Moving to left child of ${node.val}.`, "recursive", output, "postorder");
    this._postorder(node.left, output);
    
    this.addFrame(node.id, null, 5, `Postorder: Moving to right child of ${node.val}.`, "recursive", output, "postorder");
    this._postorder(node.right, output);
    
    output.push(node.val);
    this.addFrame(node.id, null, 6, `Postorder: Visiting node ${node.val}. Adding to output.`, "current", output, "postorder");
    
    this.callStack.pop();
  }
}

// Tree Coordinates Calculation (Reingold-Tilford simplified)
export function calculateNodePositions(root, width, height) {
  if (!root) return { nodes: [], edges: [] };
  const nodes = [];
  const edges = [];
  
  // Calculate max depth to determine vertical spacing
  const getDepth = (node) => {
    if (!node) return 0;
    return 1 + Math.max(getDepth(node.left), getDepth(node.right));
  };
  const maxDepth = getDepth(root);
  const verticalSpacing = Math.min(80, (height - 60) / (maxDepth || 1));

  const traverse = (node, depth, x, offset) => {
    if (!node) return;
    
    const y = 40 + depth * verticalSpacing;
    nodes.push({ ...node, x, y });

    if (node.left) {
      const childX = x - offset;
      const childY = 40 + (depth + 1) * verticalSpacing;
      edges.push({ id: `${node.id}-${node.left.id}`, x1: x, y1: y, x2: childX, y2: childY });
      traverse(node.left, depth + 1, childX, offset / 2);
    }
    if (node.right) {
      const childX = x + offset;
      const childY = 40 + (depth + 1) * verticalSpacing;
      edges.push({ id: `${node.id}-${node.right.id}`, x1: x, y1: y, x2: childX, y2: childY });
      traverse(node.right, depth + 1, childX, offset / 2);
    }
  };

  traverse(root, 0, width / 2, width / 4);
  return { nodes, edges };
}
