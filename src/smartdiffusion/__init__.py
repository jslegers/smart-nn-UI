import sys
import os
from . import _
import nodes as _nodes
from .node import extra_nodes
sys.modules["comfy_extras"] = extra_nodes
sys.modules[__name__] = _
current_dir = os.path.dirname(os.path.realpath(__file__))
nodes_dir = os.path.abspath(os.path.join(current_dir, "node", "nodes"))
nodes = os.listdir(nodes_dir)
for file in nodes:
    if(not file.startswith('__')):
        module_name = _nodes.get_module_name(os.path.join(nodes_dir, file))
        print(module_name)
        setattr(sys.modules[__name__], module_name, _.load.module(".node", module_name))
_nodes.init_builtin_nodes("node", "nodes")
_nodes.init_builtin_nodes("node", "extra_nodes")
