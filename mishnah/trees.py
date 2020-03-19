'''rather than implementing our own tree data structure from scratch, 
   we can simply use the anytree library. 

   See: https://anytree.readthedocs.io/en/latest/api.html for the API,

   We will use this data strucutre to explain Mishnayot, such as the first in Ketubut.
   
   Install by running pip install anytree. 
   
   To save human-friendly images of the trees, run the following command: 
   
   sudo apt install graphviz.
   
   The following is a simple demonstration involving a tree with one root that has two children:
'''

from anytree import Node, RenderTree
from anytree.exporter import DotExporter   

# wire up the nodes to each other, making a linked structure
root = Node("root")
left_child = Node("left_child", parent=root)
right_child = Node("right_child", parent=root)

print(root.children)

# print out a representation of the tree on the commmand line
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

# save an image of the tree starting from the root in the current working directory called 'root.png'
DotExporter(root).to_picture("root.png")

