'''
1. Find internal nodes
Let's assume we have a generic tree composed of consecutive integers (so if there is a 6 all numbers starting from and including 0 up to it also need to exist on the tree), such as follows:
Then we define this tree with a list L: [4, 4, 1, 5, -1, 4, 5] such as L(i) identifies the parent of i (the root has no parent and is denoted with -1). An internal node is any node of a tree that has at least one child, so in this case the total number of internal nodes is 3.
Implement the find_internal_nodes_num function (total number of internal nodes) as shown in the following snippet, knowing that:
an internal node is any node of a tree that has at least one child;
the solution should take into account complexity (time-wise) for very large trees; the solution should be implemented using Python.
def find_internal_nodes_num(tree):
    pass
my_tree = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num(my_tree))
'''

'''
Key ideas from the problem definition
- The list defines the parents of all nodes
- By the definition of internal node we know it is equivalent to a parent
- Hence the list defines all the internal nodes

Solution 1: using a set
- Step 1: convert the list to a set to get rid of duplicate values
- Step 2: remove the -1 value
- Step 3: count the number of elements in the set


Solution 2: iterating the list
- Step 1: iterate the list and count the occurrences of each element in a dictionary, excluding -1
- Step 2: count the number of elements in the dictionary
'''

# Set
def find_internal_nodes_num_set(tree):
    set_tree = set(tree)
    set_tree.remove(-1)
    return len(set_tree)

# Iterate
def find_internal_nodes_num_iter(tree):
    parent_count = {}
    
    for node in tree:
        if node != -1:
            parent_count[node] = parent_count.get(node, 0) + 1
    
    return len(parent_count)

my_tree = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num_set(my_tree))
print(find_internal_nodes_num_iter(my_tree))

# timeit with a tree of 1 million elements
import timeit
import random

tree_size = 10**6
large_tree = [-1]
large_tree += [random.randint(0, 1000) for _ in range(tree_size - 1)]

set_time = timeit.timeit(lambda: find_internal_nodes_num_set(large_tree), number=10)
iter_time = timeit.timeit(lambda: find_internal_nodes_num_iter(large_tree), number=10)

print(f"Set implementation time: {set_time:.6f} seconds")
print(f"Iter implementation time: {iter_time:.6f} seconds")
    

'''
timeit results:

Set implementation time: 0.223603 seconds
Iter implementation time: 1.581594 seconds

As expected, python internal method set(list) is faster than a list iteration
'''

find_internal_nodes_num = find_internal_nodes_num_set

print(find_internal_nodes_num(my_tree))
print(find_internal_nodes_num(large_tree))