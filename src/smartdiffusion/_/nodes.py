# sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), "smartdiffusion"))


from comfy import model_management
from load import module

from config import MAX_RESOLUTION


def before_node_execution():
    model_management.throw_exception_if_processing_interrupted()


def interrupt_processing(value=True):
    model_management.interrupt_current_processing(value)


NODE_CLASS_MAPPINGS = {}

NODE_DISPLAY_NAME_MAPPINGS = {}

EXTENSION_WEB_DIRS = {}

import os


def get_module_name(module_path: str) -> str:
    """
    Returns the module name based on the given module path.
    Examples:
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node.py") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node/") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node/__init__.py") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node/__init__") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node/__init__/") -> "my_custom_node"
        get_module_name("C:/Users/username/smartdiffusionserver/custom_nodes/my_custom_node.disabled") -> "custom_nodes
    Args:
        module_path (str): The path of the module.
    Returns:
        str: The module name.
    """
    base_path = os.path.basename(module_path)
    if os.path.isfile(module_path):
        base_path = os.path.splitext(base_path)[0]
    return base_path


import os
import sys
import traceback
import logging
import importlib
from types import ModuleType


def load_custom_node(
    module_path: str, ignore=set(), module_parent="custom_nodes"
) -> bool:
    module_name = os.path.basename(module_path)
    if os.path.isfile(module_path):
        sp = os.path.splitext(module_path)
        module_name = sp[0]
    try:
        logging.debug("Trying to load custom node {}".format(module_path))
        if os.path.isfile(module_path):
            module_spec = importlib.util.spec_from_file_location(
                module_name, module_path
            )
            module_dir = os.path.split(module_path)[0]
        else:
            module_spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(module_path, "__init__.py")
            )
            module_dir = module_path
        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)

        if (
            hasattr(module, "WEB_DIRECTORY")
            and getattr(module, "WEB_DIRECTORY") is not None
        ):
            web_dir = os.path.abspath(
                os.path.join(module_dir, getattr(module, "WEB_DIRECTORY"))
            )
            if os.path.isdir(web_dir):
                EXTENSION_WEB_DIRS[module_name] = web_dir
        if (
            hasattr(module, "NODE_CLASS_MAPPINGS")
            and getattr(module, "NODE_CLASS_MAPPINGS") is not None
        ):
            me = sys.modules[__name__]
            for name, node_cls in module.NODE_CLASS_MAPPINGS.items():
                if name not in ignore:
                    NODE_CLASS_MAPPINGS[name] = node_cls
                    cls = module.NODE_CLASS_MAPPINGS[name]
                    setattr(me, name, cls)
                    node_cls.RELATIVE_PYTHON_MODULE = "{}.{}".format(
                        module_parent, get_module_name(module_path)
                    )
            if (
                hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS")
                and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None
            ):
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
            return True
        else:
            logging.warning(
                f"Skip {module_path} module for custom nodes due to the lack of NODE_CLASS_MAPPINGS."
            )
            return False
    except Exception as e:
        logging.warning(traceback.format_exc())
        logging.warning(f"Cannot import {module_path} module for custom nodes: {e}")
        return False


import os
import time
import logging
import folder_paths


def init_external_custom_nodes():
    """
    Initializes the external custom nodes.

    This function loads custom nodes from the specified folder paths and imports them into the application.
    It measures the import times for each custom node and logs the results.

    Returns:
        None
    """
    base_node_names = set(NODE_CLASS_MAPPINGS.keys())
    node_paths = folder_paths.get_folder_paths("custom_nodes")
    node_import_times = []
    for custom_node_path in node_paths:
        possible_modules = os.listdir(os.path.realpath(custom_node_path))
        if "__pycache__" in possible_modules:
            possible_modules.remove("__pycache__")
        for possible_module in possible_modules:
            module_path = os.path.join(custom_node_path, possible_module)
            if (
                os.path.isfile(module_path)
                and os.path.splitext(module_path)[1] != ".py"
            ):
                continue
            if module_path.endswith(".disabled"):
                continue
            time_before = time.perf_counter()
            success = load_custom_node(
                module_path, base_node_names, module_parent="custom_nodes"
            )
            node_import_times.append(
                (time.perf_counter() - time_before, module_path, success)
            )
    if len(node_import_times) > 0:
        logging.info("\nImport times for custom nodes:")
        for n in sorted(node_import_times):
            if n[2]:
                import_message = ""
            else:
                import_message = " (IMPORT FAILED)"
            logging.info("{:6.1f} seconds{}: {}".format(n[0], import_message, n[1]))
        logging.info("")


import os


def init_builtin_nodes(*args):
    """
    Initializes the built-in nodes in Smart Diffusion Server.

    This function loads the extra node files located in the "nodes" and "extra_nodes" directories and import them into Smart Diffusion Server.
    If any of the extra node files fail to import, a warning message is logged.

    Returns:
        None
    """
    location = os.path.join(*args)
    extras_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), location
        )
    )
    extras_files = os.listdir(extras_dir)
    if "__pycache__" in extras_files:
        extras_files.remove("__pycache__")
    import_failed = []
    for node_file in extras_files:
        if not load_custom_node(
            os.path.join(extras_dir, node_file), module_parent=location
        ):
            import_failed.append(node_file)
    return import_failed


import logging


def init_extra_nodes(init_custom_nodes=True):
    if init_custom_nodes:
        init_external_custom_nodes()
    else:
        logging.info("Skipping loading of custom nodes")
