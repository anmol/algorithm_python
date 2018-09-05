#!/usr/bin/env python2.7


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        t = []
        q = [root]

        def level_order(q, t):
            if len(q) != 0:
                node = q.pop(0)
                if node:
                    t.append(node.val)
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
                else:
                    t.append(None)
                level_order(q, t)
        if root:
            level_order(q, t)

            while t[-1] is None:
                t.pop(-1)
        return str(t)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        t = data.strip('[]').split(',')
        l = len(t)
        if l > 0:
            root = TreeNode(t[0])
        else:
            return None
        q = []
        count = 0
        cur = None
        q.append(root)
        for i in range(1, l):
            node = TreeNode(t[i])
            if count == 0:
                #print i
                cur = q.pop(0)
            if count == 0:
                count += 1
                if node.val is not None:
                    cur.left = node
                else:
                    cur.left = None
            else:
                count = 0
                if node.val is not None:
                    cur.right = node
                else:
                    cur.right = None
            if t[i] is not None:
                q.append(node)
        return root


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    #data = '[1,2,3,None,None,4,5]'
    data = '[0,0,0,0,None,None,1,None,None,None,2]'
    print codec.serialize(codec.deserialize(data))
    #codec.deserialize(codec.serialize(root))