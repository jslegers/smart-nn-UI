class VAEDecode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"samples": ("LATENT",), "vae": ("VAE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "decode"

    CATEGORY = "latent"

    def decode(self, vae, samples):
        return (vae.decode(samples["samples"]),)

NODE_CLASS_MAPPINGS = {
    "VAEDecode": VAEDecode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VAEDecode": "VAE Decode",
}
