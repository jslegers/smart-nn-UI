from smartdiffusion import sd
from smartdiffusion import folder_paths

class DualCLIPLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_name1": (folder_paths.get_filename_list("clip"), ),
                              "clip_name2": (folder_paths.get_filename_list("clip"), ),
                              "type": (["sdxl", "sd3", "flux"], ),
                             }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "load_clip"

    CATEGORY = "advanced/loaders"

    def load_clip(self, clip_name1, clip_name2, type):
        clip_path1 = folder_paths.get_full_path("clip", clip_name1)
        if type == "sdxl":
            clip_type = sd.CLIPType.STABLE_DIFFUSION
            clip_path2 = folder_paths.get_full_path("clip", clip_name2)
        elif type == "sd3":
            clip_type = sd.CLIPType.SD3
            clip_path2 = folder_paths.get_full_path("t5", clip_name2)
        elif type == "flux":
            clip_type = sd.CLIPType.FLUX
            clip_path2 = folder_paths.get_full_path("t5", clip_name2)

        clip = sd.load_clip(ckpt_paths=[clip_path1, clip_path2], embedding_directory=folder_paths.get_folder_paths("embeddings"), clip_type=clip_type)
        return (clip,)
