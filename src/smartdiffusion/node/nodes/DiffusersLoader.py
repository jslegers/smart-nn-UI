from os import path, walk
from safetensors.torch import load_file
from smartdiffusion.folder_paths import get_folder_paths
from smartdiffusion.diffusers_load import load_diffusers


class DiffusersLoader:
    @classmethod
    def INPUT_TYPES(cls):
        paths = []
        for search_path in get_folder_paths("diffusers"):
            if path.exists(search_path):
                for root, subdir, files in walk(search_path, followlinks=True):
                    if "model_index.json" in files:
                        paths.append(path.relpath(root, start=search_path))
        return {
            "required": {
                "model_path": (paths,),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "advanced/loaders/deprecated"

    def load_checkpoint(self, model_path, output_vae=True, output_clip=True):
        for search_path in get_folder_paths("diffusers"):
            if path.exists(search_path):
                full_path = path.join(search_path, model_path)
                if path.exists(full_path):
                    model_path = full_path
                    break
        return load_diffusers(
            model_path,
            output_vae=output_vae,
            output_clip=output_clip,
            embedding_directory=get_folder_paths("embeddings"),
        )

NODE_CLASS_MAPPINGS = {
    "DiffusersLoader": DiffusersLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Loaders
    "DiffusersLoader": "Load Diffusers Model (deprecated)",
}
