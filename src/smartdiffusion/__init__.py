import sys
import os

base_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.dirname(base_path)

sys.path.extend([
     os.path.join(src_path, "ComfyUI"),
])

from comfy.utils import load_torch_file
