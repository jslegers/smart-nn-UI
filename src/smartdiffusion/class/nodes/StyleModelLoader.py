from smartdiffusion import sd
from smartdiffusion import folder_paths

class StyleModelLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "style_model_name": (folder_paths.get_filename_list("style_models"), )}}

    RETURN_TYPES = ("STYLE_MODEL",)
    FUNCTION = "load_style_model"

    CATEGORY = "loaders"

    def load_style_model(self, style_model_name):
        style_model_path = folder_paths.get_full_path("style_models", style_model_name)
        style_model = sd.load_style_model(style_model_path)
        return (style_model,)
