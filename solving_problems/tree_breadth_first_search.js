import { TreeNode } from './tree_node';
import { Deque } from './deque';
//Binary Tree Level Order Traversal (easy)


//Given a binary tree, populate an array to represent its level-by-level traversal. 
//You should populate the values of all nodes of each level from left to right in separate sub-arrays.

//so let's create a binary tree to further operate on it
//12,7,1,9,10,5


let root = new TreeNode(12);
root.left = new TreeNode(7);
root.right = new TreeNode(1);
root.left.left = new TreeNode(9);
root.right.left = new TreeNode(10);
root.right.right = new TreeNode(5);


function traverseLevelOrder(root){
    const result = [];
    if(!root) return result;

    const queue = [];
    currentLevel = [];
    queue.push(root);

    while(queue.length != 0){
        const currentNode = queue.shift();
        //clearing the queue by shifting/removing the current node,
        //so the queue length is 0 now
        currentLevel.push(currentNode);
        // add the node to the current level

        console.log(`${currentNode.val} `);
        // insert the children of current node in the queue
        //so the queue length is not 0 anymore until there are child nodes
        if(currentNode.left != null) {
            queue.push(currentNode.left);
        }

        if(currentNode.right != null) {
            queue.push(currentNode.right);
        }

        result.push(currentLevel);
    }
    
    return result;
}

console.log(`level order traversal of the binary tree: ${traverseLevelOrder(root)}`);



