# AccuKnox AI/ML Trainee — Assignment Solutions

Solutions to Problem Statement 1 of the AccuKnox AI/ML Trainee assessment.

## Contents

| File | Description |
|---|---|
| `ps1_sol_1.py` | Fetches books data (title, author, publication year) from the Open Library public API, stores it in a local SQLite DB, and displays the records. |
| `ps1_sol_2.py` | Calculates each student's average test score across subjects and visualizes the results as a bar chart. **Note:** no publicly available REST API serving student test score data in this format was found; a  mock dataset is used for visualization, as documented in the script. |
| `ps1_sol_3.py` | Reads user data (`users.csv`) and inserts it into a local SQLite DB. |
| `users.csv` | Sample user data used by `ps1_sol_3.py`. |

## How to Run

Each script is self-contained. From this folder:

```bash
pip install requests matplotlib
python ps1_sol_1.py
python ps1_sol_2.py
python ps1_sol_3.py
```

`sqlite3` and `csv` are part of Python's standard library and require no installation.

## Additional Work

- **Most complex Python code:** [HyRAG](https://github.com/Zeus0source/hyrag) — a hybrid-search Retrieval Augmented Generation system combining semantic vector search (ChromaDB) with BM25 keyword search over RBI financial regulatory documents, built from first principles without high-level RAG frameworks.
- **Most complex database code:** [HyRAG's ingestion pipeline](https://github.com/Zeus0source/hyrag/blob/main/ingest.py) — PDF chunking, embedding generation, and vector database storage using ChromaDB.

---

Yash Rastogi