from comfy.controlnet import load_controlnet
from folder_paths import get_filename_list, get_full_path


class DiffControlNetLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "control_net_name": (get_filename_list("controlnet"),),
            }
        }

    RETURN_TYPES = ("CONTROL_NET",)
    FUNCTION = "load_controlnet"

    CATEGORY = "loaders"

    def load_controlnet(self, model, control_net_name):
        return (load_controlnet(get_full_path("controlnet", control_net_name), model),)

NODE_CLASS_MAPPINGS = {
    "DiffControlNetLoader": DiffControlNetLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Loaders
    "DiffControlNetLoader": "Load ControlNet Model (diff)",
}