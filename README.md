# Project OMEGA v4.0

**Advanced Persistent Attack Framework**

A comprehensive, modular offensive security platform for advanced network attack simulation, vulnerability assessment, and exploitation research.

## Features

### Core Capabilities

- **Vulnerability Management**: 2000+ CVE database with detailed metadata
- **Shellcode Repository**: 1000+ payload variants for multiple architectures
- **HTTP Exploitation**: Web-based vulnerability testing framework
- **Volumetric Attacks**: SYN floods, UDP floods, and DDoS simulation
- **Advanced Evasion**: Memory manipulation, anti-debugging, anti-VM
- **OPSEC Features**: User agent rotation, proxy management, timing randomization
- **Target Management**: Persistent database for target tracking
- **Interactive CLI**: Command-line interface for real-time control

### Architecture Highlights

- **Fully Modular**: Clean separation of concerns with 13 independent modules
- **Extensible**: Easy to add new modules and features
- **Well-Documented**: Comprehensive docstrings and external documentation
- **Production-Ready**: Proper error handling and logging
- **Cross-Platform**: Windows, Linux, and macOS support
- **No External CLI**: Pure Python implementation

## Quick Start

### Requirements

- Python 3.8+
- Linux/macOS (or Windows with admin privileges for raw sockets)

### Installation

```bash
# Clone the repository
git clone https://github.com/legitimate-stupidity/omega.git
cd omega

# Install optional dependencies
pip install -r requirements.txt

# Run OMEGA
python omega.py
```

### Basic Usage

```bash
# Start the interactive agent
$ python omega.py

# Set your target
OMEGA> set target 192.168.1.1

# View your target's information
OMEGA(192.168.1.1)> info session

# List available vulnerabilities
OMEGA(192.168.1.1)> list vkb

# Launch a TCP SYN flood attack
OMEGA(192.168.1.1)> attack syn 80 10

# Exit
OMEGA(192.168.1.1)> exit
```

## Commands

### Configuration Commands

```bash
set target <ip>          # Set the target IP address
set proxy <url>          # Set proxy server (e.g., http://proxy:8080)
set timeout <seconds>    # Set HTTP request timeout
set <key> <value>        # Set arbitrary context variable
```

### Information Commands

```bash
info session             # Show session information
info opsec               # Show OPSEC configuration
info repositories        # Show data repository statistics
target list              # List all known targets
target set <ip>          # Register/set target
```

### Attack Commands

```bash
attack syn <port> [duration]           # TCP SYN flood
attack udp <port> [duration] [rate]    # UDP flood
```

### Data Commands

```bash
list vkb                 # List Vulnerability Knowledge Base
list shellcodes          # List available shellcode payloads
list agents              # List user agent pool
```

### System Commands

```bash
help [command]           # Show help information
exit                     # Exit OMEGA
```

## Project Structure

```
omega/
├── src/
│   ├── utils/              # Output formatting and utilities
│   ├── core/               # Core infrastructure
│   │   ├── dependencies.py # Dependency management
│   │   ├── database.py     # Database operations
│   │   ├── opsec.py        # Operational security
│   │   └── exploiter.py    # HTTP exploitation base
│   ├── repositories/       # Data storage
│   │   └── data_repository.py  # VKB, shellcodes, user agents
│   ├── modules/            # Offensive modules
│   │   ├── evasion/        # Evasion techniques
│   │   ├── offensive/      # Network attacks
│   │   └── exploitation/   # Web exploitation
│   └── agent/              # CLI interface
├── config/                 # Configuration
├── docs/                   # Documentation
│   ├── ARCHITECTURE.md    # Detailed architecture guide
│   └── MODULES.md         # Module reference
├── tests/                  # Unit tests (framework ready)
├── omega.py               # Main entry point
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Modules Overview

### Utility Modules

- **output.py**: Terminal formatting and color output

### Core Infrastructure

- **dependencies.py**: Dynamic import and dependency tracking
- **database.py**: SQLite database management for targets and vulns
- **opsec.py**: User agent rotation, proxy management, header spoofing
- **exploiter.py**: HTTP-based exploitation with OPSEC features

### Data Repositories

- **data_repository.py**: 
  - VulnerabilityKnowledgeBase: 2000+ CVE entries
  - ShellcodeRepository: 1000+ payloads
  - UserAgentRepository: 500+ user agents

### Offensive Modules

- **evasion/advanced_evasion.py**:
  - Memory manipulation (Windows/Linux)
  - Shellcode injection
  - Anti-debugging detection
  - Anti-VM detection

- **offensive/volumetric_attacks.py**:
  - TCP SYN flood with raw sockets
  - UDP flood attacks
  - Configurable attack parameters

- **exploitation/exploit_framework.py**:
  - SQL injection testing
  - XSS vulnerability testing
  - Directory traversal detection
  - RCE execution framework

### Agent Interface

- **agent.py**: Interactive CLI command interpreter
- **session.py**: Session state and context management

## Programmatic Usage

Use OMEGA components in your own Python code:

```python
from src.core import DatabaseManager, OPSECManager, ActiveExploiter
from src.repositories import DataRepository
from src.modules import VolumetricAttackSimulation

# Initialize components
db = DatabaseManager('omega.db')
opsec = OPSECManager()
data = DataRepository()

# Register target
target_id = db.add_or_get_target('192.168.1.1', 'server.local')

# Load data
vkb = data.get_vkb()
vulns = vkb.search_by_technology('Apache Struts')

# Configure OPSEC
ua_list = data.get_user_agents().get_all()
opsec.load_user_agents(ua_list)

# Execute attacks
volumetric = VolumetricAttackSimulation()
syn = volumetric.get_syn_flood()
syn.launch_attack('192.168.1.1', 80, duration_sec=10, rate=1000)
```

## Configuration

Edit `config/config.py` to customize:

```python
# Example: Change default timeout
set_config('HTTP.default_timeout', 20)

# Example: Enable OPSEC features
get_config('OPSEC.enable_anti_debugging')

# Example: Adjust attack parameters
get_config('ATTACKS.syn_flood.default_rate')
```

## Database

OMEGA uses SQLite for persistent storage. By default, it uses an in-memory database.

To use persistent storage:

```bash
python omega.py --db omega.db
```

Database tables:
- `targets`: IP addresses and metadata
- `vulnerabilities`: CVE information per target
- `exploits`: Exploitation attempts
- `sessions`: Session data

## Requirements

### Core Requirements

- Python 3.8+
- socket, struct, sqlite3 (built-in)

### Optional Requirements (from requirements.txt)

- requests: HTTP library for web exploitation
- boto3: AWS cloud operations
- cryptography: Cryptographic operations

### System Requirements

- Linux/macOS for full feature set
- Windows with administrator privileges for raw sockets
- ~100MB disk space

## Security Considerations

⚠️ **Important**: This framework is designed for authorized security research and penetration testing only.

- **Legal**: Ensure you have explicit authorization before testing any systems
- **Privileges**: Raw socket operations require root/administrator privileges
- **Networking**: DDoS attacks can cause service disruption
- **Detection**: OPSEC features help avoid detection but are not foolproof

## Documentation

- **ARCHITECTURE.md**: Detailed architecture and module design
- **MODULES.md**: Complete module reference with examples
- **omega.py**: Main entry point with CLI integration
- **Docstrings**: Comprehensive in-code documentation

## Performance

- VKB initialization: ~1-2 seconds (generates 2000 entries)
- Shellcode repo initialization: ~0.5 seconds (generates 1000+ payloads)
- User agent loading: ~0.1 seconds (500+ agents)
- Attack execution: Real-time with configurable rates
- Database queries: Sub-millisecond for cached data

## Troubleshooting

### Import Errors

If you get import errors:

```bash
# Ensure you're in the omega directory
cd omega

# Add to PYTHONPATH if needed
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Run with module syntax
python -m omega
```

### Permission Denied (Raw Sockets)

Raw socket operations require elevated privileges:

```bash
# Linux/macOS
sudo python omega.py

# Windows (Run as Administrator)
# Right-click terminal > Run as administrator
python omega.py
```

### Dependency Issues

Install optional dependencies:

```bash
pip install -r requirements.txt
```

## Contributing

To add new modules:

1. Create module in appropriate directory
2. Implement clean interfaces with docstrings
3. Add to `__init__.py` files for proper importing
4. Update documentation
5. Add unit tests

## License

See LICENSE file in project root

## Authors

H@ckbot - Project OMEGA Development Team

## Version History

- **v4.0** (Current): Complete modular refactor from monolithic architecture
  - 13 independent modules
  - Clean separation of concerns
  - Comprehensive documentation
  - Production-ready architecture

---

**Last Updated**: November 18, 2025
**Status**: Active Development