def __init():
    from .__.load import autoload, nodes
    me = autoload(extra_objects = [nodes])
    from . import _
    from . import ___
    me.update(___)
    del me.__init
__init()
