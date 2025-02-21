import hpccm

Stage0 += baseimage(image='nvcr.io/nvidia/pytorch:23.10-py3')
Stage0 += gnu()
Stage0 += pip(ospackages=[""], packages=[
                                         "monai[all]",
                                         "nnunetv2==2.5.1",
                                         "jupyter",
                                         "fire",
                                         "jupyterlab"
                                         ])
Stage0 += runscript(commands=[''])

