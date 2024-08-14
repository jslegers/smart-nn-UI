import sys
import os
import .node.extra_nodes as extra_nodes
sys.modules["comfy_extras"] = extra_nodes
from .. import __
__.load.add_to_env(__)
import nodes

def init_builtin_nodes(*args):
    """
    Initializes the built-in nodes in Smart Diffusion Server.

    This function loads the extra node files located in the "nodes" and "extra_nodes" directories and import them into Smart Diffusion Server.
    If any of the extra node files fail to import, a warning message is logged.

    Returns:
        None
    """
    location = os.path.join(*args)
    extras_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), location)
    )
    extras_files = os.listdir(extras_dir)
    if "__pycache__" in extras_files:
        extras_files.remove("__pycache__")
    import_failed = []
    for node_file in extras_files:
        if not nodes.load_custom_node(
            os.path.join(extras_dir, node_file), module_parent=location
        ):
            import_failed.append(node_file)
    return import_failed

init_builtin_nodes("node", "nodes")
init_builtin_nodes("node", "extra_nodes")
