from . import load

def __init():
    import sys
    import os
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.join(parent_dir, '_'))
    sys.path.append(os.path.join(parent_dir, '__'))
    new_env = os.environ.copy()
    new_env["SMARTDIFFUSION_PATH"] = parent_dir
    import smartdiffusion
__init()
