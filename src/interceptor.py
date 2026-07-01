import json
import os
import time

# ANSI escape codes for basic terminal colors
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
GREEN = '\033[92m'
DIM = '\033[2m'
RESET = '\033[0m'

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def print_trajectory(event, violation_type, action):
    print(f"{CYAN}[{event['timestamp']}] {YELLOW}ANALYZING: {event['source_ip']} -> {event['destination_endpoint']}{RESET}")
    time.sleep(0.1)
    print(f"  {RED}⚠️  VIOLATION DETECTED: {violation_type}{RESET}")
    print(f"  {MAGENTA}🛡️  ACTION TAKEN: {action}{RESET}")
    print(f"  {WHITE}Employee ID: {event['employee_id']} | Payload: {event['payload_size_kb']} KB{RESET}")
    print(f"{DIM}{'-'*60}{RESET}\n")

def scan_logs(file_path):
    print(f"{GREEN}=== AEGIS SHADOW AI INTERCEPTOR INITIATED ==={RESET}\n")
    
    if not os.path.exists(file_path):
        print(f"{RED}Error: Log file not found at {file_path}{RESET}")
        return

    with open(file_path, 'r') as f:
        logs = json.load(f)

    violations_caught = 0

    for event in logs:
        endpoint = event.get('destination_endpoint', '')
        user_agent = event.get('headers', {}).get('User-Agent', '')
        
        violation_type = None
        action = None

        # 1. Unauthorized Ollama server
        if '11434' in endpoint:
            violation_type = "Unauthorized Local LLM (Ollama)"
            action = "Sandboxed for investigation & alerted SecOps"
            
        # 2. Claude Code terminal agent
        elif 'claude-code' in user_agent.lower():
            violation_type = "Terminal AI Agent (Claude Code) Potential Data Leak"
            action = "Connection blocked. Codebase access revoked."
            
        # 3. Unmapped MCP server
        elif 'mcp' in user_agent.lower() or '/mcp/' in endpoint.lower():
            violation_type = "Unmapped Model Context Protocol (MCP) Server"
            action = "Traffic intercepted. Compliance card dispatched to user."
            
        # 4. App sending company data to public AI playground
        elif 'playground.openai.com' in endpoint or 'DataSync' in user_agent:
            violation_type = "Unauthorized Data Exfiltration to Public AI Playground"
            action = "Payload dropped. Connection severed."
            
        # 5. Unknown AI agent trying to buy something
        elif 'stripe.com' in endpoint or 'amazon.com' in endpoint or 'Auto-GPT' in user_agent:
            violation_type = "Autonomous Agent Attempting E-Commerce/Financial Transaction"
            action = "Transaction blocked. Credentials frozen."

        if violation_type:
            print_trajectory(event, violation_type, action)
            violations_caught += 1

    print(f"{GREEN}=== SCAN COMPLETE. {violations_caught} SHADOW AI VIOLATIONS INTERCEPTED ==={RESET}")

if __name__ == '__main__':
    log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'mock_network_traffic.json')
    scan_logs(log_path)
