# Project OMEGA v4.0 - Modular Architecture Guide

## Overview

Project OMEGA has been refactored from a 10,000+ line monolith into a clean, modular architecture with proper separation of concerns. This guide documents the structure and usage of each module.

## Project Structure

```
omega/
├── src/                          # Main source code
│   ├── __init__.py              # Package initialization
│   ├── utils/                    # Utility modules
│   │   ├── __init__.py
│   │   └── output.py            # Output formatting and colors
│   ├── core/                     # Core infrastructure
│   │   ├── __init__.py
│   │   ├── dependencies.py      # Dependency management
│   │   ├── database.py          # Database operations
│   │   ├── opsec.py             # OPSEC features
│   │   └── exploiter.py         # HTTP exploitation base
│   ├── repositories/             # Data repositories
│   │   ├── __init__.py
│   │   └── data_repository.py   # VKB, shellcodes, user agents
│   ├── modules/                  # Offensive modules
│   │   ├── __init__.py
│   │   ├── evasion/             # Evasion techniques
│   │   │   ├── __init__.py
│   │   │   └── advanced_evasion.py
│   │   ├── offensive/           # Network attacks
│   │   │   ├── __init__.py
│   │   │   └── volumetric_attacks.py
│   │   └── exploitation/        # Web exploitation
│   │       ├── __init__.py
│   │       └── exploit_framework.py
│   └── agent/                    # CLI interface
│       ├── __init__.py
│       ├── agent.py             # Main CLI agent
│       └── session.py           # Session management
├── config/                       # Configuration
│   └── config.py               # Central configuration
├── docs/                         # Documentation
├── tests/                        # Unit tests
├── omega.py                      # Main entry point
└── requirements.txt              # Python dependencies
```

## Module Details

### 1. Utils Package (`src/utils/`)

**Purpose**: Provides common utilities and output formatting.

#### `output.py`
- `Color` class: ANSI color definitions
- `print_header()`: Print formatted headers
- `print_info()`: Print info messages
- `print_error()`: Print error messages
- `print_debug()`: Print debug messages
- `print_success()`: Print success messages

**Usage**:
```python
from src.utils import print_header, print_info, print_error

print_header("My Header")
print_info("Information message")
print_error("Error message")
```

### 2. Core Package (`src/core/`)

**Purpose**: Core infrastructure and base functionality.

#### `dependencies.py`
- `import_dependency()`: Dynamic import with tracking
- `load_core_dependencies()`: Load all core dependencies
- `get_dependency_status()`: Report dependency status
- `is_available()`: Check if dependency is loaded

**Usage**:
```python
from src.core import load_core_dependencies, is_available

load_core_dependencies()
if is_available('requests'):
    # Use requests library
```

#### `database.py`
- `DatabaseManager`: SQLite database management
  - `add_or_get_target()`: Register/retrieve targets
  - `add_vulnerability()`: Record vulnerabilities
  - `add_exploit_attempt()`: Log exploit attempts
  - `get_target_vulnerabilities()`: Retrieve target vulns

**Usage**:
```python
from src.core import DatabaseManager

db = DatabaseManager('omega.db')
target_id = db.add_or_get_target('192.168.1.1')
db.add_vulnerability(target_id, 'CVE-2021-12345', 5, 'RCE')
```

#### `opsec.py`
- `OPSECManager`: Operational security management
  - User agent rotation
  - Proxy management
  - Header spoofing
  - Anti-detection checks

**Usage**:
```python
from src.core import OPSECManager

opsec = OPSECManager()
opsec.load_user_agents(agent_list)
opsec.set_proxy('http://proxy.com:8080')
headers = opsec.get_opsec_headers()
```

#### `exploiter.py`
- `ActiveExploiter`: HTTP-based exploitation base class
  - Session management
  - Request sending with OPSEC
  - Timing measurements
  - Response handling

**Usage**:
```python
from src.core import ActiveExploiter, OPSECManager

opsec = OPSECManager()
exploiter = ActiveExploiter(opsec_manager=opsec, target_url='http://target.com')
response = exploiter.get_request('/path')
```

### 3. Repositories Package (`src/repositories/`)

**Purpose**: Data storage and management for attack assets.

#### `data_repository.py`

**VulnerabilityKnowledgeBase**:
- 2000+ CVE entries with metadata
- `get_by_cve()`: Retrieve by CVE ID
- `search_by_technology()`: Search by tech
- `search_by_type()`: Search by vulnerability type
- `search_by_severity()`: Search by severity

**ShellcodeRepository**:
- 1000+ shellcode payloads
- `get_by_name()`: Retrieve by name
- `get_by_architecture()`: x86, x64, ARM, etc.
- `get_by_os()`: Windows, Linux, etc.

**UserAgentRepository**:
- 500+ user agent strings
- `get_random()`: Random UA
- `get_all()`: All agents

**DataRepository**: Central coordinator
- `get_vkb()`: Access VKB
- `get_shellcode_repo()`: Access shellcodes
- `get_user_agents()`: Access user agents
- `get_status()`: Repository statistics

**Usage**:
```python
from src.repositories import DataRepository

data = DataRepository()
vkb = data.get_vkb()
vulns = vkb.search_by_technology('Apache Struts')

shellcodes = data.get_shellcode_repo()
windows_payloads = shellcodes.get_by_os('Windows')

agents = data.get_user_agents()
random_ua = agents.get_random()
```

### 4. Modules Package (`src/modules/`)

#### Evasion Module (`src/modules/evasion/`)

**MemoryManipulation**:
- Windows shellcode injection via ctypes
- Linux shellcode execution
- Memory allocation and execution

**AdvancedEvasionTechniques**:
- Process hollowing preparation
- Anti-debugging checks
- Anti-VM detection
- Memory manipulation integration

**Usage**:
```python
from src.modules.evasion import AdvancedEvasionTechniques

aet = AdvancedEvasionTechniques()
mem_manip = aet.get_memory_manipulation()
mem_manip.execute_shellcode_windows(shellcode_hex)

# Check for debugging
if aet.anti_debugging_check():
    print("Debugger detected")

# Check for VM
if aet.anti_vm_check():
    print("Virtual machine detected")
```

#### Offensive Module (`src/modules/offensive/`)

**TCPSYNFlood**:
- Raw socket TCP SYN flood
- Customizable packet rate
- Random source ports
- Proper checksum calculation

**UDPFlood**:
- UDP-based volumetric attack
- Configurable packet size
- Rate limiting

**VolumetricAttackSimulation**:
- Unified attack interface
- Multi-vector support

**Usage**:
```python
from src.modules.offensive import VolumetricAttackSimulation

volumetric = VolumetricAttackSimulation()
syn = volumetric.get_syn_flood()
syn.launch_attack('192.168.1.1', 80, duration_sec=10, rate=1000)

udp = volumetric.get_udp_flood()
udp.launch_attack('192.168.1.1', 53, duration_sec=5, rate=500)
```

#### Exploitation Module (`src/modules/exploitation/`)

**WebVulnerabilityExploit**:
- SQL injection testing
- XSS detection
- Directory traversal
- HTTP-based attack vectors

**NetworkExploit**:
- RCE execution framework
- Privilege escalation
- Post-exploitation

**ExploitationFramework**: Central coordinator
- Web and network exploit integration
- Unified interface

**Usage**:
```python
from src.modules.exploitation import ExploitationFramework
from src.core import ActiveExploiter

exploiter = ActiveExploiter(target_url='http://target.com')
framework = ExploitationFramework(http_exploiter=exploiter)

web = framework.get_web_module()
web.sql_injection_test('http://target.com/search', 'q')

net = framework.get_network_module()
net.rce_execution('192.168.1.1', 'whoami')
```

### 5. Agent Package (`src/agent/`)

#### `session.py`
- `SessionState`: User session context
  - Target tracking
  - Command history
  - Context variables
  - Session information

#### `agent.py`
- `OmegaAgent`: Interactive CLI interface
  - Command parsing
  - Module orchestration
  - Help system
  - Multi-command support

**Commands**:
```
set <option> <value>      # Configure settings
info [type]               # Show information
target <cmd> [args]       # Manage targets
attack <type> [options]   # Launch attacks
list <type>               # List data repositories
help [cmd]                # Show help
exit                      # Quit
```

**Usage**:
```python
from src.agent import OmegaAgent

agent = OmegaAgent(db_path='omega.db')
agent.cmdloop()
```

## Quick Start

### Installation

```bash
# Clone/download the project
cd omega

# Install dependencies (optional)
pip install -r requirements.txt

# Run OMEGA
python omega.py
```

### Basic Usage

```
OMEGA> set target 192.168.1.1
OMEGA(192.168.1.1)> info session
OMEGA(192.168.1.1)> list vkb
OMEGA(192.168.1.1)> attack syn 80 10
OMEGA(192.168.1.1)> exit
```

### Programmatic Usage

```python
from src.agent import OmegaAgent
from src.core import DatabaseManager, OPSECManager
from src.repositories import DataRepository
from src.modules import VolumetricAttackSimulation

# Initialize components
db = DatabaseManager('omega.db')
opsec = OPSECManager()
data = DataRepository()
volumetric = VolumetricAttackSimulation()

# Use components
target_id = db.add_or_get_target('192.168.1.1')
volumetric.syn_flood.launch_attack('192.168.1.1', 80, duration_sec=10)
```

## Configuration

Edit `config/config.py` to customize:
- Database settings
- HTTP client behavior
- Proxy configuration
- Attack parameters
- OPSEC features
- Logging settings

## Architecture Principles

1. **Modularity**: Each module has a single responsibility
2. **Reusability**: Components can be used independently
3. **Testability**: Clear interfaces for unit testing
4. **Scalability**: Easy to add new modules
5. **Maintainability**: Clean separation of concerns
6. **Documentation**: Comprehensive docstrings

## Adding New Modules

### Example: Adding a New Attack Module

```python
# src/modules/custom/my_attack.py
from ...utils import print_header, print_info

class MyCustomAttack:
    def __init__(self):
        print_info("My custom attack initialized")
    
    def execute(self, target, **kwargs):
        print_header(f"Executing custom attack on {target}")
        # Implementation

# src/modules/custom/__init__.py
from .my_attack import MyCustomAttack
__all__ = ['MyCustomAttack']

# Update src/modules/__init__.py to include the new module
```

## Testing

Run tests with:
```bash
python -m pytest tests/
```

## Performance Notes

- Database uses SQLite with WAL for concurrent access
- Dependency loading is lazy - only load what you need
- Data repositories generate data on initialization (2000+ entries)
- Connection pooling for HTTP exploiter
- Configurable thread pool for concurrent operations

## Security Considerations

- No SSL verification by default (can be enabled)
- User agent and proxy rotation for OPSEC
- Memory manipulation uses unsafe operations (platform-specific)
- Raw socket operations require elevated privileges
- Consider legal implications before using

## License

See LICENSE file in project root

## Author

H@ckbot - Project OMEGA Team
