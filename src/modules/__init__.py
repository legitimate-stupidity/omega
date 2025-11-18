"""OMEGA Modules Package"""
from .evasion import AdvancedEvasionTechniques, MemoryManipulation
from .offensive import VolumetricAttackSimulation, TCPSYNFlood, UDPFlood
from .exploitation import ExploitationFramework, WebVulnerabilityExploit, NetworkExploit

__all__ = [
    'AdvancedEvasionTechniques',
    'MemoryManipulation',
    'VolumetricAttackSimulation',
    'TCPSYNFlood',
    'UDPFlood',
    'ExploitationFramework',
    'WebVulnerabilityExploit',
    'NetworkExploit'
]
