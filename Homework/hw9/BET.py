import itertools


class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, node): 
        self.left = node

    def add_right(self, node):
        self.right = node

    def evaluate(self):
        if self.value not in BETNode.OPERATORS:
            return BETNode.CARD_VAL_DICT.get(self.value)
        
        if self.left is not None and self.right is not None:
            right_value = self.right.evaluate()
            left_value = self.left.evaluate()
            operator = self.value
            if operator == '/' and right_value==0:
                return 1000000
            return eval(f'{left_value} {operator} {right_value}')

    
    def __repr__(self):
        if self.value not in BETNode.OPERATORS:
            return self.value
        
        # if statement needed to run in VS-Code
        if self.left is not None and self.right is not None:
            return f'({repr(self.left)}{self.value}{repr(self.right)})' 



def create_trees(cards): 
    possible_tree_structures = {'CCCCXXX', 'CCXCCXX', 'CCXCXCX', 'CCCXXCX', 'CCCXCXX'}
    operators = ['+', '-', '*', '/']
    combinations_cards = list(itertools.permutations(cards))
    combinations_operators = list(itertools.product(operators, repeat=3))
    all_tree_combinations = set()
    for combo_cards in combinations_cards:
        for combo_operator in combinations_operators:
            for pos_tree in possible_tree_structures:
                tree = BETNode(combo_operator[0])
                if pos_tree == 'CCCCXXX':
                    tree.add_right(BETNode(combo_operator[1]))
                    tree.add_left(BETNode(combo_cards[0]))
                    if tree.right is not None:
                        tree.right.add_right(BETNode(combo_operator[2]))
                        tree.right.right.add_right(BETNode(combo_cards[0]))
                        tree.right.right.add_left(BETNode(combo_cards[1]))
                        tree.right.add_left(BETNode(combo_cards[2]))
                        tree.add_left(BETNode(combo_cards[3]))
                
                elif pos_tree == 'CCXCCXX':
                    tree.add_right(BETNode(combo_operator[1]))
                    tree.add_left(BETNode(combo_operator[2]))
                    if tree.right is not None and tree.left is not None:
                        tree.right.add_right(BETNode(combo_cards[0]))
                        tree.right.add_left(BETNode(combo_cards[1]))
                        tree.left.add_right(BETNode(combo_cards[2]))
                        tree.left.add_left(BETNode(combo_cards[3]))
                    
                elif pos_tree == 'CCXCXCX':
                    tree.add_right(BETNode(combo_cards[0]))
                    tree.add_left(BETNode(combo_operator[1]))
                    if tree.left is not None:
                        tree.left.add_right(BETNode(combo_cards[1]))
                        tree.left.add_left(BETNode(combo_operator[2]))
                        tree.left.left.add_right(BETNode(combo_cards[2]))
                        tree.left.left.add_left(BETNode(combo_cards[3]))
                    
                elif pos_tree == 'CCCXXCX':
                    tree.add_right(BETNode(combo_cards[0]))
                    tree.add_left(BETNode(combo_operator[1]))
                    if tree.left is not None:
                        tree.left.add_right(BETNode(combo_operator[2]))
                        tree.left.add_left(BETNode(combo_cards[1]))
                        tree.left.right.add_right(BETNode(combo_cards[2]))
                        tree.left.right.add_left(BETNode(combo_cards[3]))
                
                elif pos_tree == 'CCCXCXX':
                    tree.add_right(BETNode(combo_operator[1]))
                    tree.add_left(BETNode(combo_cards[0]))
                    if tree.right is not None:
                        tree.right.add_right(BETNode(combo_cards[1]))
                        tree.right.add_left(BETNode(combo_operator[2]))
                        tree.right.left.add_right(BETNode(combo_cards[2]))
                        tree.right.left.add_left(BETNode(combo_cards[3]))

                all_tree_combinations.add(tree)
    return all_tree_combinations
                    
def find_solutions(cards):
    possible_trees = create_trees(cards)
    result = set()
    for tree in possible_trees:
        if tree.evaluate() == 24:
            result.add(repr(tree))
    return result
       