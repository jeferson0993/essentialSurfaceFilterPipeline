import subprocess
import pandas as pd
from Bio import SeqIO

def run_psortb(input_fasta):
    subprocess.run([
        "psortb",
        "-i", input_fasta,
        "-o", "terse",
        "-r", "results/psortb_results.txt"
    ], check=True)

def filter_surface_proteins(input_fasta, surface_locations):
    psort = pd.read_csv("results/psortb_results.txt", sep="\t")

    surface_df = psort[psort["Localization"].isin(surface_locations)]
    surface_ids = set(surface_df["SeqID"])

    final_records = [
        record for record in SeqIO.parse(input_fasta, "fasta")
        if record.id in surface_ids
    ]

    output_path = "results/final_surface_essential.fasta"
    SeqIO.write(final_records, output_path, "fasta")

    return output_path
