class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 第一步：树为空，或是递归终止条件
        if not preorder:
            return None
        
        # 第二步：前序遍历的第一个就是当前的中间节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 第三步：找切割点
        idx = inorder.index(root_val)

        # 第四步：切割inorder数组，得到inorder数组的左/右半边
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        # 第五步：切割preoder数组，得到preoder数组的左/右半边
        # §重点1：中序数组大小一定跟前序数组大小相等
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]

        # 第六步：递归
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        # 第七步：返回答案
        return root
