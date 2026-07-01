# AegisAI: Enterprise Shadow AI Auto-Remediator 🛡️

AegisAI is a production-grade autonomous **Policy Server and Governance Interceptor** designed to protect enterprise networks from the hidden risks of "Shadow AI"[cite: 2]. Built entirely via agentic vibe coding using Gemini 3.1 Pro High inside the Antigravity framework, this project demonstrates a self-contained pipeline that intercepts rogue AI traffic, validates threats inside an ephemeral sandbox, and forces deterministic remediation using interactive Generative UI[cite: 1, 2].

## 🚨 The Problem: The Shadow AI Crisis
With the rise of local LLMs and autonomous developer tooling, corporate security teams are facing a massive blind spot[cite: 2]. Employees are spinning up unauthorized local model endpoints, connecting untracked Model Context Protocol (MCP) servers, and exfiltrating sensitive data arrays to public AI playgrounds[cite: 2]. AegisAI acts as a zero-trust gateway to continuously audit log streams and enforce enterprise compliance rules automatically[cite: 2].

---

## 🏗️ Core Architecture & Course Blueprint Implementation
AegisAI bridges the gap between fast prototyping and robust, production-grade agentic engineering by implementing five core pillars from the intensive course framework:

### 1. Spec-Driven Development (SDD)
* The system configuration is completely decoupled from transient code logic[cite: 2]. 
* The absolute source of truth is established using behavior-driven Gherkin specifications (`specs/governance.feature`)[cite: 2].
* Testing and verification logic are automatically aligned against these strict specifications to guarantee programmatic compliance[cite: 2].

### 2. Context Engineering & Progressive Disclosure
* To eliminate "Context Rot" and prevent high model latency, the system avoids loading dense, monolithic compliance rulebooks into the main prompt loop[cite: 2].
* Instead, it implements **Progressive Disclosure** via dynamic **Agent Skills** (`skills/`)[cite: 2].
* Dense domain schemas and tracking runbooks are wrapped into modular directories and loaded strictly on-demand when triggered by specific network signatures[cite: 2].

### 3. Policy Server Interception & Ephemeral Sandboxing
* Acting as a standalone enterprise checkpoint, the core script functions as a high-velocity **Policy Server**[cite: 2].
* When a high-impact mutation or security violation signature is detected (e.g., a rogue local Ollama port handshake or unmapped MCP headers), the network payload is isolated[cite: 2].
* The system routes threats to an **Ephemeral Sandbox layer** for immediate verification without modifying or endangering local machine environment configurations[cite: 2].

### 4. OpenTelemetry Trajectory Tracking
* Traditional assertion checks are replaced with **Trajectory Evaluation** spans[cite: 2].
* Every internal step—from baseline routing and skill execution up to final validation status flags—is systematically logged chronologically to ensure perfect auditability and transparency for security operators[cite: 2].

### 5. Agent-to-User Interface (A2UI) & Human-in-the-Loop (HITL)
* Destructive actions require continuous trust validation[cite: 2].
* When a high-risk connection is confirmed, AegisAI triggers a mandatory **HITL execution halt state**[cite: 2].
* The system dynamically compiles a declarative HTML/CSS compliance component card, placing active control vectors directly into the supervisor's dashboard to allow manual override authorization or immediate connection termination[cite: 2].

---

## 📂 Repository Workspace Structure
```text
aegis_ai_remediator/
│
├── specs/
│   └── governance.feature             # The behavioral absolute truth (SDD specs)
│
├── logs/
│   └── mock_network_traffic.json      # Ingested enterprise JSON log pipelines
│
├── skills/                            # Procedural Memory & Progressive Skills
│   ├── detect/                        # Interception routing intent runbooks
│   ├── sandbox/                       # Isolated verification testing scripts
│   └── remediator/                    # A2UI declarative presentation logic
│
└── src/
    ├── interceptor.py                 # Core Policy Engine runtime harness
    └── compliance_card.html           # Compiled Generative UI enforcement component
