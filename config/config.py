"""
Project OMEGA Configuration File
Central configuration management for all modules
"""

# ============================================================================
# GENERAL CONFIGURATION
# ============================================================================

PROJECT_NAME = "Project OMEGA"
PROJECT_VERSION = "4.0"
PROJECT_DESCRIPTION = "Advanced Persistent Attack Framework"

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

DATABASE = {
    'default_path': ':memory:',  # Can be overridden with --db flag
    'max_connections': 10,
    'timeout': 30,
    'enable_wal': True,  # Write-Ahead Logging for better concurrency
}

# ============================================================================
# HTTP CONFIGURATION
# ============================================================================

HTTP = {
    'default_timeout': 10,
    'verify_ssl': False,
    'max_retries': 3,
    'retry_delay': 1,
    'user_agent_rotation': True,
}

# ============================================================================
# PROXY CONFIGURATION
# ============================================================================

PROXY = {
    'enabled': False,
    'rotate': True,
    'default_proxy': None,
}

# ============================================================================
# ATTACK CONFIGURATION
# ============================================================================

ATTACKS = {
    'syn_flood': {
        'default_rate': 1000,  # packets per second
        'default_duration': 10,  # seconds
    },
    'udp_flood': {
        'default_rate': 1000,
        'default_duration': 10,
        'packet_size': 512,
    },
}

# ============================================================================
# OPSEC CONFIGURATION
# ============================================================================

OPSEC = {
    'enable_anti_debugging': True,
    'enable_anti_vm': True,
    'randomize_timings': True,
    'clean_logs': True,
}

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOGGING = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR
    'format': '[%(levelname)s] %(asctime)s - %(name)s: %(message)s',
    'file': None,  # Log to file if specified
    'max_file_size': 10 * 1024 * 1024,  # 10MB
}

# ============================================================================
# DATA REPOSITORY CONFIGURATION
# ============================================================================

REPOSITORIES = {
    'vkb_entries': 2000,
    'shellcode_variants': 1000,
    'user_agents': 500,
    'generate_on_init': True,
}

# ============================================================================
# SESSION CONFIGURATION
# ============================================================================

SESSION = {
    'max_history': 1000,
    'auto_save': False,
    'session_file': 'session.json',
}

# ============================================================================
# MODULES CONFIGURATION
# ============================================================================

MODULES = {
    'evasion_techniques': {
        'enabled': True,
        'memory_manipulation': True,
        'anti_debugging': True,
        'anti_vm': True,
    },
    'volumetric_attacks': {
        'enabled': True,
        'syn_flood': True,
        'udp_flood': True,
    },
    'exploitation': {
        'enabled': True,
        'web_exploits': True,
        'network_exploits': True,
    },
}

# ============================================================================
# SECURITY CONFIGURATION
# ============================================================================

SECURITY = {
    'require_target_confirmation': False,
    'enable_dry_run': True,
    'audit_logging': True,
}

# ============================================================================
# ADVANCED CONFIGURATION
# ============================================================================

ADVANCED = {
    'threading_pool_size': 10,
    'socket_buffer_size': 65535,
    'connection_keepalive': True,
}

# ============================================================================
# CONFIGURATION HELPER FUNCTIONS
# ============================================================================

def get_config(key, default=None):
    """Get configuration value by key (dot notation)."""
    parts = key.split('.')
    config = globals()
    
    for part in parts:
        if isinstance(config, dict) and part in config:
            config = config[part]
        else:
            return default
    
    return config


def set_config(key, value):
    """Set configuration value by key (dot notation)."""
    parts = key.split('.')
    config = globals()
    
    for part in parts[:-1]:
        if part not in config:
            config[part] = {}
        config = config[part]
    
    if isinstance(config, dict):
        config[parts[-1]] = value
