class ImageInvert:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "invert"

    CATEGORY = "image"

    def invert(self, image):
        return (1.0 - image,)

NODE_CLASS_MAPPINGS = {
    "ImageInvert": ImageInvert
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageInvert": "Invert Image",
}
