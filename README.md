# 🔐 Custom File Integrity Monitoring (FIM) Tool

A lightweight, real-time, and modular File Integrity Monitoring (FIM) tool built with minimal dependencies. This tool helps detect unauthorized changes to critical files and directories by monitoring file system events and comparing cryptographic hashes.

---

## 📌 Project Goals

- **Lightweight & Minimal**: Designed for low-resource systems.
- **Real-Time Monitoring**: Event-driven file system tracking.
- **Modular Architecture**: Plugin-based design for easy extensions.
- **Educational Dashboard**: Integrity score and file change visualization (Phase 2).
- **Cross-Platform**: Compatible with Linux, Windows, and macOS (via `watchdog`).

---

## 🚀 Features

- SHA-256 based file hashing
- JSON-based baseline for file integrity
- Real-time event detection (create, modify, delete)
- Plugin support for alerts, logging, etc.
- CLI interface with commands like `init`, `monitor`, `check`
- (Planned) GUI/Web dashboard for visual integrity scoring

---

## 🗂️ Folder Structure

```
custom-fim-tool/
│
├── fim/                        # 🔧 Core FIM logic (modular, reusable)
│   ├── __init__.py
│   ├── baseline.py             # Step 1: Hashing & metadata
│   ├── monitor.py              # Step 2: Real-time event-based monitoring
│   ├── plugins.py              # Plugin loader and manager
│   ├── checker.py              # Manual integrity checker
│   └── utils.py                # Common helper functions
│
├── plugins/                   # 🔌 Custom user-defined plugins
│   └── example_plugin.py      # Sample plugin for demo
│
├── cli/                       # 🧰 CLI commands and interface
│   ├── __init__.py
│   └── main.py                # CLI entry point
│
├── gui/                       # 🖥️ (Optional) GUI/dashboard layer (future)
│   └── app.py                 # Flask/Tkinter interface (Phase 2)
│
├── tests/                     # ✅ Unit and integration tests
│   └── test_baseline.py
│
├── baseline.json              # 📄 Output file storing hashes/metadata
├── requirements.txt           # 📦 Dependencies (minimal)
├── README.md                  # 📘 Project description
├── .gitignore                 # 🚫 Files to exclude from git
└── run.py                     # 🔗 Main launcher (can route CLI or GUI)

```

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/custom-fim-tool.git
cd custom-fim-tool
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 CLI Usage

```bash
# Initialize a baseline hash of files
python run.py init /path/to/directory

# Start real-time monitoring
python run.py monitor

# Manually check for changes
python run.py check
```

> ⚠️ Real-time monitoring depends on the `watchdog` package (already included in `requirements.txt`).

---

## 🧩 Plugin System

- Add plugins in the `plugins/` folder.
- Each plugin must implement a `run(event_type, file_path)` function.
- Automatically loaded at runtime.

---

## 📊 Integrity Score (Planned)

A GUI or Web Dashboard will be added to:

- Visualize file events
- Show real-time integrity score
- Display logs and suspicious activity

---

## 🧠 Ideal Use Cases

- Monitoring sensitive configuration files
- Alerting on unauthorized file tampering
- Lightweight file security for servers or personal systems
- Educational cybersecurity demonstrations

---

## 📅 Project Roadmap

- [x] Baseline creation
- [x] Real-time event monitoring
- [x] Plugin system
- [ ] Manual integrity checker
- [ ] Educational GUI Dashboard
- [ ] Email/Telegram/Discord alert plugin

---

## 🙋‍♂️ Author

**Srujan Singh Rathod**  
👨‍💻 [GitHub](https://github.com/srujan-singh) • [LinkedIn](https://www.linkedin.com/in/srujan-singh-rathod-748182234/) • [Twitter](https://x.com/srujan_singh_)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

