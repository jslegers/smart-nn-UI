class CLIPVisionEncode:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"clip_vision": ("CLIP_VISION",), "image": ("IMAGE",)}}

    RETURN_TYPES = ("CLIP_VISION_OUTPUT",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip_vision, image):
        return (clip_vision.encode_image(image),)
