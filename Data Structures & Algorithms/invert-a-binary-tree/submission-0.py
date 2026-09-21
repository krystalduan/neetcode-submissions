# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        

        def switch (c):
            if c == None:
                return
            switch(c.left)
            switch(c.right)
            temp = c.left
            c.left = c.right
            c.right = temp
        
        switch(curr)
        return root
        
        