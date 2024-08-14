from smartdiffusion import nodes, load
nodes.load_custom_node("trampoline", no_parent = True)
nodes.load_custom_node("torchsde", no_parent = True)
nodes.load_custom_node("latent_preview", no_parent = True)
nodes.load_custom_node("folder_paths", no_parent = True)
nodes.load_custom_node("node_helpers", no_parent = True)
nodes.load_custom_node("nodes", no_parent = True)
load.add_to_env("SMARTDIFFUSION_PATH")
