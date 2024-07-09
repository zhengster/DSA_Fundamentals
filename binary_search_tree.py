class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        pass          

# DFS 
def dfs(root): 
    pass 

# BFS
def bfs(root): 
    pass 

# PRE-ORDER
def pre_order(root): 
    """
    Root, Left, Right
    """
    if root is None: 
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right) 

# IN-ORDER
def in_order(root): 
    """
    Left, Root, Right 
    """
    if root is None: 
        return [] 
    return in_order(root.left) + [root.val] + in_order(root.right) 

def in_order_iter(root): 
    """
    Iterative solution. 
    Go down left subtree as far as possible. 
    Then go down the right subtree as far as possible. 
    """
    if root is None: 
        return [] 
    
    cur = root 
    stack = [] 
    order = [] 

    while cur or stack: 
        # Go as far down to the left as possible 
        while cur: 
            stack.append(cur) 
            cur = cur.left 
        
        # Once you can't go left anymore, pop the most recently added node and add that to the level order traversal
        cur = stack.pop() 
        order.append(cur.val)

        # Go to the right subtree 
        cur = cur.right 

    return order  

# POST-ORDER
def post_order(root): 
    """
    Left, Right, Root 
    """
    if root is None: 
        return [] 
    return post_order(root.left) + post_order(root.right) + [root.val] 

def post_order_iter(root): 
    """
    Iterative solution. 
    Go down the left subtree as far as possible. 
    Then go down the right subtree as far as possible. 
    Then add the root to the order. 
    """
    if root is None: 
        return [] 
    
    stack = [root] 
    visit = [False]
    order = [] 

    # TOOD         
        

# BALANCED BINARY TREE
def balanced_bst(root): 
    """
    A BST is balanced if the left and right subtrees are both balanced 
    AND if the difference in height between the left and right subtrees
    is <= 1. 
    """
    def dfs_height_balanced(root): 
        if root is None: 
            return (0, True) # Return (height, whether or not the tree is balanced)
        # Recurse on left and right subtrees
        left = dfs_height_balanced(root.left) 
        right = dfs_height_balanced(root.right) 
        
        # Compute height on current subtree 
        height = max(left[0], right[0]) + 1 
        # Determine whether tree is height balanced
        is_balanced = (left[1] and right[1]) and (abs(left[0] - right[0]) <= 1)
        return (height, is_balanced) 


# LOWEST COMMON ANCESTOR: BST 
def lca_bst(root, p, q): 
    """
    Note that a root can be the lowest common ancestor of itself. 
    The trick is to use the definition of a BST. For example, if root.val 
    is bigger than both p.val and q.val, then that means we need to 
    search root's left subtree to find p and q's LCA. 
    """
    if root is None: 
        return None 
    if root == p or root == q: 
        return root 
    # Search left subtree
    elif root.val > p.val and root.val > q.val: 
        return lca_bst(root.left, p, q) 
    # Search right subtree
    elif root.val < p.val and root.val < q.val: 
        return lca_bst(root.right, p.val, q.val) 
    # If root.val is between p.val and q.val, that means root is the LCA
    else: 
        return root 

# LOWEST COMMON ANCESTOR: BINARY TREE 
def lca(root, p, q): 
    """
    This time, the tree is a binary tree rather than a BST. 
    There is no rule that left subtree values < root val < right subtree values. 
    """
    if root is None: 
        return root 
    
    if root == p or root == q: 
        return root 
    
    left = lca(root.left, p, q) 
    right = lca(root.right, p, q) 

    # If p and q are each found in separate subtrees, the current root is the LCA
    if left and right: # If left and right are not None,
        return root 
    
    # Else, p and q are found on one side. Return the side that has both p and q. 
    else: 
        return left or right 

# DIAMETER 
def diameter_bst(root): 
    pass 

# VALID BST 
def valid_bst(root): 
    """
    The values in the left subtree are strictly less than the root, 
    and the values in the right subtree are strictly greater. 

    The trick is to recurse using two variables, min and max, 
    and ensure the values of the subtree rooted at root are >= min 
    and <= max. 
    """
    def recurse(root, min, max): 
        if root is None: 
            return True
        elif not (root.val > min and root.val < max):  
            return False 
        else: 
            is_left_valid = recurse(root.left, min, root.val) 
            is_right_valid = recurse(root.right, root.val, max) 
            return is_left_valid and is_right_valid
    
    minimum, maximum = -1 * float('inf'), float('inf')
    return recurse(root, minimum, maximum)     

