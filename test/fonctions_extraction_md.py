from pathlib import Path
import yaml

def load_markdown_with_yaml(path):
    path = Path(path)
    text = path.read_text(encoding="utf-8")

    if text.lstrip().startswith("---"):
        parts = text.split("---", 2)
        fm_text = parts[1]
        body = parts[2]
        metadata = yaml.safe_load(fm_text) or {}
    else:
        metadata = {}
        body = text

    # Valeurs par défaut si certains champs manquent
    if "id" not in metadata:
        metadata["id"] = path.stem

    if "title" not in metadata:
        # Essaye de prendre la première ligne commençant par "# "
        first_line = body.splitlines()[0] if body else ""
        if first_line.startswith("# "):
            metadata["title"] = first_line[2:].strip()
        else:
            metadata["title"] = path.stem

    if "application" not in metadata:
        metadata["application"] = "unknown"

    if "module" not in metadata:
        metadata["module"] = "unknown"

    if "language" not in metadata:
        metadata["language"] = "fr"

    body = body.strip()
    return metadata, body

