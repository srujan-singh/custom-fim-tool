from pathlib import Path
from fim.utils import hash_file, load_json

def check_integrity(directory, baseline_path="baseline.json"):
    print("[Checker] Comparing current state with baseline...")

    baseline_data = load_json(baseline_path)
    current_files = {}

    for file_path in Path(directory).rglob("*"):
        if file_path.is_file():
            try:
                current_files[str(file_path)] = hash_file(file_path)
            except Exception as e:
                print(f"[Checker] Error hashing {file_path}: {e}")

    modified = []
    deleted = []
    new_files = []

    for path in baseline_data:
        if path not in current_files:
            deleted.append(path)
        elif current_files[path] != baseline_data[path]:
            modified.append(path)

    for path in current_files:
        if path not in baseline_data:
            new_files.append(path)

    print("\n[Integrity Report]")
    print(f"🟥 Modified Files: {len(modified)}")
    for f in modified: print(f"  - {f}")

    print(f"🟨 Deleted Files: {len(deleted)}")
    for f in deleted: print(f"  - {f}")

    print(f"🟩 New Files: {len(new_files)}")
    for f in new_files: print(f"  - {f}")
