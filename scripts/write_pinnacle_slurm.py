#! /usr/bin/env python3

print('#!/bin/bash')

print('#SBATCH --job-name=example')
print('#SBATCH --partition comp72')
print('#SBATCH --nodes=1')
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=72:00:00')
print('#SBATCH -o example_%j.out')
print('#SBATCH -e example_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=email@uark.edu)

module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1

cd $SLURM_SUBMIT_DIR

# job command here

