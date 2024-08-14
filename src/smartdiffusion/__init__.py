def __init():
    from .__ import load, nodes
    me = load.autoload(extra_objects = [nodes])
    from ._ import _nodes
    me = me + _nodes
    from . import ___
    me = me + ___
    del me._
    del me.__
    del me.___
    del me.__init
__init()
