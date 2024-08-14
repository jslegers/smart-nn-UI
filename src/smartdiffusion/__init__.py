import sys
from . import _, node
setattr(_, "comfy_extras", node.extra_nodes)
sys.modules['smartdiffusion'] = _
_.nodes.init_builtin_nodes("node", "nodes")
_.nodes.init_builtin_nodes("node", "extra_nodes")
