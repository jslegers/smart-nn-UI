import sys
from . import _
import nodes
sys.modules['smartdiffusion'] = _
nodes.init_builtin_nodes("node", "nodes")
nodes.init_builtin_nodes("node", "extra_nodes")
