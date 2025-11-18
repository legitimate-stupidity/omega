"""OMEGA Package"""
from src.agent import OmegaAgent, SessionState
from src.core import (
    DatabaseManager,
    OPSECManager,
    ActiveExploiter,
    load_core_dependencies
)
from src.repositories import DataRepository
from src.modules import (
    AdvancedEvasionTechniques,
    VolumetricAttackSimulation,
    ExploitationFramework
)

__version__ = "4.0"
__author__ = "H@ckbot"
__title__ = "Project OMEGA"

__all__ = [
    'OmegaAgent',
    'SessionState',
    'DatabaseManager',
    'OPSECManager',
    'ActiveExploiter',
    'DataRepository',
    'AdvancedEvasionTechniques',
    'VolumetricAttackSimulation',
    'ExploitationFramework',
    'load_core_dependencies'
]
