from pathlib import Path
from test.fonctions_extraction_md import load_markdown_with_yaml

md_path = Path("data/docs_markdown/Commande Cuisine.md")

metadata, body = load_markdown_with_yaml(md_path)
print("Metadata extracted:")
print(metadata)
print("\nBody content:")
print(body)
print("\n---\n")
