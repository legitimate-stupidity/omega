"""
OMEGA Database Management Module
Handles database operations for target tracking and metadata storage.
"""

import sqlite3
from ..utils.output import print_error, print_info, print_debug


class DatabaseManager:
    """
    Manages SQLite database operations for OMEGA.
    Supports both in-memory and persistent database storage.
    """
    
    def __init__(self, db_path=':memory:'):
        """
        Initialize database connection.
        
        Args:
            db_path (str): Path to database file or ':memory:' for in-memory DB
        """
        self.db_path = db_path
        self.conn = None
        self._initialize_connection()
    
    def _initialize_connection(self):
        """Establish database connection and initialize schema."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self._initialize_db()
            print_debug(f"Database initialized: {self.db_path}")
        except sqlite3.Error as e:
            print_error(f"Database initialization failed: {e}")
            self.conn = None
    
    def _initialize_db(self):
        """Create database tables if they don't exist."""
        if not self.conn:
            return
        
        cursor = self.conn.cursor()
        
        # Targets table - stores reconnaissance information
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS targets (
                id INTEGER PRIMARY KEY,
                ip_address TEXT UNIQUE,
                hostname TEXT,
                status TEXT DEFAULT 'active',
                discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_scanned TIMESTAMP
            )
        """)
        
        # Vulnerabilities table - stores found vulnerabilities
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id INTEGER PRIMARY KEY,
                target_id INTEGER,
                cve_id TEXT,
                severity INTEGER,
                description TEXT,
                discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (target_id) REFERENCES targets(id)
            )
        """)
        
        # Exploits table - tracks attempted exploitations
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exploits (
                id INTEGER PRIMARY KEY,
                target_id INTEGER,
                exploit_name TEXT,
                status TEXT,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (target_id) REFERENCES targets(id)
            )
        """)
        
        # Sessions table - tracks active sessions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY,
                target_id INTEGER,
                session_type TEXT,
                session_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (target_id) REFERENCES targets(id)
            )
        """)
        
        self.conn.commit()
    
    def add_or_get_target(self, ip_address, hostname=None):
        """
        Add a target or retrieve existing target ID.
        
        Args:
            ip_address (str): Target IP address
            hostname (str): Optional hostname
        
        Returns:
            int: Target ID
        """
        if not self.conn:
            return None
        
        cursor = self.conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO targets (ip_address, hostname) VALUES (?, ?)",
                (ip_address, hostname)
            )
            self.conn.commit()
            print_info(f"New target registered: {ip_address}")
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute(
                "SELECT id FROM targets WHERE ip_address = ?",
                (ip_address,)
            )
            result = cursor.fetchone()
            return result[0] if result else None
    
    def get_all_targets(self):
        """Retrieve all known targets."""
        if not self.conn:
            return []
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, ip_address, hostname, status FROM targets")
        return cursor.fetchall()
    
    def add_vulnerability(self, target_id, cve_id, severity, description):
        """Record a discovered vulnerability."""
        if not self.conn:
            return None
        
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO vulnerabilities 
               (target_id, cve_id, severity, description) 
               VALUES (?, ?, ?, ?)""",
            (target_id, cve_id, severity, description)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def add_exploit_attempt(self, target_id, exploit_name, status):
        """Record an exploit attempt."""
        if not self.conn:
            return None
        
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO exploits (target_id, exploit_name, status) VALUES (?, ?, ?)",
            (target_id, exploit_name, status)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_target_vulnerabilities(self, target_id):
        """Retrieve vulnerabilities for a specific target."""
        if not self.conn:
            return []
        
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT cve_id, severity, description FROM vulnerabilities WHERE target_id = ?",
            (target_id,)
        )
        return cursor.fetchall()
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
