import sys
from . import _
import nodes
from .node import nodes, extra_nodes
sys.modules["comfy_extras"] = extra_nodes
sys.modules['smartdiffusion'] = _
for node in dir(nodes):
    if(not node.startswith('__')):
        sys.modules['smartdiffusion.'+ node] = _.load.module("nodes", node)
nodes.init_builtin_nodes("node", "nodes")
nodes.init_builtin_nodes("node", "extra_nodes")
