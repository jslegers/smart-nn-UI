from comfy.controlnet import load_controlnet as c_load_controlnet
from folder_paths import get_full_path, get_filename_list


class ControlNetLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"control_net_name": (get_filename_list("controlnet"),)}}

    RETURN_TYPES = ("CONTROL_NET",)
    FUNCTION = "load_controlnet"

    CATEGORY = "loaders"

    def load_controlnet(self, control_net_name):
        return (c_load_controlnet(get_full_path("controlnet", control_net_name)),)

NODE_CLASS_MAPPINGS = {
    "ControlNetLoader": ControlNetLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Loaders
    "ControlNetLoader": "Load ControlNet Model",
}
