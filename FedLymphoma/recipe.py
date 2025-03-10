#!/usr/bin/env python
import hpccm


#rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_1.13.1
Stage0 += baseimage(image='nvcr.io/nvidia/pytorch:23.10-py3')
Stage0 += gnu()
Stage0 += pip(ospackages=[""], packages=[
                                         "nvflare",
                                         "jupyter",
                                         "jupyterlab",
                                         ])
Stage0 += runscript(commands=[''])