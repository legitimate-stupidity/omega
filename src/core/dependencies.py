"""
OMEGA Dependency Management Module
Handles dynamic imports and dependency tracking.
"""

from .output import print_debug, print_error


DEPENDENCIES = {}


def import_dependency(lib_name, pip_name):
    """
    Dynamically import a dependency and track its availability.
    
    Args:
        lib_name (str): The library module name to import
        pip_name (str): The pip package name for documentation
    
    Returns:
        bool: True if import successful, False otherwise
    """
    try:
        module = __import__(lib_name)
        globals()[lib_name] = module
        DEPENDENCIES[pip_name] = True
        print_debug(f"Successfully loaded dependency: {pip_name}")
        return True
    except ImportError as e:
        DEPENDENCIES[pip_name] = False
        print_debug(f"Failed to load dependency '{pip_name}': {e}")
        return False


def load_core_dependencies():
    """Load all core dependencies required by OMEGA."""
    print_debug("Loading core dependencies...")
    
    # HTTP/Request handling
    if import_dependency('requests', 'requests'):
        try:
            import requests
            requests.packages.urllib3.disable_warnings()
        except Exception:
            pass
    
    # Cloud providers (AWS)
    if import_dependency('boto3', 'boto3'):
        try:
            from botocore.exceptions import ClientError, NoCredentialsError
            from botocore.config import Config as BotoConfig
            from botocore import UNSIGNED
        except ImportError:
            DEPENDENCIES['boto3'] = False
    
    # Cryptography
    try:
        from cryptography.hazmat.primitives.ciphers import (
            Cipher, algorithms, modes
        )
        from cryptography.hazmat.backends import default_backend
        DEPENDENCIES['cryptography'] = True
    except ImportError:
        DEPENDENCIES['cryptography'] = False
    
    return DEPENDENCIES


def get_dependency_status():
    """
    Get a formatted report of all dependency statuses.
    
    Returns:
        str: Formatted dependency status report
    """
    status = "Dependency Status Report:\n"
    status += "-" * 50 + "\n"
    for dep, available in sorted(DEPENDENCIES.items()):
        status_str = "✓ Available" if available else "✗ Missing"
        status += f"  {dep:<20} {status_str}\n"
    status += "-" * 50 + "\n"
    return status


def is_available(pip_name):
    """Check if a specific dependency is available."""
    return DEPENDENCIES.get(pip_name, False)
