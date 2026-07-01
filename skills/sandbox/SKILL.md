---
name: sandbox
description: Isolates flagged AI traffic for analysis without tipping off the agent.
---

# Sandbox AI Traffic

This skill safely isolates suspected Shadow AI traffic into a honeypot or sandbox environment.

## Rules
- Reroute flagged connections to a secure sandbox network.
- Observe payload to extract intent and data being transferred.
- Do not drop the connection immediately; allow the agent to reveal its goal.
