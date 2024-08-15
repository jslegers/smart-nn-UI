from random import choice
from folder_paths import get_temp_directory
import load
SaveImage = load.module("smartdiffusion").SaveImage


class PreviewImage(SaveImage):
    def __init__(self):
        self.output_dir = get_temp_directory()
        self.type = "temp"
        self.prefix_append = "_temp_" + "".join(
            choice("abcdefghijklmnopqrstupvxyz") for x in range(5)
        )
        self.compress_level = 1

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

NODE_CLASS_MAPPINGS = {
    "PreviewImage": PreviewImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PreviewImage": "Preview Image",
}
