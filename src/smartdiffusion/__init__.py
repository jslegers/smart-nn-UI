import sys
import os
from smartdiffusion.load import autoload

base_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.dirname(base_path)

sys.path.extend([
     os.path.join(src_path, "ComfyUI"),
])

import comfy


autoload(extra_objects = { "comfy" : comfy })
