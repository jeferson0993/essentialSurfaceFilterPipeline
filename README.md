### ▶️ Como Executar
- 1️⃣ Coloque o input aqui:
`data/ecoli_nonredundant.fasta`

- 2️⃣ Build
```sh
docker build -t phase2-pipeline .
```

- 3️⃣ Run
```sh
docker run -v $(pwd)/data:/app/data \
           -v $(pwd)/results:/app/results \
           phase2-pipeline
```

Ou:
```sh
docker-compose up --build
```

📊 Output Final
```sh
results/
│
├── query_vs_deg.xml
├── essential_proteins.fasta
├── psortb_results.txt
└── final_surface_essential.fasta
```
