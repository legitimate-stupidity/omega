"""
OMEGA Agent Interface Module
Command-line interface and agent orchestration.
"""

import cmd
import shlex
from ..utils import (
    Color, print_header, print_info, print_error,
    print_result, print_debug
)
from ..core import (
    DatabaseManager, OPSECManager, ActiveExploiter,
    load_core_dependencies
)
from ..repositories import DataRepository
from ..modules import (
    AdvancedEvasionTechniques,
    VolumetricAttackSimulation,
    ExploitationFramework
)
from .session import SessionState


class OmegaAgent(cmd.Cmd):
    """
    Main OMEGA Agent interface - interactive command-line controller
    for all offensive security operations.
    """
    
    intro_text = f"""{Color.HEADER}
      ___    __  __  _______   _____      ___     
     /   \  |  \/  | |  ____| /  ___|    /   \    {Color.BOLD}Project OMEGA v4.0{Color.ENDC}
    / /_\ \ |      | |  |__  |  /  ___  / /_\ \   {Color.HEADER}Advanced Persistent Attack Framework{Color.ENDC}
   |  ___  || |\/| | |   __| | |  |_  ||  ___  |  
   | |   | || |  | | |  |___ |  \__| || |   | |  
   |_|   |_||_|  |_| |______| \_____/ |_|   |_|  

Type 'help' or 'help <command>' for available commands.
Type 'exit' to quit.
"""
    
    def __init__(self, db_path=':memory:'):
        """
        Initialize OMEGA Agent.
        
        Args:
            db_path (str): Database path for persistent storage
        """
        super().__init__()
        
        print_header("OMEGA Initialization Sequence")
        
        # Load dependencies first
        print_debug("Loading dependencies...")
        load_core_dependencies()
        
        # Initialize core components
        print_debug("Initializing core infrastructure...")
        self.db = DatabaseManager(db_path)
        self.session = SessionState(self.db)
        self.opsec = OPSECManager()
        
        # Initialize data repositories
        print_debug("Initializing data repositories...")
        self.data_repo = DataRepository()
        self.opsec.load_user_agents(self.data_repo.get_user_agents().get_all())
        
        # Initialize HTTP exploiter
        self.http_exploiter = ActiveExploiter(
            opsec_manager=self.opsec,
            target_url="http://localhost"
        )
        
        # Initialize offensive modules
        print_debug("Initializing offensive modules...")
        self.evasion = AdvancedEvasionTechniques()
        self.volumetric = VolumetricAttackSimulation()
        self.exploitation = ExploitationFramework(self.http_exploiter)
        
        # Set intro and prompt
        self.intro = self.intro_text
        self._update_prompt()
        
        print_info("OMEGA Agent ready")
    
    def _update_prompt(self):
        """Update the command prompt."""
        self.prompt = self.session.get_prompt()
    
    def default(self, line):
        """Handle unknown commands."""
        if not line.strip():
            return
        
        try:
            args = shlex.split(line)
        except Exception as e:
            print_error(f"Parsing error: {e}")
            return
        
        cmd_name = args[0].lower()
        cmd_args = args[1:] if len(args) > 1 else []
        
        # Route commands to handlers
        if cmd_name == "set":
            self._handle_set(cmd_args)
        elif cmd_name == "info":
            self._handle_info(cmd_args)
        elif cmd_name == "attack":
            self._handle_attack(cmd_args)
        elif cmd_name == "exploit":
            self._handle_exploit(cmd_args)
        elif cmd_name == "list":
            self._handle_list(cmd_args)
        elif cmd_name == "target":
            self._handle_target(cmd_args)
        else:
            print_error(f"Unknown command: {cmd_name}")
    
    def _handle_set(self, args):
        """Handle 'set' commands."""
        if len(args) < 2:
            print_error("Usage: set <option> <value>")
            return
        
        option = args[0].lower()
        value = args[1]
        
        if option == "target":
            self.session.set_target(value)
            self._update_prompt()
        elif option == "proxy":
            self.opsec.set_proxy(value)
        elif option == "timeout":
            try:
                self.http_exploiter.timeout = int(value)
                print_info(f"Timeout set to {value}s")
            except ValueError:
                print_error("Timeout must be an integer")
        else:
            self.session.set_context_var(option, value)
    
    def _handle_info(self, args):
        """Handle 'info' commands."""
        print_header("OMEGA Information")
        
        if not args or args[0] == "session":
            print_result(str(self.session.get_session_info()))
        elif args[0] == "opsec":
            print_result(str(self.opsec.get_status()))
        elif args[0] == "repositories":
            status = self.data_repo.get_status()
            print_result(f"VKB Entries: {status['vkb_entries']}\n"
                       f"Shellcodes: {status['shellcodes']}\n"
                       f"User Agents: {status['user_agents']}")
        else:
            print_error(f"Unknown info type: {args[0]}")
    
    def _handle_target(self, args):
        """Handle 'target' commands."""
        if not args:
            print_error("Usage: target <command> [args]")
            return
        
        cmd = args[0].lower()
        
        if cmd == "list":
            targets = self.db.get_all_targets()
            if targets:
                print_header("Known Targets")
                for target_id, ip, hostname, status in targets:
                    print(f"  [{target_id}] {ip} ({hostname or 'Unknown'}) - {status}")
            else:
                print_info("No targets registered")
        elif cmd == "set" and len(args) > 1:
            self.session.set_target(args[1])
            self._update_prompt()
        else:
            print_error("Usage: target <list|set <ip>>")
    
    def _handle_attack(self, args):
        """Handle 'attack' commands."""
        if not args:
            print_error("Usage: attack <type> [options]")
            return
        
        target = self.session.current_target_ip
        if not target:
            print_error("Target not set. Use 'set target <ip>'")
            return
        
        attack_type = args[0].lower()
        
        if attack_type == "syn":
            if len(args) < 2:
                print_error("Usage: attack syn <port> [duration]")
                return
            try:
                port = int(args[1])
                duration = int(args[2]) if len(args) > 2 else 10
                self.volumetric.syn_flood.launch_attack(target, port, duration)
            except ValueError:
                print_error("Port and duration must be integers")
        elif attack_type == "udp":
            if len(args) < 2:
                print_error("Usage: attack udp <port> [duration] [rate]")
                return
            try:
                port = int(args[1])
                duration = int(args[2]) if len(args) > 2 else 10
                rate = int(args[3]) if len(args) > 3 else 1000
                self.volumetric.udp_flood.launch_attack(target, port, duration, rate)
            except ValueError:
                print_error("All numeric arguments must be integers")
        else:
            print_error(f"Unknown attack type: {attack_type}")
    
    def _handle_exploit(self, args):
        """Handle 'exploit' commands."""
        if not args:
            print_error("Usage: exploit <type> [options]")
            return
        
        exploit_type = args[0].lower()
        
        if exploit_type == "web_sql":
            print_error("Web exploit commands require additional setup")
        elif exploit_type == "shellcode":
            print_info("Shellcode execution framework ready")
        else:
            print_error(f"Unknown exploit type: {exploit_type}")
    
    def _handle_list(self, args):
        """Handle 'list' commands."""
        if not args:
            print_error("Usage: list <vkb|shellcodes|agents>")
            return
        
        list_type = args[0].lower()
        
        if list_type == "vkb":
            print_header("Vulnerability Knowledge Base (Sample)")
            vkb = self.data_repo.get_vkb()
            count = 0
            for cve_id, data in list(vkb.get_all().items())[:10]:
                print(f"  {cve_id}: {data['name']} (Severity: {data['severity']})")
                count += 1
            total = vkb.count()
            print(f"\n... and {total - count} more entries")
        
        elif list_type == "shellcodes":
            print_header("Shellcode Repository (Sample)")
            sr = self.data_repo.get_shellcode_repo()
            count = 0
            for name, data in list(sr.get_all().items())[:10]:
                print(f"  {name}: {data['description']}")
                count += 1
            total = sr.count()
            print(f"\n... and {total - count} more payloads")
        
        elif list_type == "agents":
            print_header("User Agent Pool (Sample)")
            ua_repo = self.data_repo.get_user_agents()
            for ua in ua_repo.get_all()[:5]:
                print(f"  {ua}")
            print(f"\n... and {ua_repo.count() - 5} more agents")
        else:
            print_error(f"Unknown list type: {list_type}")
    
    def do_help(self, arg):
        """Show help information."""
        if not arg:
            print_header("OMEGA Commands")
            print("""
  Core Commands:
    set <option> <value>     - Set configuration option or target
    info [type]              - Show system information
    target <cmd> [args]      - Manage targets
    
  Attack Commands:
    attack <type> [options]  - Launch attack
      - attack syn <port> [duration]
      - attack udp <port> [duration] [rate]
    
  Data Commands:
    list <type>              - List data repositories
      - list vkb             - Vulnerability Knowledge Base
      - list shellcodes      - Shellcode Repository
      - list agents          - User Agent Pool
    
  System Commands:
    help [cmd]               - Show this help
    exit                     - Exit OMEGA
            """)
        else:
            print_header(f"Help: {arg}")
            if arg == "set":
                print("set <option> <value> - Sets configuration options")
                print("  set target <ip>  - Set target IP address")
                print("  set proxy <url>  - Set proxy server")
            elif arg == "attack":
                print("attack <type> [options] - Launch attack on current target")
                print("  attack syn <port> [duration]")
                print("  attack udp <port> [duration] [rate]")
            else:
                print(f"No additional help for '{arg}'")
    
    def do_exit(self, arg):
        """Exit the agent."""
        print_info("Closing connections...")
        if self.http_exploiter:
            self.http_exploiter.close()
        if self.db:
            self.db.close()
        print_info("OMEGA Agent terminated")
        return True
    
    def postcmd(self, stop, line):
        """Called after every command."""
        self._update_prompt()
        return stop
    
    def emptyline(self):
        """Handle empty input."""
        pass
