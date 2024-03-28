print("#!/bin/bash")

print("# Define paths")
print("gff_file_path = '../watermelon/watermelon.gff'")
print("cds_file_path = 'watermelon.gbf'  
print()

print("# Your SLURM directives here...")
print("#SBATCH --job-name=example")
print("#SBATCH --partition comp72")
print("#SBATCH --nodes=1")
print("#SBATCH --qos comp")
print("#SBATCH --tasks-per-node=32")
print("#SBATCH --time=00:30:00  o
print("#SBATCH -o example_%j.out")
print("#SBATCH -e example_%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=olubanjo@uark.edu")
print()

print("# Load necessary modules (if needed)")
print("module purge")
print("module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")
print()

print("# Navigate to the directory containing the Python script")
print("cd ~/Desktop/biol5153/scripts/")
print()

print("# Run the Python script to process the GFF file and generate the GBF file")
print("python3 write_pinnacle_slurm.py \"$gff_file_path\" \"$cds_file_path\"")
