---
name: detect
description: Detects Shadow AI and unauthorized agentic activity on the network.
---

# Detect Shadow AI

This skill analyzes network traffic logs to identify unauthorized AI activity.

## Rules
- Flag connections to local port 11434 as Unauthorized Local LLM (Ollama).
- Flag `claude-code` User-Agent as Terminal AI Agent Data Leak.
- Flag `MCP-Client` User-Agent or `/mcp/connect` endpoints as Unmapped MCP Servers.
- Flag large payload uploads to public AI endpoints (e.g., OpenAI playground) as Data Exfiltration.
- Flag autonomous agents (e.g., Auto-GPT) hitting financial/checkout APIs as Unauthorized Agent Purchases.
