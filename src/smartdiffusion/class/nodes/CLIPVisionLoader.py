from smartdiffusion import clip_vision
from smartdiffusion import folder_paths

class CLIPVisionLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_name": (folder_paths.get_filename_list("clip_vision"), ),
                             }}
    RETURN_TYPES = ("CLIP_VISION",)
    FUNCTION = "load_clip"

    CATEGORY = "loaders"

    def load_clip(self, clip_name):
        clip_path = folder_paths.get_full_path("clip_vision", clip_name)
        clip_vision = clip_vision.load(clip_path)
        return (clip_vision,)
