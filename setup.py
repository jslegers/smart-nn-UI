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
    python_requires=">=3.11.9",
    setup_requires=['setuptools_scm'],
    include_package_data = True,
    install_requires = [
        "torch>=2.3.1",
        "torchvision>=0.18.1",
        "torchaudio>=2.3.1",
        "bitsandbytes>=0.43.3",
        "transformers>=4.44.0",
        "tokenizers>=0.19.1",
        "safetensors>=0.4.4",
        "pyyaml>=6.0.2",
        "Pillow>=10.4.0",
        "scipy>=1.14.0",
        "accelerate>=0.33.0",
        "huggingface_hub>=0.24.5",
        "xformers>=0.0.27"
        "scipy>=1.14.0",
        "opencv-contrib-python>=4.10"
    ]
)
