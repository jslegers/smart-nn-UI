from smartdiffusion import sd
from smartdiffusion import folder_paths

class CLIPLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_name": (folder_paths.get_filename_list("clip"), ),
                              "type": (["stable_diffusion", "stable_cascade", "sd3", "stable_audio"], ),
                             }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "load_clip"

    CATEGORY = "advanced/loaders"

    def load_clip(self, clip_name, type="stable_diffusion"):
        if type == "stable_cascade":
            clip_type = sd.CLIPType.STABLE_CASCADE
        elif type == "sd3":
            clip_type = sd.CLIPType.SD3
        elif type == "stable_audio":
            clip_type = sd.CLIPType.STABLE_AUDIO
        else:
            clip_type = sd.CLIPType.STABLE_DIFFUSION

        clip_path = folder_paths.get_full_path("clip", clip_name)
        clip = sd.load_clip(ckpt_paths=[clip_path], embedding_directory=folder_paths.get_folder_paths("embeddings"), clip_type=clip_type)
        return (clip,)
