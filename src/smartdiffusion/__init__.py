import sys
import os
from smartdiffusion.load import autoload, module

base_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.dirname(base_path)

sys.path.extend([
     os.path.join(src_path, "ComfyUI"),
])

autoload(extra_objects = module("comfy").__dict__)
