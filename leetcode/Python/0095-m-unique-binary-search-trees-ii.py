# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generate_trees(1, n)
        
    def generate_trees(self, start, end):
        if start > end:
            return [None,]
        
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1)
            right_trees = self.generate_trees(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
        
        return all_trees