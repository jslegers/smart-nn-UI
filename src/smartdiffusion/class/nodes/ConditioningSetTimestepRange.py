from smartdiffusion import node_helpers


class ConditioningSetTimestepRange:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
                "start": (
                    "FLOAT",
                    {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.001},
                ),
                "end": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.001},
                ),
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "set_range"

    CATEGORY = "advanced/conditioning"

    def set_range(self, conditioning, start, end):
        c = node_helpers.conditioning_set_values(
            conditioning, {"start_percent": start, "end_percent": end}
        )
        return (c,)
