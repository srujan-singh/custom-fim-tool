import os
import hashlib
import json

def hash_file(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def generate_baseline(directory):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = hash_file(path)
            if file_hash:
                baseline[path] = file_hash

    with open("baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)
    
    print(f"✅ Baseline created for directory: {directory}")
