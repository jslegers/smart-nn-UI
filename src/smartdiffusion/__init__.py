import sys
from . import _
from .node import extra_nodes
setattr(_, "comfy_extras", extra_nodes)
sys.modules['smartdiffusion'] = _
_.nodes.init_builtin_nodes("node", "nodes")
_.nodes.init_builtin_nodes("node", "extra_nodes")
