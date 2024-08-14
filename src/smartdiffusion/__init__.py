from smartdiffusion import nodes, load
nodes.load_custom_node("trampoline", module_parent = None)
nodes.load_custom_node("torchsde", module_parent = None)
nodes.load_custom_node("latent_preview", module_parent = None)
nodes.load_custom_node("folder_paths", module_parent = None)
nodes.load_custom_node("node_helpers", module_parent = None)
nodes.load_custom_node("nodes", module_parent = None)
load.add_to_env("SMARTDIFFUSION_PATH")
