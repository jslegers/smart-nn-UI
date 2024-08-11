from smartdiffusion import sd
from smartdiffusion import folder_paths


class GLIGENLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {"gligen_name": (folder_paths.get_filename_list("gligen"),)}
        }

    RETURN_TYPES = ("GLIGEN",)
    FUNCTION = "load_gligen"

    CATEGORY = "loaders"

    def load_gligen(self, gligen_name):
        gligen_path = folder_paths.get_full_path("gligen", gligen_name)
        gligen = sd.load_gligen(gligen_path)
        return (gligen,)
