class Solution:

    def height(self, root):
        if root is None:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root):
        if root is None:
            return True

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        if self.isBalanced(root.left) == False:
            return False

        if self.isBalanced(root.right) == False:
            return False

        return True
