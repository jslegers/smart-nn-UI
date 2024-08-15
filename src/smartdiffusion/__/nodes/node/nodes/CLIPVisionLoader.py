from comfy.clip_vision import load
from folder_paths import get_full_path, get_filename_list


class CLIPVisionLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"clip_name": (get_filename_list("clip_vision"),)}}

    RETURN_TYPES = ("CLIP_VISION",)
    FUNCTION = "load_clip"

    CATEGORY = "loaders"

    def load_clip(self, clip_name):
        return (load(get_full_path("clip_vision", clip_name)),)

NODE_CLASS_MAPPINGS = {
    "CLIPVisionLoader": CLIPVisionLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Loaders
    "CLIPVisionLoader": "Load CLIP Vision",
}
