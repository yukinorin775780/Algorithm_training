# 递归法1
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 情况1:根节点为空或者没有找到key
        if not root:
            return root
        # 找到key    
        if root.val == key:
            # 情况2:key节点为叶子结点
            if not root.left and not root.right:
                return None
            # 情况3:key节点没有左子树，有右子树
            elif not root.left:
                return root.right
            # 情况4:key节点没有右子树，有左子树
            elif not root.right:
                return root.left
            # 情况5:key节点有左右子树
            else:
                cur = root.right
                # 找到key节点右子树的最左侧叶子结点 即最小值
                while cur.left:
                    cur = cur.left
                # 将key节点的左子树 挂在 key节点右子树的最左侧叶子结点的左侧
                cur.left = root.left
                # 返回key节点的右子树
                return root.right
            
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root

# 递归法2
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # 如果根节点为空，直接返回
            return root

        if root.val == key: # 找到key节点
            if not root.right: # 如果右子树为空，直接返回左子树作为新的根节点
                return root.left
            cur = root.right 
            while cur.left: # 找到右子树中的最左节点
                cur = cur.left
            root.val, cur.val = cur.val, root.val # 将要删除的节点值与最左节点值交换
        root.left = self.deleteNode(root.left, key) # 在左子树中递归删除目标节点
        root.right = self.deleteNode(root.right, key) # 在右子树中递归删除目标节点
        return root


# 迭代法
class Solution:
    def deleteOneNote(self, target):
        """
        将key节点的左子树放到key节点的右子树的最左节点的左孩子上
        并返回key节点的右孩子作为新的根节点
        """
        if not target:
            return target
        if not target.right:
            return target.left
        cur = target.right
        while cur.left:
            cur = cur.left
        cur.left = target.left
        return target.right

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        cur = root
        pre = None # 记录cur的父节点，用于删除cur
        while cur:
            if cur.val == key:
                break
            pre = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if not pre: # 如果树只有头节点
            return self.deleteOneNote(cur)
        # pre要知道是删除左孩子还是右孩子
        if pre.left and pre.left.val == key:
            pre.left = self.deleteOneNote(cur)
        if pre.right and pre.right.val == key:
            pre.right = self.deleteOneNote(cur)
        
        return root
