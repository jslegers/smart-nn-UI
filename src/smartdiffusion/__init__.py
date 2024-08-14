import smartdiffusion
import sys
sys.modules["comfy"] = smartdiffusion
sys.modules["comfy_extras"] = smartdiffusion
smartdiffusion.load.add_to_env("SMARTDIFFUSION_PATH")
