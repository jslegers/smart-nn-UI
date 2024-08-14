class VAEEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"pixels": ("IMAGE",), "vae": ("VAE",)}}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "encode"

    CATEGORY = "latent"

    def encode(self, vae, pixels):
        return ({"samples": vae.encode(pixels[:, :, :, :3])},)

NODE_CLASS_MAPPINGS = {
    "VAEEncode": VAEEncode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VAEEncode": "VAE Encode",
}