import subprocess
import requests
import os
from Bio import SearchIO, SeqIO

def download_deg(url, output_path):
    if not os.path.exists(output_path):
        subprocess.run(["wget", "-O", "deg.gz", url], check=True)
        subprocess.run(["gunzip", "-f", "deg.gz"], check=True)
        subprocess.run(["mv", "DEG10.aa", output_path], check=True)

def make_blast_db(fasta_file):
    subprocess.run([
        "makeblastdb",
        "-in", fasta_file,
        "-dbtype", "prot",
        "-out", "deg_db"
    ], check=True)

def run_blast(query_fasta, evalue):
    subprocess.run([
        "blastp",
        "-query", query_fasta,
        "-db", "deg_db",
        "-out", "results/query_vs_deg.xml",
        "-outfmt", "5",
        "-evalue", str(evalue)
    ], check=True)

def filter_essential(query_fasta, evalue):
    essential_ids = set()

    for qresult in SearchIO.parse("results/query_vs_deg.xml", "blast-xml"):
        if qresult.hits:
            essential_ids.add(qresult.id)

    essential_records = [
        record for record in SeqIO.parse(query_fasta, "fasta")
        if record.id in essential_ids
    ]

    output_path = "results/essential_proteins.fasta"
    SeqIO.write(essential_records, output_path, "fasta")

    return output_path
