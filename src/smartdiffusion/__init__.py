import sys
from . import _
import nodes
from .node import extra_nodes
sys.modules["comfy_extras"] = extra_nodes
sys.modules['smartdiffusion'] = _
nodes.init_builtin_nodes("node", "nodes")
nodes.init_builtin_nodes("node", "extra_nodes")
