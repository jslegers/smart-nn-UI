from comfy.sd import load_gligen
from folder_paths import get_full_path, get_filename_list


class GLIGENLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"gligen_name": (get_filename_list("gligen"),)}}

    RETURN_TYPES = ("GLIGEN",)
    FUNCTION = "load_gligen"

    CATEGORY = "loaders"

    def load_gligen(self, gligen_name):
        return (load_gligen(get_full_path("gligen", gligen_name)),)

NODE_CLASS_MAPPINGS = {
    "GLIGENLoader": GLIGENLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Loaders
    "GLIGENLoader": "GLIGEN Loader",
}