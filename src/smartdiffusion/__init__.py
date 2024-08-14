from smartdiffusion.load import add_to_env
import sys
sys.modules["comfy"] = smartdiffusion
sys.modules["comfy_extras"] = smartdiffusion
add_to_env("SMARTDIFFUSION_PATH")
