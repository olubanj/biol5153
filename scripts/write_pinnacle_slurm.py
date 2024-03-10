#!/bin/bash

#SBATCH --job-name=example
#SBATCH --partition comp72
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=32
#SBATCH --time=72:00:00
#SBATCH -o example_%j.out
#SBATCH -e example_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=email@uark.edu

module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1

cd $SLURM_SUBMIT_DIR

# job command here

