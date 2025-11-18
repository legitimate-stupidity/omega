#!/usr/bin/env python3
"""
OMEGA v4.0 - Verification Script
Verify that all modules are properly organized and importable.
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def verify_imports():
    """Verify all modules can be imported."""
    print("=" * 60)
    print("PROJECT OMEGA v4.0 - Module Verification")
    print("=" * 60)
    
    results = {
        'passed': [],
        'failed': []
    }
    
    # Utility modules
    print("\n[1/4] Verifying Utility Modules...")
    try:
        from src.utils import print_header, print_info, print_error
        results['passed'].append("✓ src.utils")
        print("  ✓ Output formatting module")
    except Exception as e:
        results['failed'].append(f"✗ src.utils: {e}")
        print(f"  ✗ Output formatting: {e}")
    
    # Core modules
    print("\n[2/4] Verifying Core Infrastructure...")
    try:
        from src.core import (
            DatabaseManager,
            OPSECManager,
            ActiveExploiter,
            load_core_dependencies
        )
        results['passed'].append("✓ src.core")
        print("  ✓ Database management")
        print("  ✓ OPSEC features")
        print("  ✓ HTTP exploitation")
        print("  ✓ Dependency management")
    except Exception as e:
        results['failed'].append(f"✗ src.core: {e}")
        print(f"  ✗ Core modules: {e}")
    
    # Repository modules
    print("\n[3/4] Verifying Data Repositories...")
    try:
        from src.repositories import (
            VulnerabilityKnowledgeBase,
            ShellcodeRepository,
            UserAgentRepository,
            DataRepository
        )
        results['passed'].append("✓ src.repositories")
        print("  ✓ Vulnerability Knowledge Base")
        print("  ✓ Shellcode repository")
        print("  ✓ User agent repository")
        print("  ✓ Data repository coordinator")
    except Exception as e:
        results['failed'].append(f"✗ src.repositories: {e}")
        print(f"  ✗ Repositories: {e}")
    
    # Offensive modules
    print("\n[4/4] Verifying Offensive Modules...")
    try:
        from src.modules import (
            AdvancedEvasionTechniques,
            VolumetricAttackSimulation,
            ExploitationFramework
        )
        results['passed'].append("✓ src.modules.evasion")
        results['passed'].append("✓ src.modules.offensive")
        results['passed'].append("✓ src.modules.exploitation")
        print("  ✓ Advanced evasion techniques")
        print("  ✓ Volumetric attacks")
        print("  ✓ Exploitation framework")
    except Exception as e:
        results['failed'].append(f"✗ src.modules: {e}")
        print(f"  ✗ Offensive modules: {e}")
    
    # Agent modules
    print("\n[5/5] Verifying Agent Interface...")
    try:
        from src.agent import OmegaAgent, SessionState
        results['passed'].append("✓ src.agent")
        print("  ✓ CLI agent")
        print("  ✓ Session management")
    except Exception as e:
        results['failed'].append(f"✗ src.agent: {e}")
        print(f"  ✗ Agent: {e}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"✓ Passed: {len(results['passed'])}")
    print(f"✗ Failed: {len(results['failed'])}")
    
    if results['failed']:
        print("\nFailed imports:")
        for fail in results['failed']:
            print(f"  {fail}")
    
    if not results['failed']:
        print("\n✓ All modules verified successfully!")
        print("✓ Project OMEGA v4.0 is ready to use")
        print("\nTo start OMEGA:")
        print("  python omega.py")
        print("\nFor help:")
        print("  python omega.py --help")
        print("  See docs/README.md for complete guide")
        return 0
    else:
        print("\n✗ Some modules failed verification")
        print("Check installation and PYTHONPATH")
        return 1


def verify_file_structure():
    """Verify all required files exist."""
    print("\n" + "=" * 60)
    print("FILE STRUCTURE VERIFICATION")
    print("=" * 60)
    
    required_files = {
        'Source Code': [
            'src/__init__.py',
            'src/utils/__init__.py',
            'src/utils/output.py',
            'src/core/__init__.py',
            'src/core/dependencies.py',
            'src/core/database.py',
            'src/core/opsec.py',
            'src/core/exploiter.py',
            'src/repositories/__init__.py',
            'src/repositories/data_repository.py',
            'src/modules/__init__.py',
            'src/modules/evasion/__init__.py',
            'src/modules/evasion/advanced_evasion.py',
            'src/modules/offensive/__init__.py',
            'src/modules/offensive/volumetric_attacks.py',
            'src/modules/exploitation/__init__.py',
            'src/modules/exploitation/exploit_framework.py',
            'src/agent/__init__.py',
            'src/agent/session.py',
            'src/agent/agent.py',
        ],
        'Configuration': [
            'config/config.py',
        ],
        'Documentation': [
            'docs/README.md',
            'docs/ARCHITECTURE.md',
            'docs/MODULES.md',
            'docs/SETUP.md',
            'docs/COMPLETION_SUMMARY.md',
            'docs/INDEX.md',
        ],
        'Root Files': [
            'omega.py',
            'requirements.txt',
            'README.md',
        ]
    }
    
    missing = []
    found = []
    
    for category, files in required_files.items():
        print(f"\n{category}:")
        for file_path in files:
            if os.path.exists(file_path):
                print(f"  ✓ {file_path}")
                found.append(file_path)
            else:
                print(f"  ✗ {file_path}")
                missing.append(file_path)
    
    print("\n" + "=" * 60)
    print(f"✓ Found: {len(found)}/{len(found) + len(missing)} files")
    
    if missing:
        print(f"✗ Missing: {len(missing)} files")
        for f in missing:
            print(f"  - {f}")
        return 1
    else:
        print("✓ All required files present!")
        return 0


def main():
    """Run all verifications."""
    print("\n")
    
    file_status = verify_file_structure()
    import_status = verify_imports()
    
    print("\n" + "=" * 60)
    print("FINAL STATUS")
    print("=" * 60)
    
    if file_status == 0 and import_status == 0:
        print("✓ PROJECT OMEGA v4.0 VERIFICATION COMPLETE")
        print("✓ All systems operational")
        print("\nReady to deploy!")
        return 0
    else:
        print("✗ VERIFICATION FAILED")
        print("Check errors above and fix any issues")
        return 1


if __name__ == '__main__':
    sys.exit(main())
