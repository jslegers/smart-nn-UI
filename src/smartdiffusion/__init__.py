from smartdiffusion import nodes, load
nodes.init_builtin_nodes("latent_preview.py", no_parent = True)
nodes.init_builtin_nodes("node_helpers.py", no_parent = True)
nodes.init_builtin_nodes("torchsde", no_parent = True)
nodes.init_builtin_nodes("folder_paths.py", no_parent = True)
nodes.init_builtin_nodes("nodes.py", no_parent = True)
load.add_to_env("SMARTDIFFUSION_PATH")
