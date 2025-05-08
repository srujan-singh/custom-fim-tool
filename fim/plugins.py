import os
import importlib.util
from pathlib import Path

PLUGINS_DIR = Path("plugins")

def load_plugins():
    """Dynamically load all plugins in the 'plugins/' folder."""
    plugins = []

    if not PLUGINS_DIR.exists():
        print("[Plugin Loader] No plugins directory found.")
        return plugins

    for file in PLUGINS_DIR.glob("*.py"):
        if file.name.startswith("_"):
            continue

        spec = importlib.util.spec_from_file_location(file.stem, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "run"):
            plugins.append(module)
            print(f"[Plugin Loader] Loaded plugin: {file.name}")
        else:
            print(f"[Plugin Loader] Skipped {file.name} (no `run` function)")

    return plugins


def run_plugins(event_type, file_path):
    """Run all loaded plugins with event details."""
    plugins = load_plugins()
    for plugin in plugins:
        try:
            plugin.run(event_type, file_path)
        except Exception as e:
            print(f"[Plugin Error] {plugin.__name__}: {e}")
