"""
OMEGA Session State Module
Manages user session context and state tracking.
"""

from ..utils import print_info, print_debug, Color


class SessionState:
    """
    Manages user session state including current target,
    session history, and context variables.
    """
    
    def __init__(self, db_manager):
        """
        Initialize session state.
        
        Args:
            db_manager: DatabaseManager instance
        """
        self.db = db_manager
        self.current_target_ip = None
        self.current_target_id = None
        self.session_history = []
        self.context_vars = {}
        print_debug("SessionState initialized")
    
    def set_target(self, ip_address, hostname=None):
        """
        Set the current target.
        
        Args:
            ip_address (str): Target IP address
            hostname (str): Optional hostname
        """
        target_id = self.db.add_or_get_target(ip_address, hostname)
        self.current_target_ip = ip_address
        self.current_target_id = target_id
        print_info(f"Target set to {ip_address}")
    
    def add_to_history(self, command, result=None):
        """
        Add command to session history.
        
        Args:
            command (str): Command executed
            result: Optional command result
        """
        self.session_history.append({
            'command': command,
            'result': result,
            'timestamp': __import__('datetime').datetime.now()
        })
    
    def get_prompt(self):
        """
        Get formatted command prompt.
        
        Returns:
            str: Formatted prompt string
        """
        if self.current_target_ip:
            return (f'{Color.FAIL}OMEGA({Color.WARNING}{self.current_target_ip}'
                   f'{Color.FAIL})> {Color.ENDC}')
        return f'{Color.FAIL}OMEGA> {Color.ENDC}'
    
    def set_context_var(self, key, value):
        """Set a context variable."""
        self.context_vars[key] = value
        print_debug(f"Context var {key} = {value}")
    
    def get_context_var(self, key):
        """Get a context variable."""
        return self.context_vars.get(key)
    
    def get_session_info(self):
        """Get current session information."""
        return {
            'current_target': self.current_target_ip,
            'target_id': self.current_target_id,
            'history_count': len(self.session_history),
            'context_vars': len(self.context_vars)
        }
