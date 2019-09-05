# Best Fit Bin Packing Algorithm in O(n log n)

The best fit bin packing algorithm is generally implemented in O(n**2). 

In this implementation, the algorithm runs in O(nlogn) with the use of a hash table.

The algorithm initiates a class for each bin which accepts add, remove, sum and show operations.

The AVL tree stores the capacity of each bin. As elements are added to a bin or a new bin is created, the AVL tree is updated. 

A hash table stores the capacity and index of bin as key, value pairs.

The best_fit() function traverses through the AVL tree to find the least capacity that is greater than or equal to the item. 

If a suitable capacity is found, the corresponding bin index is obtained from the hash table and the element is added to that bin – the AVL tree and the hash table are updated.

If no suitable capacity is found in the AVL tree, a new bin is created for the element and the remaining capacity is added to the AVL tree. 

The (capacity, bin_index) is added as key, value pair in the hash table.

The algorithm only traverses the height of the AVL tree (log n). Therefore, the total runtime complexity improves to O(nlogn). 

To apply this to best fit decreasing, you can sort the items and apply the best fit algorithm.
