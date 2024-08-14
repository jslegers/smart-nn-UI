class SetLatentNoiseMask:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "samples": ("LATENT",),
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "set_mask"

    CATEGORY = "latent/inpaint"

    def set_mask(self, samples, mask):
        s = samples.copy()
        s["noise_mask"] = mask.reshape((-1, 1, mask.shape[-2], mask.shape[-1]))
        return (s,)

NODE_CLASS_MAPPINGS = {
    "SetLatentNoiseMask": SetLatentNoiseMask
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SetLatentNoiseMask": "Set Latent Noise Mask",
}
