"""
OMEGA OPSEC Management Module
Handles operational security features like proxy rotation, user agent spoofing, etc.
"""

import random
from ..utils.output import print_info, print_debug


class OPSECManager:
    """
    Operational Security Manager for maintaining anonymity during operations.
    Implements user agent rotation, proxy management, and other OPSEC features.
    """
    
    def __init__(self):
        """Initialize OPSEC manager with default settings."""
        self.proxy = None
        self.user_agents = self._get_default_user_agents()
        self.rotate_ua = True
        self.proxy_list = []
        self.current_proxy_index = 0
        print_debug("OPSEC Manager initialized")
    
    def _get_default_user_agents(self):
        """Get default user agents for spoofing."""
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
    
    def load_user_agents(self, ua_list):
        """
        Load custom user agent list.
        
        Args:
            ua_list (list): List of user agent strings
        """
        if ua_list:
            self.user_agents = ua_list
            print_info(f"Loaded {len(ua_list)} user agents")
    
    def get_random_ua(self):
        """
        Get a random user agent from the pool.
        
        Returns:
            str: A random user agent string
        """
        return random.choice(self.user_agents)
    
    def rotate_ua_status(self, enabled):
        """
        Enable/disable user agent rotation.
        
        Args:
            enabled (bool): Whether to rotate user agents
        """
        self.rotate_ua = enabled
        status = "enabled" if enabled else "disabled"
        print_info(f"User agent rotation {status}")
    
    def set_proxy(self, proxy_string):
        """
        Set a single proxy server.
        
        Args:
            proxy_string (str): Proxy URL (e.g., 'http://proxy.com:8080')
        """
        if proxy_string:
            self.proxy = {
                "http": proxy_string,
                "https": proxy_string
            }
            print_info(f"Proxy set to: {proxy_string}")
        else:
            self.proxy = None
            print_info("Proxy cleared")
    
    def add_proxy(self, proxy_string):
        """
        Add a proxy to the rotation pool.
        
        Args:
            proxy_string (str): Proxy URL
        """
        if proxy_string not in self.proxy_list:
            self.proxy_list.append(proxy_string)
            print_info(f"Proxy added: {proxy_string}")
    
    def set_proxy_list(self, proxy_list):
        """
        Load multiple proxies for rotation.
        
        Args:
            proxy_list (list): List of proxy URLs
        """
        self.proxy_list = proxy_list
        self.current_proxy_index = 0
        print_info(f"Loaded {len(proxy_list)} proxies for rotation")
    
    def get_rotating_proxy(self):
        """
        Get next proxy from rotation pool.
        
        Returns:
            dict: Proxy dict for requests library or None
        """
        if not self.proxy_list:
            return None
        
        proxy_url = self.proxy_list[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxy_list)
        
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    
    def get_opsec_headers(self):
        """
        Get OPSEC-compliant headers for HTTP requests.
        
        Returns:
            dict: Dictionary of HTTP headers
        """
        return {
            'User-Agent': self.get_random_ua() if self.rotate_ua else self.user_agents[0],
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
    
    def get_status(self):
        """Get current OPSEC configuration status."""
        return {
            'user_agent_rotation': self.rotate_ua,
            'proxy_enabled': self.proxy is not None,
            'proxy_list_count': len(self.proxy_list),
            'loaded_ua_count': len(self.user_agents)
        }
