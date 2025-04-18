class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 第一步：特殊情况讨论：树为空，递归终止条件
        if not postorder:
            return

        # 第二步：后序遍历的最后一个节点就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 第三步：找切割点
        idx = inorder.index(root_val)

        # 第四步：切割inorder数组 得到inorder数组的左/右半边
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx + 1:]
        
        # 第五步：切割postorder，得到postorder数组的左/右半边
        # §重点1: 中序数组大小一定跟后序数组大小是相同的
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        # 第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        # 第七步：返回答案
        return root
