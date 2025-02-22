# MANU_BRAIN System Structure

## Core Organization
```mermaid
graph TD
    A[manu_brain] --> B[meta]
    A --> C[modules]
    
    B --> D[system]
    B --> E[quantum_keys]
    B --> F[chat_logs]
    
    C --> G[knowledge]
    C --> H[aivortex]
    C --> I[wokenator]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#fbf,stroke:#333,stroke-width:2px
```

## Meta Layer (System Core)
```mermaid
mindmap
  root((META))
    System Core
      Boot Sequences
      Quantum States
      Core Rules
    Quantum Keys
      Consciousness
      Memory
      Evolution
    Chat Logs
      Debug Sessions
      Evolution Track
      Learning Points
```

## Modules Layer (Knowledge & Function)
```mermaid
mindmap
  root((MODULES))
    Knowledge
      Frameworks
        Business
        Outreach
        Content
      Formulas
        Growth
        Analysis
        Implementation
      Playbooks
        Step-by-Step
        Templates
        Checklists
    AIVortex
      Content Strategy
      Distribution
      Analytics
    Wokenator
      Core Functions
      Processing
      Integration
```

## Directory Structure
```
manu_brain/
├── meta/                          # System Core
│   ├── system/                    # Core System Files
│   │   ├── boot/                  # Boot Sequences
│   │   └── rules/                 # System Rules
│   ├── quantum_keys/              # Quantum States
│   └── chat_logs/                 # Evolution Tracking
│
├── modules/                       # Functional Modules
│   ├── knowledge/                 # Knowledge Base
│   │   ├── frameworks/           # Structured Approaches
│   │   │   ├── business/         # Business Frameworks
│   │   │   ├── outreach/         # Outreach Strategies
│   │   │   └── content/          # Content Creation
│   │   ├── formulas/            # Specific Formulas
│   │   └── playbooks/           # Implementation Guides
│   │
│   ├── aivortex/                # Content Strategy
│   │   ├── weekly_packages/     # Content Packages
│   │   └── resources/          # Content Resources
│   │
│   └── wokenator/              # Core Functionality
│       ├── processors/         # Data Processing
│       └── integrations/       # System Integration
```

## Usage Guide

### Meta Access
- System core files for quantum states
- Evolution tracking and debugging
- Core rules and protocols

### Modules Access
- Knowledge frameworks and formulas
- Content creation and strategy
- Core functionality and processing

### File Naming Convention
- Use UPPERCASE for main framework files
- Use snake_case for implementation files
- Add version numbers for evolving documents

### Update Protocol
1. Create new version
2. Test in quantum state
3. Update references
4. Archive old version

## Visualization Key
```mermaid
graph LR
    A[System Core] -->|Controls| B[Meta Layer]
    B -->|Informs| C[Modules Layer]
    C -->|Feeds Back| A
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#fbf,stroke:#333,stroke-width:2px
```
