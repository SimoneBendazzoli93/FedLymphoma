#!/usr/bin/env python

import os
from monai.apps.nnunet import nnUNetV2Runner
import argparse



def train(data_src_cfg, nnunet_root_dir, fold=0):
    """
    Trains a neural network model using the nnUNet framework.
    
    Parameters
    ----------
    data_src_cfg : dict
        Configuration dictionary for the data source.
    nnunet_root_dir : str
        Root directory for nnUNet.
    fold : int, optional
        Fold number for cross-validation (default is 0).
    
    Returns
    -------
    None
    """

    runner = nnUNetV2Runner(
        input_config=data_src_cfg, trainer_class_name="nnUNetTrainer", work_dir=nnunet_root_dir
    )
    
    runner.train_single_model(config="3d_fullres", fold=fold)
    
def get_arg_parser():
    
    parser = argparse.ArgumentParser(description='Train a model using the nnUNet framework.')
    parser.add_argument('--nnunet-root-dir', type=str, required=True, help='Root directory for nnUNet.')
    parser.add_argument('--fold', type=int, default=0, help='Fold number for cross-validation.')
    
    return parser
    
    
def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    nnunet_root_dir = args.nnunet_root_dir
    fold = args.fold
    data_src_cfg = os.path.join(nnunet_root_dir, "data_src_cfg.yaml")

    train(data_src_cfg, nnunet_root_dir, fold=fold)
    