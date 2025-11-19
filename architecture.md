chat_bot_isosl/
├─ README.md
├─ .gitignore
├─ requirements.txt        # ou pyproject.toml si tu passes à poetry plus tard
├─ src/
│  └─ app/
│     ├─ __init__.py
│     ├─ main.py           # point d'entrée (api ou interface console)
│     ├─ config.py         # configs générales (chemins, options)
│     ├─ models/           # classes pydantic, schémas, DTO
│     ├─ services/         # logique métier
│     │  ├─ ingestion/     # ingestion PDF
│     │  ├─ search/        # recherche, RAG
│     │  └─ summarization/ # résumés de procédures
│     └─ adapters/         # interfaces vers l’extérieur (fichiers, DB, intranet)
│        ├─ filesystem.py
│        └─ vector_store.py
├─ data/
│  ├─ raw_procedures/      # PDF bruts (attention RGPD: pas de patients)
│  ├─ processed/           # textes extraits, nettoyés
│  └─ indexes/             # index/vectorstore locaux (FAISS, Chroma…)
├─ notebooks/              # exploration, POC, tests rapides
├─ scripts/
│  ├─ ingest_pdfs.py       # script CLI pour ingérer les PDF
│  └─ build_index.py       # création / mise à jour de l’index
└─ tests/
   ├─ test_ingestion.py
   └─ test_search.py
