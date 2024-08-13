from torch import float8_e4m3fn, float8_e5m2
from smartdiffusion.sd import load_diffusion_model
from smartdiffusion.folder_paths import get_full_path, get_filename_list


class UNETLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "unet_name": (get_filename_list("unet"),),
                "weight_dtype": (["default", "fp8_e4m3fn", "fp8_e5m2"],),
            }
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "load_unet"

    CATEGORY = "advanced/loaders"

    def load_unet(self, unet_name, weight_dtype):
        model_options = {}
        if weight_dtype == "fp8_e4m3fn":
            model_options["dtype"] = float8_e4m3fn
        elif weight_dtype == "fp8_e5m2":
            model_options["dtype"] = float8_e5m2

        unet_path = folder_paths.get_full_path("unet", unet_name)
        model = load_diffusion_model(unet_path, model_options=model_options)
        return (model,)
