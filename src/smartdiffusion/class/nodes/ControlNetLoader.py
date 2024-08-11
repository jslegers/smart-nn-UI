from smartdiffusion import controlnet
from smartdiffusion import folder_paths


class ControlNetLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "control_net_name": (folder_paths.get_filename_list("controlnet"),)
            }
        }

    RETURN_TYPES = ("CONTROL_NET",)
    FUNCTION = "load_controlnet"

    CATEGORY = "loaders"

    def load_controlnet(self, control_net_name):
        controlnet_path = folder_paths.get_full_path("controlnet", control_net_name)
        controlnet = controlnet.load_controlnet(controlnet_path)
        return (controlnet,)