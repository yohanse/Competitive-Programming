class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Root Left_subtree Right_subtree
        # Root [root, left_subtree, right_subtree] [root, left_subtree, right_subtree]
        # 5 2 1 3 6
        # root -- 5, left_subtree: 2 1 3  right_subtree: 6
        
        # preorder_traversal

        def is_bst(left, right, max_val, min_val):
            if right < left:
                return True
            
            
            
            node = preorder[left]
            l, r = left + 1, right
            while l < r:
                mid = (l + r) // 2
                if preorder[mid] > node:
                    r = mid
                else:
                    l = mid + 1
            
            if l == right and preorder[l] < node:
                l += 1

            
            is_left_bst = is_bst(left + 1, l - 1, min(max_val, node), min_val)
            is_right_bst = is_bst(l, right, max_val, max(min_val, node))
            return is_left_bst and is_right_bst and min_val < node < max_val
            
        
        return is_bst(0, len(preorder) - 1, inf, -inf)