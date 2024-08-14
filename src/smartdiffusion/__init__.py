def __init():
    from .__ import load, nodes
    me = load.autoload(extra_objects = [nodes])
    from . import _
    from . import ___
    me.update(___)
    del me._
    del me.__
    del me.___
    del me.__init
__init()
