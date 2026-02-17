import os
from config import *
from deg_utils import download_deg, make_blast_db, run_blast, filter_essential
from localization_utils import run_psortb, filter_surface_proteins

def main():

    os.makedirs("data", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    print("Downloading DEG database...")
    download_deg(DEG_URL, DEG_FASTA)

    print("Creating BLAST database...")
    make_blast_db(DEG_FASTA)

    print("Running BLASTp vs DEG...")
    run_blast(INPUT_FASTA, EVALUE_THRESHOLD)

    print("Filtering essential proteins...")
    essential_fasta = filter_essential(INPUT_FASTA, EVALUE_THRESHOLD)

    print("Running PSORTb...")
    run_psortb(essential_fasta)

    print("Filtering surface-associated proteins...")
    final_fasta = filter_surface_proteins(essential_fasta, SURFACE_LOCATIONS)

    print("Pipeline complete.")
    print("Final file:", final_fasta)

if __name__ == "__main__":
    main()
