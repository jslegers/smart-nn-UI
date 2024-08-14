#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

setup(
    name = "smartdiffusion",
    version = "0.0.4",
    description = "A library for making it easier to work with neural networks",
    long_description = "A library for making it easier to work with neural networks",
    url ="https://github.com/jslegers/smartdiffusion",
    author ="John Slegers",
    license = "GNU v3",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    python_requires=">=3.8.0",
    setup_requires=['setuptools_scm'],
    include_package_data = True,
    install_requires = [
        "torch>=2.3.1",
        "torchsde>=0.2.6",
        "torchvision>=0.18.1",
        "torchaudio>=2.3.1",
        "bitsandbytes>=0.43.3"
        "einops>=0.8.0",
        "transformers>=4.28.1",
        "tokenizers>=0.13.3",
        "sentencepiece",
        "safetensors>=0.4.2",
        "pyyaml>=6.0.2",
        "Pillow>=10.4.0",
        "scipy>=1.14.0",
        "tqdm>=4.66.5",
        "psutil>=6.0.0",
        "accelerate>=0.33.0",
        "huggingface_hub>=0.24.5",
        "xformers>=0.0.26"
    ]
)
