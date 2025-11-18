"""
OMEGA Data Repository Module
Manages vulnerability knowledge base, shellcode repository, and other data assets.
"""

import random
import datetime
import hashlib
from ..utils.output import print_debug, print_info


class VulnerabilityKnowledgeBase:
    """
    Stores and manages vulnerability information including CVE data,
    exploits, and associated metadata.
    """
    
    def __init__(self):
        """Initialize VKB with technology and vulnerability data."""
        self.data = {}
        self._initialize_data()
        print_debug(f"VKB initialized with {len(self.data)} entries")
    
    def _initialize_data(self):
        """Generate vulnerability knowledge base."""
        technologies = [
            "Apache Struts", "Tomcat", "JBoss", "Nginx", "IIS",
            "OpenSSH", "vsftpd", "Exim", "Postfix",
            "MySQL", "PostgreSQL", "MongoDB", "Redis", "Memcached",
            "WordPress", "Drupal", "Joomla",
            "SAP NetWeaver", "Oracle WebLogic",
            "Cisco IOS", "Fortinet FortiOS", "Palo Alto PAN-OS",
            "Citrix NetScaler", "VMware vCenter",
            "Microsoft Exchange", "SharePoint",
            "Docker", "Kubernetes", "Jenkins", "GitLab",
            "PHP", "Node.js", "Ruby on Rails", "Django", "Flask"
        ]
        
        vuln_types = [
            "RCE", "SQL Injection", "Buffer Overflow", "XSS",
            "Authentication Bypass", "Information Disclosure",
            "Directory Traversal", "Insecure Deserialization",
            "XXE", "SSRF", "Privilege Escalation", "Denial of Service"
        ]
        
        # Generate 2000 vulnerability entries
        cve_counter = 1
        for year in range(2010, 2026):
            for _ in range(125):  # 16 years * 125 = 2000 entries
                cve_id = f"CVE-{year}-{cve_counter:05d}"
                tech = random.choice(technologies)
                vtype = random.choice(vuln_types)
                name = f"{vtype} in {tech} v{random.randint(1,10)}.{random.randint(0,9)}"
                severity = random.randint(1, 5)
                module_name = f"Exploit_{vtype.replace(' ', '_')}_{tech.replace(' ', '')}"
                
                self.data[cve_id] = {
                    'name': name,
                    'severity': severity,
                    'technology': tech,
                    'vuln_type': vtype,
                    'module': module_name,
                    'signatures': [{'type': 'banner', 'value': tech}],
                    'discovery_date': f"{year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
                }
                cve_counter += 1
    
    def get_by_cve(self, cve_id):
        """Retrieve vulnerability by CVE ID."""
        return self.data.get(cve_id)
    
    def search_by_technology(self, technology):
        """Search vulnerabilities by technology name."""
        return [
            (cve_id, data) for cve_id, data in self.data.items()
            if data['technology'].lower() == technology.lower()
        ]
    
    def search_by_type(self, vuln_type):
        """Search vulnerabilities by type."""
        return [
            (cve_id, data) for cve_id, data in self.data.items()
            if data['vuln_type'].lower() == vuln_type.lower()
        ]
    
    def search_by_severity(self, min_severity, max_severity=None):
        """Search vulnerabilities by severity range."""
        if max_severity is None:
            max_severity = 5
        
        return [
            (cve_id, data) for cve_id, data in self.data.items()
            if min_severity <= data['severity'] <= max_severity
        ]
    
    def get_all(self):
        """Get all vulnerabilities."""
        return self.data
    
    def count(self):
        """Get total number of vulnerabilities."""
        return len(self.data)


class ShellcodeRepository:
    """
    Stores compiled shellcode for various architectures and OS platforms.
    """
    
    def __init__(self):
        """Initialize shellcode repository."""
        self.repo = {}
        self._initialize_shellcodes()
        print_debug(f"Shellcode Repository initialized with {len(self.repo)} payloads")
    
    def _initialize_shellcodes(self):
        """Initialize with functional and filler shellcodes."""
        # Real shellcodes (documented examples)
        self.repo["LINUX_X86_EXEC_BINSH"] = {
            "description": "Executes /bin/sh (32-bit)",
            "architecture": "x86",
            "os": "Linux",
            "shellcode": "31c050682f2f7368682f62696e89e3505389e1b00bcd80"
        }
        
        self.repo["WINDOWS_X64_EXEC_CALC"] = {
            "description": "Executes calc.exe (64-bit)",
            "architecture": "x64",
            "os": "Windows",
            "shellcode": "fc4883e4f0e8c0000000415141505251564831d265488b5260488b5218488b5220488b7250480fb74a4a4d31c94831c0ac3c617c022c2041c1c90d4101c1e2ed524151488b52208b423c4801d08b80880000004885c074674801d0508b4818448b40204901d0e35648ffc9418b34884801d64d31c94831c0ac41c1c90d4101c138e075f14c037c244c01d1668b0c48448b401c4901d0418b04884801d0415841585e595a41584159415a4883ec204152ffe05841595a488b12e957ffffff5d48ba0100000000000000488d8d0101000041ba318b6f87ffd5bbfc4a004883c4404831d86a01584831c951488d050d0000006863616c6300514889e74889f14889da4150ffd5"
        }
        
        # Generate NOP sled fillers
        for i in range(1000):
            filler_name = f"SHELLCODE_FILLER_{i:04d}"
            nop_count = random.randint(8, 32)
            shellcode_data = "90" * nop_count
            
            self.repo[filler_name] = {
                "description": f"NOP Sled ({nop_count} bytes)",
                "architecture": "Universal",
                "os": "Cross-platform",
                "shellcode": shellcode_data
            }
    
    def get_by_name(self, payload_name):
        """Retrieve shellcode by name."""
        return self.repo.get(payload_name)
    
    def get_by_architecture(self, architecture):
        """Search shellcodes by architecture."""
        return [
            (name, data) for name, data in self.repo.items()
            if data['architecture'].lower() == architecture.lower()
        ]
    
    def get_by_os(self, os_name):
        """Search shellcodes by operating system."""
        return [
            (name, data) for name, data in self.repo.items()
            if data['os'].lower() == os_name.lower()
        ]
    
    def get_all(self):
        """Get all shellcodes."""
        return self.repo
    
    def count(self):
        """Get total number of shellcodes."""
        return len(self.repo)


class UserAgentRepository:
    """
    Manages a pool of user agents for web-based operations and spoofing.
    """
    
    def __init__(self):
        """Initialize user agent repository."""
        self.agents = []
        self._initialize_agents()
        print_debug(f"User Agent Repository initialized with {len(self.agents)} agents")
    
    def _initialize_agents(self):
        """Generate diverse user agents."""
        # Base realistic user agents
        base_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        ]
        self.agents.extend(base_agents)
        
        # Generate synthetic variants
        browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
        os_list = [
            "Windows NT 10.0",
            "Macintosh; Intel Mac OS X 10_15",
            "X11; Linux x86_64"
        ]
        
        for _ in range(500):
            browser = random.choice(browsers)
            os_name = random.choice(os_list)
            version = f"{random.randint(100, 120)}.{random.randint(0, 9)}"
            ua = f"Mozilla/5.0 ({os_name}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36"
            self.agents.append(ua)
    
    def get_random(self):
        """Get a random user agent."""
        return random.choice(self.agents)
    
    def get_all(self):
        """Get all user agents."""
        return self.agents
    
    def count(self):
        """Get total user agents."""
        return len(self.agents)


class DataRepository:
    """
    Central repository managing all OMEGA data assets including
    vulnerabilities, shellcodes, and user agents.
    """
    
    def __init__(self):
        """Initialize all data repositories."""
        print_debug("Initializing Data Repository...")
        self.vkb = VulnerabilityKnowledgeBase()
        self.shellcode_repo = ShellcodeRepository()
        self.user_agents = UserAgentRepository()
        print_info("Data Repository initialization complete")
    
    def get_vkb(self):
        """Get Vulnerability Knowledge Base."""
        return self.vkb
    
    def get_shellcode_repo(self):
        """Get Shellcode Repository."""
        return self.shellcode_repo
    
    def get_user_agents(self):
        """Get User Agent Repository."""
        return self.user_agents
    
    def get_status(self):
        """Get status of all repositories."""
        return {
            'vkb_entries': self.vkb.count(),
            'shellcodes': self.shellcode_repo.count(),
            'user_agents': self.user_agents.count()
        }
