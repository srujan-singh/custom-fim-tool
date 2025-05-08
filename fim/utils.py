import hashlib
import json
from pathlib import Path


def hash_file(file_path, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def load_json(file_path):
    if not Path(file_path).exists():
        return {}
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def is_text_file(file_path):
    try:
        with open(file_path, "r") as f:
            f.read()
        return True
    except:
        return False
