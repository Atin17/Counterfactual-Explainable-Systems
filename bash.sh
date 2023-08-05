#!/bin/bash -l
#SBATCH --output=/common/home/ps1279/PycharmProjects/pythonProject/counter/logfile
#SBATCH -o /common/home/ps1279/PycharmProjects/pythonProject/counter/yelp.txt

export PATH="$PATH:/koko/system/anaconda/bin"
source activate python39



cd /common/home/ps1279/PycharmProjects/pythonProject/counter
source setup.sh



python scripts/train_base_yelp.py
python scripts/generate_exp_yelp.py