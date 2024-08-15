def __init():
    from . import __
    from .__ import load
    load.add_to_env(__)
    import nodes
    me = load.autoload(extra_objects = [nodes])
    from ._ import init_builtin_nodes
    return init_builtin_nodes
__init_builtin_nodes = __init()
__init_builtin_nodes("node", "nodes")
__init_builtin_nodes("node", "extra_nodes")
