def __init():
    import sys
    from . import __
    from .__ import load
    from ._.node import extra_nodes
    sys.modules["comfy_extras"] = extra_nodes
    load.add_to_env(__)
    import nodes
    load.autoload(extra_objects = [nodes])
__init()
