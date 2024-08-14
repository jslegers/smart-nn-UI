from smartdiffusion import nodes, load
extras_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
nodes.load_custom_node(os.path.join(extras_dir, "trampoline"), module_parent = None)
nodes.load_custom_node(os.path.join(extras_dir, "torchsde"), module_parent = None)
nodes.load_custom_node(os.path.join(extras_dir, "latent_preview"), module_parent = None)
nodes.load_custom_node(os.path.join(extras_dir, "folder_paths"), module_parent = None)
nodes.load_custom_node(os.path.join(extras_dir, "node_helpers"), module_parent = None)
nodes.load_custom_node(os.path.join(extras_dir, "nodes"), module_parent = None)
load.add_to_env("SMARTDIFFUSION_PATH")
