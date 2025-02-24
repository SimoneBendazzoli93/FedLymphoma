# MAIA-HPC

[MAIA-HPC](https://github.com/kthcloud/MAIA/tree/master/MAIA-HPC) is a toolkit to facilitate the use of HPC (High Performance Computing) resources for the training of deep learning models.

## nnUNet Training with MAIA-HPC
You first need to install MAIA-HPC. You can follow the instructions in the [MAIA-HPC repository](https://github.com/kthcloud/MAIA/tree/master/MAIA-HPC).
After the installation, you can configure your HPC server by running the following command:
```bash
configure_MAIA-HPC.sh
```
After configuring the HPC server, you can also import the nnUNet training experiment configuration by running the following command:
```bash
import_experiment.sh nnUNet_training.json
```

## Transfer Data and Singularity Image
After locally preprocessing the data with the nnUNet preprocessing pipeline, you can transfer the data to the HPC server by running the following command:
```bash
cd <nnUnet_root_dir>
ssh <server_name> mkdir -p /<project_dir>/Data/nnUNet
sftp <server_name>:/<project_dir>/Data/nnUNet
```
and then run the following command:
```bash
put -r * .
```
You can also transfer the Singularity image to the HPC server by running the following command:
```bash
sftp <server_name>:/<project_dir>
```

## Run nnUNet Training
After transferring the data and the Singularity image, you can then configure the training in MAIA-HPC by running:
```bash
edit_ssh_config.sh 
```
and adding the following lines:
```bash
[<server_name>]
EXPERIMENT_NAME=nnUNet_training
REMOTE_PATH=~/nnUNet
LOCAL_PATH=</path/to/repo>/nnUNet
```
And then you can run the following command to start the training:
```bash
submit_job.sh <server_name>
```

Monitor the training by running:
```bash
log_out.sh <server_name>
log_err.sh <server_name>
```
