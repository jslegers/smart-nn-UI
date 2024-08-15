from . import load

def __init(self):
    import sys
    import os
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent_dir, '_'))
    sys.path.append(os.path.join(parent_dir, '__'))
    new_env = os.environ.copy()
    new_env["SMARTDIFFUSION_PATH"] = parent_dir


    parent_dir = os.path.dirname(os.path.realpath(__file__))
    nodes_dir = os.path.join(parent_dir, "__", "nodes", "node")
    sys.path.append(nodes_dir)
    import nodes

    def __init_builtin_nodes(*args):
        """
        Initializes the built-in nodes in Smart Diffusion Server.

        This function loads the extra node files located in the "nodes" and "extra_nodes" directories and import them into Smart Diffusion Server.
        If any of the extra node files fail to import, a warning message is logged.

        Returns:
            None
        """
        location = os.path.join(*args)
        extras_dir = os.path.abspath(os.path.join(nodes_dir, location))
        extras_files = os.listdir(extras_dir)
        if "__pycache__" in extras_files:
            extras_files.remove("__pycache__")
        if "__init__.py" in extras_files:
            extras_files.remove("__init__.py")
        import_failed = []
        for node_file in extras_files:
            if not nodes.load_custom_node(
                os.path.join(extras_dir, node_file), module_parent=args[-1]
            ):
                import_failed.append(node_file)
        return import_failed


    __init_builtin_nodes("nodes")
    __init_builtin_nodes("comfy_extras")

load.autoload(stop_at_sub_package = False, afer_init = __init)
