from smartdiffusion import nodes, load
nodes.init_builtin_nodes("latent_preview", no_parent = True)
nodes.init_builtin_nodes("node_helpers", no_parent = True)
nodes.init_builtin_nodes("torchsde", no_parent = True)
nodes.init_builtin_nodes("folder_paths", no_parent = True)
nodes.init_builtin_nodes("nodes", no_parent = True)
load.add_to_env("SMARTDIFFUSION_PATH")
