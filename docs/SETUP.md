# Project OMEGA v4.0 - Installation and Setup Guide

## Prerequisites

- **Python 3.8+** (test with `python --version`)
- **pip** (Python package manager)
- **Git** (for cloning repository)
- **Administrator/Root** privileges (for raw socket operations)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/legitimate-stupidity/omega.git
cd omega
```

### 2. Verify Python Version

```bash
python --version
# Expected: Python 3.8.0 or higher
```

### 3. Create Virtual Environment (Recommended)

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
# Install optional dependencies
pip install -r requirements.txt

# Core dependencies (built-in):
# - socket
# - struct
# - sqlite3
# - cmd
# - time
# - random
# - threading
# - json
```

### 5. Verify Installation

```bash
# Check imports
python -c "from src.agent import OmegaAgent; print('✓ Installation successful')"

# List project structure
python -c "import os; [print(x) for x in os.walk('src')]"
```

## Running OMEGA

### Interactive Mode

```bash
# Basic usage (in-memory database)
python omega.py

# With persistent database
python omega.py --db omega.db

# Get help
python omega.py --help
```

### Example Session

```
$ python omega.py

      ___    __  __  _______   _____      ___     
     /   \  |  \/  | |  ____| /  ___|    /   \    Project OMEGA v4.0
    / /_\ \ |      | |  |__  |  /  ___  / /_\ \   Advanced Persistent Attack Framework
   |  ___  || |\/| | |   __| | |  |_  ||  ___  |  
   | |   | || |  | | |  |___ |  \__| || |   | |  
   |_|   |_||_|  |_| |______| \_____/ |_|   |_|  

Repository Loaded: VKB Entries (2000), Shellcodes (1001)

OMEGA> set target 192.168.1.1
OMEGA(192.168.1.1)> info session
OMEGA(192.168.1.1)> help
OMEGA(192.168.1.1)> exit
```

## Programmatic Usage

### Basic Example

```python
#!/usr/bin/env python3
"""Example usage of OMEGA modules."""

from src.core import DatabaseManager, OPSECManager
from src.repositories import DataRepository
from src.modules import VolumetricAttackSimulation

# Initialize
db = DatabaseManager('test.db')
opsec = OPSECManager()
data = DataRepository()

# Use modules
target_id = db.add_or_get_target('192.168.1.1')
print(f"Target ID: {target_id}")

# Search vulnerabilities
vkb = data.get_vkb()
results = vkb.search_by_technology('Apache')
print(f"Found {len(results)} Apache vulnerabilities")
```

Save as `example.py` and run:

```bash
python example.py
```

## Configuration

### Editing Configuration

Edit `config/config.py` to customize behavior:

```python
# Example modifications

# Change HTTP timeout
HTTP = {
    'default_timeout': 20,  # increased from 10
    'verify_ssl': False,
    'max_retries': 5,  # increased from 3
}

# Enable OPSEC features
OPSEC = {
    'enable_anti_debugging': True,
    'enable_anti_vm': True,
    'randomize_timings': True,
}

# Modify attack parameters
ATTACKS = {
    'syn_flood': {
        'default_rate': 5000,  # increased from 1000
        'default_duration': 30,  # increased from 10
    },
}
```

### Using Configuration in Code

```python
from config.config import get_config, set_config

# Get value
timeout = get_config('HTTP.default_timeout')
print(f"Timeout: {timeout}")

# Set value
set_config('HTTP.default_timeout', 25)

# Get with default
verify = get_config('HTTP.verify_ssl', True)
```

## Database Management

### In-Memory Database (Default)

```bash
python omega.py
# Data is lost when program exits
```

### Persistent Database

```bash
python omega.py --db omega.db
# Data saved to omega.db file
```

### Database Operations

```python
from src.core import DatabaseManager

db = DatabaseManager('omega.db')

# Add target
target_id = db.add_or_get_target('192.168.1.1', 'server.local')

# Record vulnerability
db.add_vulnerability(target_id, 'CVE-2021-12345', 5, 'RCE vulnerability')

# Record exploit attempt
db.add_exploit_attempt(target_id, 'struts_rce', 'success')

# Query data
vulns = db.get_target_vulnerabilities(target_id)
for cve, severity, desc in vulns:
    print(f"{cve}: {desc} (Severity: {severity})")

# Close connection
db.close()
```

## Module Organization

### Import Paths

```python
# Core modules
from src.core import (
    DatabaseManager,
    OPSECManager,
    ActiveExploiter,
    load_core_dependencies
)

# Repositories
from src.repositories import DataRepository

# Modules
from src.modules import (
    AdvancedEvasionTechniques,
    VolumetricAttackSimulation,
    ExploitationFramework
)

# Agent
from src.agent import OmegaAgent
```

## Testing Setup

### Running Tests

```bash
# Install testing dependencies
pip install pytest pytest-cov

# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_core.py -v

# Run with coverage report
python -m pytest tests/ --cov=src
```

### Creating Tests

Example test file `tests/test_modules.py`:

```python
import pytest
from src.core import DatabaseManager
from src.modules import VolumetricAttackSimulation

class TestVolumetricAttacks:
    def test_syn_flood_initialization(self):
        attack = VolumetricAttackSimulation()
        assert attack.syn_flood is not None
    
    def test_database_initialization(self):
        db = DatabaseManager(':memory:')
        target_id = db.add_or_get_target('127.0.0.1')
        assert target_id is not None
```

## Troubleshooting

### Common Issues

#### ModuleNotFoundError

```bash
# Solution 1: Ensure you're in the omega directory
cd /path/to/omega

# Solution 2: Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Solution 3: Use module syntax
python -m omega
```

#### Permission Denied (Raw Sockets)

```bash
# Linux/macOS - Use sudo
sudo python omega.py

# Windows - Run as Administrator
# Right-click Command Prompt → "Run as administrator"
python omega.py
```

#### Import Errors After Installation

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Reinstall package in development mode
pip install -e .
```

#### Database Locked Error

```bash
# Solution: Close other instances of OMEGA
# OR delete the database file and restart
rm omega.db
python omega.py --db omega.db
```

## Performance Optimization

### Initial Load Times

```
Data Repository Initialization:
  - VKB: ~1-2 seconds (2000 entries)
  - Shellcodes: ~0.5 seconds (1000+ payloads)
  - User Agents: ~0.1 seconds (500 agents)
  Total: ~2 seconds

Database: < 100ms initialization
Connection Pool: ~50ms setup
```

### Tips for Faster Operation

```python
# Load only needed data
from src.repositories import VulnerabilityKnowledgeBase

vkb = VulnerabilityKnowledgeBase()  # Fast, only loads VKB

# Use persistent database for faster subsequent runs
python omega.py --db omega.db  # Pre-populated database

# Cache frequently accessed data
results = vkb.search_by_technology('Apache')
# Reuse results variable instead of re-querying
```

## Security Setup

### Minimal Permissions Setup

```bash
# Run as non-root user for most operations
python omega.py --db omega.db

# Escalate only for raw socket operations
sudo python omega.py --db omega.db  # For SYN floods
```

### Firewall Configuration

```bash
# Linux - Allow outbound traffic
sudo ufw allow out to any port 80
sudo ufw allow out to any port 443

# macOS - No additional configuration needed
# Windows - Windows Firewall (configure as needed)
```

## Advanced Setup

### Using with Virtual Environments

```bash
# Create environment
python3 -m venv omega_env

# Activate (Linux/macOS)
source omega_env/bin/activate

# Activate (Windows)
omega_env\Scripts\activate

# Install OMEGA
cd omega
pip install -r requirements.txt
python omega.py
```

### Systemd Service (Linux)

Create `/etc/systemd/system/omega.service`:

```ini
[Unit]
Description=Project OMEGA Service
After=network.target

[Service]
Type=simple
User=omega_user
WorkingDirectory=/path/to/omega
ExecStart=/usr/bin/python3 /path/to/omega/omega.py --db /var/lib/omega/omega.db
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable omega
sudo systemctl start omega
sudo systemctl status omega
```

## Next Steps

1. **Read Documentation**
   - `docs/ARCHITECTURE.md` - Detailed architecture
   - `docs/MODULES.md` - Module reference

2. **Run Examples**
   - Try interactive CLI commands
   - Execute example scripts

3. **Develop Extensions**
   - Add custom modules in `src/modules/`
   - Extend functionality with new classes

4. **Contribute**
   - Follow coding standards
   - Document all changes
   - Submit pull requests

## Support and Resources

- **GitHub Issues**: Report bugs and request features
- **Documentation**: See `docs/` directory
- **Code Examples**: Check `tests/` for usage patterns
- **Inline Docs**: Read docstrings in source files

---

**Last Updated**: November 18, 2025
**Version**: OMEGA v4.0
