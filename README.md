# SphericalProjection
Plane segmentation pipeline with spherical projection

# Data preparation

## Downloading dataset
[Download](http://www.cvlibs.net/download.php?file=data_odometry_velodyne.zip) Semantic Kitti dataset. 
You will need sequence **00**.

[Download](https://drive.google.com/drive/folders/17qZpTi3BYhQTHxlMwsNHf5QK8rCpmocL?usp=sharing)
EVOPS plane labels for Semantic Kitti dataset.

Put **velodyne** and **labels**  as well as evops labels renamed to **plane_labels** into one directory. 
In the end the directory with data should look like this.
```
├── labels
│   └── 000000.label
├── plane_labels
│   └── label-000000.npy
└── velodyne
    └── 000000.bin
```
You can find an example in `examples/data/kitti/00`. 

## Preparing dataset
The next step is running data preprocessing script. This can be done with the `preprocessing.py` script.
It takes the following parameters:
##### Required
- `--dataset` path to your dataset folder
- `--dataset_len` length of your dataset
- `--save_path` path to store ready to use data

#### Optional
By default, preprocessing applies ransac filtering and considers road labels as planes. However, you can change that.
- `--no_ransac` turns off ransac filtering
- `--no_road` road labels will not be considered as planes
- `--visualise_ransac` ransac filtering steps will be visualised

An example of preprocessing script run, applied to the data in **examples** directory:
> python3 preprocessing.py --dataset examples/data/kitti/00/ 
> --save_path examples/data/dataset_ready/ --dataset_len 1

# Training network

A train run is configured with a config file in a `.yaml` format. You can find an example in 
**runs_configs** directory. If you wish to train the network with your own parameters create a copy of an existing run 
and change the parameters you like. Don't forget to fill in your wandb project name(`wandb_project`), log in into wandb,
and dataset directory (`dataset_dir`).

After the run is configured you can run train with `run_network.py`. 
This script takes only one required parameter - path to your config file. Here is an example:

> python3 run_network --config runs_configs/exp1_basic.yaml
