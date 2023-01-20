from random import shuffle  # needed for tests


def to_tree(source):
    # First we create a map of nodes, so that we can refer to them by ID
    # and build subtrees where the node is the root.
    # *Key*     - ID of the node
    # *Value*   - the subtree, where the node is the root
    nodes_table = {}
    for parent_id, node_id in source:
        nodes_table[node_id] = {}

    # The `tree` is what we are going to return
    tree = {}

    # We iterate over the `source` list, getting the `parent_id` and `node_id`.
    # We can find the subtree with the parent is the root. This is going to be
    # the subtree we need to insert our current node in.
    # However, if the `parent_id` is None, then we need to insert the subtree
    # where the root is the current node to the resulting `tree`.
    for parent_id, node_id in source:
        # Find the subtree where the current node is the root
        subtree = nodes_table[node_id]

        if parent_id is None:
            # The current node is one of the roots of the resulting `tree`
            tree[node_id] = subtree
        else:
            # Insert the current node into the subtree
            # where the parent is the root
            parent = nodes_table[parent_id]
            parent[node_id] = subtree

    return tree


source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected

# Different order of the `source`
shuffle(source)
assert to_tree(source) == expected