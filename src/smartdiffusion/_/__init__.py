import sys
import os
from .node import extra_nodes
sys.modules["comfy_extras"] = extra_nodes
import nodes

current_dir = os.path.dirname(os.path.realpath(__file__))

def init_builtin_nodes(*args):
    """
    Initializes the built-in nodes in Smart Diffusion Server.

    This function loads the extra node files located in the "nodes" and "extra_nodes" directories and import them into Smart Diffusion Server.
    If any of the extra node files fail to import, a warning message is logged.

    Returns:
        None
    """
    location = os.path.join(*args)
    extras_dir = os.path.abspath(os.path.join(current_dir, location))
    extras_files = os.listdir(extras_dir)
    if "__pycache__" in extras_files:
        extras_files.remove("__pycache__")
    import_failed = []
    for node_file in extras_files:
        if not nodes.load_custom_node(
            os.path.join(extras_dir, node_file), module_parent=args[-1]
        ):
            import_failed.append(node_file)
    return import_failed
