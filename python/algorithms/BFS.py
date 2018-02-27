import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_structures.BST import Node 


b = Node(4)
b.print_in_order()
