# FedLymphoma

**Federated Learning for PET/CT Lymphoma Lesion Segmentation**

This repository contains all the instructions and code for running the experiments of the project "Federated Learning for PET/CT Lymphoma Lesion Segmentation".


## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
5. [Results](#results)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)
8. [References](#references)




## Introduction

Lymphoma is a common type of cancer, and accurate segmentation of lymph nodes in PET-CT images is crucial for diagnosis, staging, and treatment planning. Deep learning (DL) models have demonstrated strong performance in medical image segmentation, but their success often relies on large, well-curated datasets. Given the sensitive nature of medical data, Federated Learning (FL) has emerged as a privacy-preserving solution that allows institutions to collaboratively train DL models without sharing patient data.

However, a major challenge in federated learning is managing data heterogeneity, particularly when different institutions use varying preprocessing strategies for PET-CT images. These variations can introduce inconsistencies that degrade the global model's performance. Therefore, optimizing the combination of preprocessing strategies from different clients to improve the global model's segmentation performance is crucial.

[nnUNet](https://github.com/MIC-DKFZ/nnUNet) is a state-of-the-art deep learning framework for medical image segmentation that has achieved strong performance on various datasets. In this project, we aim to develop a federated learning framework for PET/CT lymphoma lesion segmentation using nnUnet. We will leverage NVIDIA's [NVFlare](https://github.com/NVIDIA/NVFlare), a federated learning platform, to build a distributed DL model for lymphoma segmentation. The project will focus on determining how to harmonize and aggregate different preprocessing strategies from participating institutions to enhance generalization and improve the overall segmentation accuracy of the global model.


The main contributions of this project are:
- Developing a federated learning framework for PET/CT lymphoma lesion segmentation.
- Adapting nnUNet for federated learning.
- Investigate different nnUNet-based preprocessing techniques and propose a strategy to harmonize them in a federated learning setting.
- Evaluating the performance of the federated model on a multi-institutional dataset.


[MONAI](https://github.com/Project-MONAI/MONAI) is a PyTorch-based, open-source framework for deep learning in healthcare imaging that provides domain-optimized implementations of common medical imaging tasks. MONAI provides a complete eco-system for end-to-end deep learning experiments in healthcare imaging, including data loading, preprocessing, training, evaluation, visualization and model deployment. Among its features, MONAI Bundles are pre-configured, reusable components that simplify the process of building and training deep learning models. MONAI APIs are designed to seamlessly integrate MONAI Bundles with other components, such as MONAI Label for Active Learning, MONAI Deploy for model deployment, and MONAI Algo NVFlare for federated learning.

To adopt nnUNet for federated learning (specifically, NVFlare), we decided to adopt [MONAI](https://github.com/Project-MONAI/MONAI) as the main framework for the implementation. This is because MONAI provides a seamless integration between MONAI Bundles and NVFlare, which simplifies the process of adapting nnUNet for federated learning. Our additional contribution is to develop a MONAI Bundle for nnUNet that can be easily integrated with NVFlare for federated learning experiments.

## Dataset
[AutoPET](https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/) is a collection of annotated oncological PET/CT images. The dataset contains whole-body FDG-PET/CT scans of patients with various types of cancer, including lymphoma. The images are annotated with manually segmented tumor lesions, which can be used for training and evaluating deep learning models for lesion segmentation. The dataset is publicly available and can be downloaded from TCIA.

To know more about getting access to the dataset and preparing it for the experiments, please refer to the [AutoPET](AutoPET.ipynb) notebook.



## References
- https://arxiv.org/abs/2211.02701
- https://arxiv.org/abs/2210.13291
- Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring 
method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

- Gatidis S, Kuestner T. (2022) A whole-body FDG-PET/CT dataset with manually annotated tumor lesions (FDG-PET-CT-Lesions) [Dataset]. The Cancer Imaging Archive. DOI: 10.7937/gkr0-xv29 




