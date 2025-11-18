# Project OMEGA v4.0 - Module Reference

## Complete Module Inventory

This document provides a complete reference for all modules in Project OMEGA.

## Core Modules

### 1. Output & Formatting (`src/utils/output.py`)

| Function | Purpose | Example |
|----------|---------|---------|
| `print_header(title)` | Print section header | `print_header("Attack Phase")` |
| `print_info(message)` | Information message | `print_info("Operation started")` |
| `print_error(message)` | Error message | `print_error("Failed to connect")` |
| `print_debug(message)` | Debug message | `print_debug("Variable x = 5")` |
| `print_success(message)` | Success message | `print_success("Target compromised")` |
| `print_warning(message)` | Warning message | `print_warning("High-risk operation")` |

**Color Class Properties**:
- `Color.HEADER` - Purple
- `Color.OKBLUE` - Blue
- `Color.OKGREEN` - Green
- `Color.WARNING` - Yellow
- `Color.FAIL` - Red
- `Color.BOLD` - Bold text

---

### 2. Dependency Management (`src/core/dependencies.py`)

| Function | Purpose | Returns |
|----------|---------|---------|
| `import_dependency(lib, pip)` | Dynamic import | `bool` - Success/failure |
| `load_core_dependencies()` | Load all dependencies | `dict` - Status map |
| `get_dependency_status()` | Generate report | `str` - Formatted report |
| `is_available(pip_name)` | Check availability | `bool` |

**Tracked Dependencies**:
- `requests` - HTTP library
- `boto3` - AWS SDK
- `cryptography` - Crypto operations
- `winreg` - Windows registry (Windows only)

---

### 3. Database (`src/core/database.py`)

**DatabaseManager Class**:

| Method | Purpose | Signature |
|--------|---------|-----------|
| `__init__()` | Initialize DB | `DatabaseManager(db_path=':memory:')` |
| `add_or_get_target()` | Register target | `add_or_get_target(ip, hostname) -> int` |
| `get_all_targets()` | List targets | `get_all_targets() -> list` |
| `add_vulnerability()` | Record vuln | `add_vulnerability(target_id, cve, severity, desc) -> int` |
| `add_exploit_attempt()` | Log attempt | `add_exploit_attempt(target_id, name, status) -> int` |
| `get_target_vulnerabilities()` | Get vulns | `get_target_vulnerabilities(target_id) -> list` |
| `close()` | Close connection | `close()` |

**Tables**:
- `targets` - IP addresses and metadata
- `vulnerabilities` - CVE information per target
- `exploits` - Exploitation attempts
- `sessions` - Session data

---

### 4. OPSEC Management (`src/core/opsec.py`)

**OPSECManager Class**:

| Method | Purpose |
|--------|---------|
| `load_user_agents(ua_list)` | Load UA pool |
| `get_random_ua()` | Get random UA |
| `rotate_ua_status(enabled)` | Enable/disable UA rotation |
| `set_proxy(proxy_string)` | Set single proxy |
| `add_proxy(proxy_string)` | Add to rotation |
| `set_proxy_list(proxy_list)` | Set multiple proxies |
| `get_rotating_proxy()` | Get next proxy |
| `get_opsec_headers()` | Get spoofed headers |
| `get_status()` | Get config status |

**Configuration Options**:
- User agent rotation
- Proxy rotation
- Header spoofing
- Connection management

---

### 5. HTTP Exploiter (`src/core/exploiter.py`)

**ActiveExploiter Class**:

| Method | Purpose | Example |
|--------|---------|---------|
| `get_request()` | Send GET | `get_request('/path')` |
| `post_request()` | Send POST | `post_request('/api', data={})` |
| `put_request()` | Send PUT | `put_request('/api', json={})` |
| `send_request()` | Custom request | `send_request('GET', url, **kwargs)` |
| `close()` | Close session | `close()` |

**Features**:
- OPSEC header injection
- Proxy rotation support
- Response timing
- Exception handling

---

## Data Repository Modules

### 6. Vulnerability Knowledge Base (`src/repositories/data_repository.py`)

**VulnerabilityKnowledgeBase Class**:

| Method | Purpose | Returns |
|--------|---------|---------|
| `get_by_cve(cve_id)` | Get by CVE | `dict` - CVE data |
| `search_by_technology(tech)` | Search by tech | `list` - Tuples |
| `search_by_type(vuln_type)` | Search by type | `list` - Tuples |
| `search_by_severity(min, max)` | Search by severity | `list` - Tuples |
| `get_all()` | All entries | `dict` |
| `count()` | Count entries | `int` |

**Entry Structure**:
```python
{
    'name': 'RCE in Apache Struts',
    'severity': 5,
    'technology': 'Apache Struts',
    'vuln_type': 'RCE',
    'module': 'Exploit_RCE_ApacheStruts',
    'signatures': [{'type': 'banner', 'value': 'Apache Struts'}],
    'discovery_date': '2021-03-15'
}
```

### 7. Shellcode Repository

**ShellcodeRepository Class**:

| Method | Purpose | Returns |
|--------|---------|---------|
| `get_by_name(name)` | Get by name | `dict` - Shellcode data |
| `get_by_architecture(arch)` | Get by arch | `list` - Tuples |
| `get_by_os(os_name)` | Get by OS | `list` - Tuples |
| `get_all()` | All payloads | `dict` |
| `count()` | Count payloads | `int` |

**Payload Structure**:
```python
{
    'description': 'Executes /bin/sh',
    'architecture': 'x86',
    'os': 'Linux',
    'shellcode': '31c050682f2f7368...'
}
```

### 8. User Agent Repository

**UserAgentRepository Class**:

| Method | Purpose |
|--------|---------|
| `get_random()` | Random user agent |
| `get_all()` | All agents |
| `count()` | Total count |

---

## Offensive Modules

### 9. Advanced Evasion Techniques (`src/modules/evasion/advanced_evasion.py`)

**MemoryManipulation Class**:

| Method | Purpose | Platform |
|--------|---------|----------|
| `execute_shellcode_windows(hex)` | Execute shellcode | Windows |
| `execute_shellcode_linux(hex)` | Execute shellcode | Linux |

**AdvancedEvasionTechniques Class**:

| Method | Purpose |
|--------|---------|
| `get_memory_manipulation()` | Access mem module |
| `process_hollowing_preparation(proc, path)` | Prep hollowing |
| `anti_debugging_check()` | Detect debugger |
| `anti_vm_check()` | Detect VM |

---

### 10. Volumetric Attacks (`src/modules/offensive/volumetric_attacks.py`)

**TCPSYNFlood Class**:

```python
# Usage
syn = TCPSYNFlood()
syn.launch_attack(
    target_ip='192.168.1.1',
    target_port=80,
    duration_sec=10,
    rate=1000  # packets/sec
)
```

**UDPFlood Class**:

```python
# Usage
udp = UDPFlood()
udp.launch_attack(
    target_ip='192.168.1.1',
    target_port=53,
    duration_sec=10,
    rate=1000,
    packet_size=512
)
```

**VolumetricAttackSimulation Class**:

| Method | Purpose |
|--------|---------|
| `get_syn_flood()` | Access SYN module |
| `get_udp_flood()` | Access UDP module |

---

### 11. Exploitation Framework (`src/modules/exploitation/exploit_framework.py`)

**WebVulnerabilityExploit Class**:

| Method | Purpose |
|--------|---------|
| `sql_injection_test(url, param)` | Test SQL injection |
| `xss_test(url, param)` | Test XSS |
| `directory_traversal_test(url)` | Test path traversal |

**NetworkExploit Class**:

| Method | Purpose |
|--------|---------|
| `rce_execution(target, command)` | Execute command |
| `privilege_escalation(target, method)` | Attempt escalation |

**ExploitationFramework Class**:

| Method | Purpose |
|--------|---------|
| `get_web_module()` | Web exploits |
| `get_network_module()` | Network exploits |

---

## Agent Modules

### 12. Session Management (`src/agent/session.py`)

**SessionState Class**:

| Method | Purpose |
|--------|---------|
| `set_target(ip, hostname)` | Set current target |
| `add_to_history(cmd, result)` | Log command |
| `set_context_var(key, value)` | Set variable |
| `get_context_var(key)` | Get variable |
| `get_prompt()` | Get CLI prompt |
| `get_session_info()` | Session stats |

### 13. CLI Agent (`src/agent/agent.py`)

**OmegaAgent Class** (extends `cmd.Cmd`):

| Command | Format | Example |
|---------|--------|---------|
| `set` | `set <opt> <val>` | `set target 192.168.1.1` |
| `info` | `info [type]` | `info session` |
| `target` | `target <cmd>` | `target list` |
| `attack` | `attack <type>` | `attack syn 80` |
| `list` | `list <type>` | `list vkb` |
| `help` | `help [cmd]` | `help attack` |
| `exit` | `exit` | `exit` |

---

## Configuration

### `config/config.py`

**Configuration Sections**:

| Section | Key Settings |
|---------|--------------|
| `DATABASE` | `default_path`, `max_connections`, `timeout` |
| `HTTP` | `default_timeout`, `verify_ssl`, `max_retries` |
| `PROXY` | `enabled`, `rotate`, `default_proxy` |
| `ATTACKS` | `syn_flood`, `udp_flood` settings |
| `OPSEC` | Anti-debug, anti-VM, timing randomization |
| `LOGGING` | `level`, `format`, `file`, `max_file_size` |
| `MODULES` | Enable/disable modules |
| `SECURITY` | Confirmation, dry-run, audit |

**Access Configuration**:
```python
from config.config import get_config, set_config

value = get_config('HTTP.default_timeout')  # Get
set_config('HTTP.default_timeout', 20)      # Set
```

---

## Quick Reference

### Initialization Pattern

```python
# Standard initialization
from src.core import load_core_dependencies, DatabaseManager, OPSECManager
from src.repositories import DataRepository
from src.modules import VolumetricAttackSimulation

load_core_dependencies()
db = DatabaseManager('omega.db')
opsec = OPSECManager()
data = DataRepository()
volumetric = VolumetricAttackSimulation()
```

### Common Workflows

**Vulnerability Lookup**:
```python
vkb = data.get_vkb()
vuln = vkb.get_by_cve('CVE-2021-44228')
results = vkb.search_by_technology('Apache Struts')
```

**Target Management**:
```python
target_id = db.add_or_get_target('192.168.1.1', 'server.local')
vulns = db.get_target_vulnerabilities(target_id)
```

**Attack Execution**:
```python
syn = volumetric.get_syn_flood()
syn.launch_attack('192.168.1.1', 80, duration_sec=10, rate=1000)
```

**HTTP Exploitation**:
```python
from src.core import ActiveExploiter
exploiter = ActiveExploiter(opsec_manager=opsec)
response = exploiter.get_request('http://target.com/vulnerable')
```

---

## Module Dependencies

```
agent/
  ├─ requires: core, modules, repositories, utils
modules/
  ├─ evasion/ → utils
  ├─ offensive/ → utils
  └─ exploitation/ → utils, core
repositories/ → utils
core/
  ├─ depends on: utils
  └─ opsec.py, exploiter.py → requests (optional)
utils/
  └─ no dependencies
```

---

End of Module Reference
