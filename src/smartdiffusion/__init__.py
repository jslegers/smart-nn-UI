import sys
from . import _
import nodes as _nodes
from .node import nodes, extra_nodes
sys.modules["comfy_extras"] = extra_nodes
sys.modules[__name__] = _
for node in dir(nodes):
    if(not node.startswith('__')):
        setattr(sys.modules[__name__], node, _.load.module("nodes", node))
_nodes.init_builtin_nodes("node", "nodes")
_nodes.init_builtin_nodes("node", "extra_nodes")
