int dfs(struct TreeNode* root,int *nodes, int index){
    if (!root)
        return NULL;
    if (nodes[index] == -1)
        nodes[index] = root->val;
    int size = dfs(root->right, nodes, index + 1);
    size = fmax(dfs(root->left, nodes, index + 1), size);
    ++size;

    return size;
}

int* rightSideView(struct TreeNode* root, int* returnSize){
    int *nodes = malloc(sizeof(int) * 100);
    for (int i = 0; i < 100; ++i) {
        nodes[i] = -1;
    }
    *returnSize = dfs(root, nodes, 0);
    return nodes;
}
