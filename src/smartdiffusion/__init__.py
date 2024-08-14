import sys
from . import _
import nodes
import load
from .node import extra_nodes
sys.modules["comfy_extras"] = extra_nodes
load.autoload()
nodes.init_builtin_nodes("node", "nodes")
nodes.init_builtin_nodes("node", "extra_nodes")
