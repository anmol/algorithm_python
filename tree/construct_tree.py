#!/usr/bin/env python2.7

from tree import BinaryTree


def construct_tree(inorder, preorder):
    global index
    node = preorder[0]
    t = BinaryTree(node)
    index += 1
    left_inorder = inorder.split(node)[0]
    right_inorder = inorder.split(node)[1]
    if len(left_inorder) > 1 and len(preorder[index:]) > 0:
        t.insert_left(construct_tree(left_inorder, preorder[index:]))
    else:
        t.insert_left(BinaryTree(left_inorder))
        index += 1
    if len(right_inorder) > 1 and len(preorder[index:]) > 0:
        t.insert_right(construct_tree(right_inorder, preorder[index:]))
    else:
        t.insert_right(BinaryTree(right_inorder))
        index += 1
    return t



if __name__ == "__main__":
    inorder = 'DBEAFC'
    preorder = 'ABDECF'
    index = 0
    t = construct_tree(inorder, preorder)
    t.traverse()


