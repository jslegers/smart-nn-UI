from folder_paths import get_filename_list
from comfy import LoraLoader


class LoraLoaderModelOnly(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "lora_name": (get_filename_list("loras"),),
                "strength_model": (
                    "FLOAT",
                    {"default": 1.0, "min": -100.0, "max": 100.0, "step": 0.01},
                ),
            }
        }

    RETURN_TYPES = ("MODEL",)
    FUNCTION = "load_lora_model_only"

    def load_lora_model_only(self, model, lora_name, strength_model):
        return (self.load_lora(model, None, lora_name, strength_model, 0)[0],)

NODE_CLASS_MAPPINGS = {
    "LoraLoaderModelOnly": LoraLoaderModelOnly
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraLoaderModelOnly": "Load Lora (Model only)",
}
