# FedLymphoma: Federated Learning for Lymphoma Segmentation

This repo contains the code and the instructions to connect to the FedLymphoma federation and train a federated model for lymphoma segmentation using nnUNet.

## Connect to the NVFlare Federation

To connect to the federation , you first need to install the `nvflare` package. You can install it using pip:

```bash
pip install nvflare
```

After receving your startup kit, save it under [StartupKit](./StartupKit/) and unzip it with the given password:

```bash
unzip -P <password> StartupKit/<username>.zip -d StartupKit/<username>
```

Then, you can connect to the federation using the following command:

```bash
StartupKit/<username>/startup/fl_admin.sh
```

Or follow the instructions in the [FedLymphoma](./FedLymphoma.ipynb) notebook.

## Start Clients in HPC

If the experiment is running in an HPC environment, you can start the clients using the following command:

```bash
submit_job.sh <HPC>
```

Don't forget to replace `<HPC>` with the name of the HPC environment you are using and configure the ssh_config file with the correct information:

```bash
edit_ssh_config.sh

[<HPC>-client]
EXPERIMENT_NAME=<experiment_name>
REMOTE_PATH=FedLymphoma/FedLymphoma/<HPC>-Client
LOCAL_PATH=/path/to/FedLymphoma/FedLymphoma/<HPC>-Client
```

Also, remember to import the experiment to your MAIA HPC environment:

```bash
cd FedLymphoma/<HPC>-Client
import_experiment.sh <experiment_name>.json
```