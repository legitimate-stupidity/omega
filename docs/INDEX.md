# Project OMEGA v4.0 - Quick Navigation Guide

## 📋 Start Here

### For New Users
1. **First Time?** → Read `README.md`
2. **Want to Install?** → Follow `docs/SETUP.md`
3. **Ready to Run?** → `python omega.py`

### For Developers
1. **Understand Architecture?** → Read `docs/ARCHITECTURE.md`
2. **Module Reference?** → Check `docs/MODULES.md`
3. **Adding New Code?** → See Architecture guide for patterns

### For Understanding the Code
1. **Module Overview** → `docs/MODULES.md` - Complete reference
2. **Design Patterns** → `docs/ARCHITECTURE.md` - Principles & patterns
3. **Full Summary** → `docs/COMPLETION_SUMMARY.md` - What was done

---

## 📁 Project Structure

```
omega/                              # Root directory
├── src/                           # Main source code
│   ├── __init__.py               # Package initialization
│   ├── utils/                    # Utilities (output formatting)
│   ├── core/                     # Core infrastructure
│   │   ├── dependencies.py       # Dynamic imports
│   │   ├── database.py           # SQLite operations
│   │   ├── opsec.py              # Security features
│   │   └── exploiter.py          # HTTP base class
│   ├── repositories/             # Data storage
│   │   └── data_repository.py   # VKB, shellcodes, agents
│   ├── modules/                  # Offensive modules
│   │   ├── evasion/              # Evasion techniques
│   │   ├── offensive/            # Network attacks
│   │   └── exploitation/         # Web exploitation
│   └── agent/                    # CLI interface
│       ├── agent.py              # Interactive shell
│       └── session.py            # Session management
├── config/                       # Configuration
│   └── config.py                # All settings in one place
├── docs/                         # Documentation (5 guides)
│   ├── ARCHITECTURE.md          # Detailed architecture
│   ├── MODULES.md               # Module reference
│   ├── SETUP.md                 # Installation & setup
│   ├── COMPLETION_SUMMARY.md    # What was accomplished
│   └── INDEX.md                 # This file
├── tests/                        # Test directory (ready)
├── omega.py                     # Main entry point
├── requirements.txt             # Python dependencies
├── README.md                    # Project overview
└── LICENSE                      # License
```

---

## 📚 Documentation Index

### Main Documentation Files

| File | Purpose | Length | Audience |
|------|---------|--------|----------|
| `README.md` | Project overview & features | 400 lines | Everyone |
| `ARCHITECTURE.md` | Complete architecture guide | 500 lines | Developers |
| `MODULES.md` | Module reference & examples | 600 lines | Developers |
| `SETUP.md` | Installation & configuration | 400 lines | Users |
| `COMPLETION_SUMMARY.md` | What was accomplished | 300 lines | Project managers |

### Quick Links by Purpose

**"How do I..."** Questions:

- **...get started?**
  → `README.md` Quick Start section

- **...install OMEGA?**
  → `docs/SETUP.md` Installation Steps

- **...use the CLI?**
  → `README.md` Commands section

- **...use OMEGA in code?**
  → `docs/MODULES.md` Quick Reference

- **...extend with new modules?**
  → `docs/ARCHITECTURE.md` Adding New Modules

- **...configure settings?**
  → `config/config.py` with `docs/ARCHITECTURE.md`

- **...understand the design?**
  → `docs/ARCHITECTURE.md` Architecture Principles

- **...find a specific module?**
  → `docs/MODULES.md` Module Inventory

---

## 🔧 Core Modules (13 Total)

### Utilities (1)
- **output.py** - Terminal formatting and colors

### Core (4)
- **dependencies.py** - Dependency management
- **database.py** - SQLite operations (4 tables)
- **opsec.py** - User agent rotation, proxies
- **exploiter.py** - HTTP exploitation base

### Repositories (1)
- **data_repository.py** - VKB (2000 CVEs), Shellcodes (1000+), User Agents (500+)

### Offensive (3)
- **advanced_evasion.py** - Memory manipulation, anti-debug, anti-VM
- **volumetric_attacks.py** - SYN flood, UDP flood
- **exploit_framework.py** - Web exploits (SQL injection, XSS, traversal)

### Agent (2)
- **session.py** - Session state management
- **agent.py** - Interactive CLI interface

### Configuration (1)
- **config.py** - Centralized configuration

---

## 🚀 Quick Start

### Installation
```bash
cd omega
pip install -r requirements.txt
python omega.py
```

### Basic Usage
```
OMEGA> set target 192.168.1.1
OMEGA(192.168.1.1)> attack syn 80 10
OMEGA(192.168.1.1)> list vkb
OMEGA(192.168.1.1)> exit
```

### In Python Code
```python
from src.modules import VolumetricAttackSimulation
volumetric = VolumetricAttackSimulation()
volumetric.syn_flood.launch_attack('192.168.1.1', 80)
```

---

## 📖 Reading Order Recommendations

### For Beginners
1. `README.md` - Get overview
2. `docs/SETUP.md` - Install
3. Try CLI commands in `README.md`
4. `docs/MODULES.md` - Learn APIs

### For Developers
1. `README.md` - Overview
2. `docs/ARCHITECTURE.md` - Design
3. `docs/MODULES.md` - Reference
4. `config/config.py` - Settings
5. Source code in `src/` - Implementation

### For Project Managers
1. `docs/COMPLETION_SUMMARY.md` - What was done
2. `README.md` - Features
3. `docs/ARCHITECTURE.md` - Quality metrics

---

## 🎯 Common Tasks

### Task: Find a Module
**Answer:** Check `docs/MODULES.md` Module Inventory (Table of all 13 modules)

### Task: Use VKB Data
**Answer:** See `docs/MODULES.md` Section 6 - Data Repository

### Task: Launch Attack
**Answer:** See `README.md` Programmatic Usage or try CLI

### Task: Add New Module
**Answer:** Follow `docs/ARCHITECTURE.md` - Adding New Modules section

### Task: Configure Settings
**Answer:** Edit `config/config.py` and refer to `docs/ARCHITECTURE.md`

### Task: Understand OPSEC
**Answer:** See `docs/MODULES.md` Section 4 - OPSEC Management

### Task: Database Operations
**Answer:** See `docs/MODULES.md` Section 3 - Database

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 38 |
| **Python Modules** | 17 |
| **Classes** | 25+ |
| **Functions** | 150+ |
| **Lines of Code** | ~3,500 |
| **Documentation Lines** | 1,900+ |
| **Docstrings** | 200+ |
| **CVE Entries** | 2,000 |
| **Shellcode Payloads** | 1,000+ |
| **User Agents** | 500+ |

---

## 🔗 File Cross-References

### By Module Name
- **output** → `src/utils/output.py` (docs: `MODULES.md` §1)
- **dependencies** → `src/core/dependencies.py` (docs: `MODULES.md` §2)
- **database** → `src/core/database.py` (docs: `MODULES.md` §3)
- **opsec** → `src/core/opsec.py` (docs: `MODULES.md` §4)
- **exploiter** → `src/core/exploiter.py` (docs: `MODULES.md` §5)
- **data_repository** → `src/repositories/data_repository.py` (docs: `MODULES.md` §6-8)
- **evasion** → `src/modules/evasion/advanced_evasion.py` (docs: `MODULES.md` §9)
- **volumetric** → `src/modules/offensive/volumetric_attacks.py` (docs: `MODULES.md` §10)
- **exploitation** → `src/modules/exploitation/exploit_framework.py` (docs: `MODULES.md` §11)
- **session** → `src/agent/session.py` (docs: `MODULES.md` §12)
- **agent** → `src/agent/agent.py` (docs: `MODULES.md` §13)
- **config** → `config/config.py` (docs: `ARCHITECTURE.md` Configuration)

### By Topic
- **Getting Started** → `README.md` + `docs/SETUP.md`
- **Architecture** → `docs/ARCHITECTURE.md`
- **API Reference** → `docs/MODULES.md`
- **Configuration** → `config/config.py` + `docs/ARCHITECTURE.md`
- **Database** → `src/core/database.py` + `docs/MODULES.md` §3
- **CLI Commands** → `README.md` Commands + `src/agent/agent.py`
- **Attack Types** → `docs/MODULES.md` §9-11
- **Data Assets** → `src/repositories/data_repository.py`

---

## 💡 Tips & Tricks

### Finding Something Quickly
1. **Module?** → Check `docs/MODULES.md` inventory
2. **Function?** → Search in source files or MODULES.md
3. **Configuration?** → Look in `config/config.py`
4. **Documentation?** → Start with `README.md`, then specific docs

### Adding New Feature
1. Create file in appropriate `src/modules/` subdirectory
2. Follow class/function patterns in existing code
3. Add docstrings with examples
4. Update `docs/MODULES.md` with new entries
5. Test with pytest

### Extending OMEGA
See `docs/ARCHITECTURE.md` section "Adding New Modules" for complete pattern.

---

## 📞 Help & Resources

- **Installation issues?** → `docs/SETUP.md` Troubleshooting
- **Command help?** → `README.md` Commands section
- **Module not found?** → Check import in `src/modules/__init__.py`
- **Configuration?** → Edit `config/config.py`
- **Code examples?** → See `docs/MODULES.md` Quick Reference

---

## ✅ Verification Checklist

After installation, verify:
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Can import OMEGA (`python -c "from src.agent import OmegaAgent"`)
- [ ] CLI starts (`python omega.py`)
- [ ] Commands work (type `help` in CLI)
- [ ] Documentation readable (`less docs/MODULES.md`)

---

## 📝 Version Information

- **Project**: Project OMEGA v4.0
- **Type**: Advanced Persistent Attack Framework
- **Status**: Production Ready
- **Last Updated**: November 18, 2025
- **Architecture**: Fully Modular (13 modules)
- **Documentation**: Comprehensive (4 guides)

---

**Ready to begin? Start with `README.md` or `docs/SETUP.md`**

For detailed information, visit the appropriate documentation file above.
