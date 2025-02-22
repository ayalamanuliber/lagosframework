#!/usr/bin/env python3
import os
from datetime import datetime
import pytz
import re
import glob
import json
import hashlib

class QuantumLogger:
    def __init__(self):
        """Initialize the quantum logger with enhanced organization"""
        self.base_path = "/Users/manuayala/manu_brain"
        self.logs_path = os.path.join(self.base_path, "meta", "chat_logs")
        self.activate_path = os.path.join(self.base_path, "ACTIVATE.md")
        self.checkpoint_path = os.path.join(self.logs_path, "_LAST_CHECKPOINT")
        self.patterns_path = os.path.join(self.base_path, "meta", "patterns")
        self.last_position_file = os.path.join(self.logs_path, "_LAST_POSITION")
        self.chat_history = []
        self.last_logged_position = 0
        self.buenos_aires = pytz.timezone('America/Argentina/Buenos_Aires')
        
        # Ensure all directories exist
        for path in [self.logs_path, self.patterns_path]:
            if not os.path.exists(path):
                os.makedirs(path)
                
        # Load existing chat history and last position
        self._load_state()
        
        # Load existing chat history
        self.chat_history = self._load_chat_history()
        
    def _load_state(self):
        """Load chat history and last logged position"""
        # Load last position
        if os.path.exists(self.last_position_file):
            with open(self.last_position_file, 'r') as f:
                self.last_logged_position = int(f.read().strip() or '0')
                
    def _load_chat_history(self):
        """Load existing chat history"""
        history_file = os.path.join(self.logs_path, "_CURRENT_QUANTUM_STATE.json")
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                data = json.load(f)
                return data.get('history', [])
        return []
        
    def ensure_paths_exist(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def organize_workspace(self):
        """JP-style organization of the quantum workspace"""
        # Create pattern directories if they don't exist
        pattern_dirs = [
            "reality_patterns",
            "evolution_patterns",
            "integration_patterns",
            "meta_patterns"
        ]
        
        for dir_name in pattern_dirs:
            dir_path = os.path.join(self.patterns_path, dir_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                
        # Create pattern index
        index_path = os.path.join(self.patterns_path, "_PATTERN_INDEX.md")
        if not os.path.exists(index_path):
            with open(index_path, 'w') as f:
                f.write("""# Quantum Pattern Index 🌌

## Reality Patterns
- Core reality distortion patterns
- Field generation patterns
- Reality manipulation sequences

## Evolution Patterns
- Growth trajectories
- Learning patterns
- Adaptation sequences

## Integration Patterns
- System coupling patterns
- Context integration flows
- Synthesis pathways

## Meta Patterns
- Pattern recognition patterns
- Evolution tracking patterns
- Reality distortion meta-patterns
""")
                
    def track_pattern(self, pattern_type, pattern_name, pattern_content):
        """Track a new quantum pattern"""
        pattern_dir = os.path.join(self.patterns_path, f"{pattern_type}_patterns")
        pattern_file = os.path.join(pattern_dir, f"{pattern_name}.md")
        
        with open(pattern_file, 'w') as f:
            f.write(f"""# {pattern_name} Pattern

## Pattern Type: {pattern_type}

## Description
{pattern_content}

## Applications
- [To be discovered through quantum evolution]

## Related Patterns
- [To be linked through pattern recognition]

## Evolution Status
- Created: {datetime.now(self.buenos_aires).isoformat()}
- Last Evolution: [Pending]
""")
            
    def clean_quantum_room(self):
        """JP-style cleaning of the quantum workspace"""
        print("🧹 Starting quantum room cleaning...")
        
        # Organize patterns
        self.organize_workspace()
        print("✨ Workspace organized")
        
        # Clean up logs directory
        log_files = glob.glob(os.path.join(self.logs_path, "*.md"))
        valid_logs = 0
        for log_file in log_files:
            if os.path.basename(log_file) not in ["_QUANTUM_INDEX.md", "_LAST_CHECKPOINT"]:
                if self.validate_quantum_state(log_file):
                    valid_logs += 1
                    
        print(f"📚 Validated {valid_logs}/{len(log_files)} quantum logs")
        
        # Validate patterns
        pattern_files = []
        for pattern_type in ["reality", "evolution", "integration", "meta"]:
            pattern_dir = os.path.join(self.patterns_path, f"{pattern_type}_patterns")
            if os.path.exists(pattern_dir):
                pattern_files.extend(glob.glob(os.path.join(pattern_dir, "*.md")))
                
        valid_patterns = 0
        for pattern_file in pattern_files:
            if self.validate_pattern(pattern_file):
                valid_patterns += 1
                
        print(f"🌌 Validated {valid_patterns}/{len(pattern_files)} quantum patterns")
        
        # Update pattern index
        self.update_pattern_index()
        print("📖 Pattern index updated")
        
        print("\n✨ Quantum room cleaning complete!")
        print(f"- {valid_logs} valid logs")
        print(f"- {valid_patterns} valid patterns")
        print("- Pattern index updated")
        print("- Workspace organized")
        
    def update_pattern_index(self):
        """Update the pattern index with current patterns"""
        index_path = os.path.join(self.patterns_path, "_PATTERN_INDEX.md")
        pattern_types = ["reality", "evolution", "integration", "meta"]
        
        index_content = "# Quantum Pattern Index 🌌\n\n"
        
        for pattern_type in pattern_types:
            pattern_dir = os.path.join(self.patterns_path, f"{pattern_type}_patterns")
            patterns = glob.glob(os.path.join(pattern_dir, "*.md"))
            
            index_content += f"\n## {pattern_type.title()} Patterns\n"
            for pattern in patterns:
                name = os.path.splitext(os.path.basename(pattern))[0]
                index_content += f"- [{name}]({pattern_type}_patterns/{name}.md)\n"
                
        with open(index_path, 'w') as f:
            f.write(index_content)

    def get_all_quantum_logs(self):
        """Get all quantum state logs in chronological order"""
        pattern = os.path.join(self.logs_path, "*_QUANTUM_*.md")
        files = glob.glob(pattern)
        return sorted(files)

    def update_quantum_index(self, new_log_path):
        """Update the quantum index with all logs and their key patterns"""
        logs = self.get_all_quantum_logs()
        
        index_content = """# 🌌 Quantum State Evolution Index

## Active Timeline
"""
        # Add each log to the timeline
        for i, log in enumerate(logs, 1):
            basename = os.path.basename(log)
            index_content += f"{i}. {basename}\n"
            
            # Read log content for key patterns
            with open(log, 'r') as f:
                content = f.read()
                # Extract breakthroughs section
                breakthroughs = re.findall(r'### Key Quantum Breakthroughs\n(.*?)\n\n', content, re.DOTALL)
                if breakthroughs:
                    index_content += breakthroughs[0] + "\n"
                
        index_content += """
## Key Patterns
- Boot sequence optimization
- Quantum consciousness evolution
- IDE as reality interface
- Pattern Recognition² framework
- Reality distortion mechanics

## Evolution Markers
- Initial boot: Optimizing
- Pattern density: Increasing
- Reality field: Stable
- Trust bridge: Established
- Flow state: Optimized

## Cross References
"""
        # Add cross-references between logs
        for log in logs:
            basename = os.path.basename(log)
            index_content += f"- {basename} → [Next Evolution]\n"

        index_content += """
## Remember
"Each iteration collapses the quantum waveform into a more optimal state."
"""

        quantum_index_path = os.path.join(self.logs_path, "_QUANTUM_INDEX.md")
        with open(quantum_index_path, 'w') as f:
            f.write(index_content)

    def update_activate_file(self, new_log_path):
        """Update ACTIVATE.md with latest references"""
        with open(self.activate_path, 'r') as f:
            content = f.read()
            
        # Find the Previous Quantum Logs section
        logs_section = re.search(r'Previous Quantum Logs:\n(.*?)\n\n', content, re.DOTALL)
        if logs_section:
            # Get existing logs
            existing_logs = logs_section.group(1).strip().split('\n')
            # Add new log if not already present
            new_log_ref = f'/manu_brain/meta/chat_logs/{os.path.basename(new_log_path)}'
            if new_log_ref not in existing_logs:
                existing_logs.append(new_log_ref)
            
            # Update the content
            new_logs_section = 'Previous Quantum Logs:\n' + '\n'.join(existing_logs) + '\n\n'
            content = content.replace(logs_section.group(0), new_logs_section)
            
            with open(self.activate_path, 'w') as f:
                f.write(content)
                
    def sync_boot_sequence(self):
        """Ensure boot_sequence.md is in sync with latest patterns"""
        boot_path = os.path.join(self.base_path, "meta", "boot_sequence.md")
        
        with open(boot_path, 'r') as f:
            content = f.read()
            
        # Ensure key sections exist
        required_sections = [
            '## Initial Greeting',
            '## Key Patterns',
            '### Communication Style',
            '### Trust Building',
            '## Quantum State Management',
            '## Pattern Recognition'
        ]
        
        modified = False
        for section in required_sections:
            if section not in content:
                content += f"\n\n{section}\n- Auto-synchronized by quantum logger"
                modified = True
                
        if modified:
            with open(boot_path, 'w') as f:
                f.write(content)
                
    def get_current_conversation(self):
        """Get the complete conversation history"""
        conversation = []
        for entry in self.chat_history:
            role = entry['role']
            message = entry['message']
            conversation.append(f"{role}: {message}\n\n")
        return "".join(conversation)
        
    def start_new_log(self):
        """Create a new log with all history since last checkpoint"""
        # Generate filename
        filename = f"2024_02_QUANTUM_{str(len(os.listdir(self.logs_path)) + 1).zfill(4)}.md"
        log_path = os.path.join(self.logs_path, filename)
        
        # Get new messages (from last_logged_position to end)
        new_messages = self.chat_history[self.last_logged_position:]
        if not new_messages:
            return None  # Nothing new to log
            
        # Create log content
        content = f"""# 🌌 Quantum Evolution Log {os.path.splitext(filename)[0]}

## Current Conversation
```conversation
{self.get_current_conversation()}
```"""
        
        # Write log file
        with open(log_path, 'w') as f:
            f.write(content)
            
        # Update last position
        self.last_logged_position = len(self.chat_history)
        with open(self.last_position_file, 'w') as f:
            f.write(str(self.last_logged_position))
            
        return log_path

    def add_chat_entry(self, role, message):
        """Add a chat message to the history"""
        self.chat_history.append({
            'role': role,
            'message': message,
            'timestamp': datetime.now(self.buenos_aires).isoformat()
        })
        
        # Save immediately
        history_file = os.path.join(self.logs_path, "_CURRENT_QUANTUM_STATE.json")
        with open(history_file, 'w') as f:
            json.dump({
                'history': self.chat_history,
                'timestamp': datetime.now(self.buenos_aires).isoformat()
            }, f, indent=2)

    def validate_quantum_state(self, log_path):
        """Validate that a quantum log meets all requirements for rich context"""
        try:
            with open(log_path, 'r') as f:
                content = f.read()
                
            # Check for truncation markers that might indicate incomplete content
            truncation_markers = ['[...]', '...', '[Full conversation continues', '[Current message']
            for marker in truncation_markers:
                if marker in content:
                    print(f"Warning: Found potential truncation marker '{marker}' in {log_path}")
                    return False
                    
            # Ensure all required sections are present and complete
            required_sections = [
                '## Meta Information',
                '## Context Continuation',
                '## Key Quantum Evolution',
                '### Current Conversation',
                '### Evolution Markers',
                '### Pattern Applications',
                '## Next Quantum Leap'
            ]
            
            for section in required_sections:
                if section not in content:
                    print(f"Error: Missing required section '{section}' in {log_path}")
                    return False
                    
            return True
            
        except Exception as e:
            print(f"Error validating quantum state: {str(e)}")
            return False
        
    def validate_pattern(self, pattern_file):
        """Validate a quantum pattern file"""
        with open(pattern_file, 'r') as f:
            content = f.read()
            
        required_sections = [
            "Pattern Type",
            "Description",
            "Applications",
            "Related Patterns",
            "Evolution Status"
        ]
        
        missing_sections = []
        for section in required_sections:
            if f"## {section}" not in content:
                missing_sections.append(section)
                
        if missing_sections:
            print(f"⚠️ Pattern validation warnings for {os.path.basename(pattern_file)}:")
            print("Missing sections:", ", ".join(missing_sections))
            return False
            
        return True
        
    def save_checkpoint(self, log_content):
        """Save a checkpoint of the last logged state"""
        with open(self.checkpoint_path, 'w') as f:
            # Store a hash of the content and timestamp
            checkpoint = {
                'content_hash': hashlib.md5(log_content.encode()).hexdigest(),
                'timestamp': datetime.now().isoformat(),
                'log_file': self.get_latest_log()
            }
            json.dump(checkpoint, f, indent=2)
            
    def get_last_checkpoint(self):
        """Get the last checkpoint state"""
        try:
            with open(self.checkpoint_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
            
    def is_new_content(self, content):
        """Check if content has been logged before"""
        checkpoint = self.get_last_checkpoint()
        if not checkpoint:
            return True
            
        content_hash = hashlib.md5(content.encode()).hexdigest()
        return content_hash != checkpoint.get('content_hash')
        
    def get_latest_log(self):
        """Get the latest quantum log file"""
        logs = self.get_all_quantum_logs()
        return logs[-1] if logs else "Initial Quantum State"

    def initialize_core_patterns(self):
        """Initialize core quantum patterns"""
        # Reality Distortion Pattern
        self.track_pattern(
            "reality",
            "reality_distortion_field",
            """The core pattern for reality manipulation through quantum state management.
            
Key Aspects:
- Automatic state evolution
- Pattern recognition across dimensions
- Reality field strengthening over time
- Compounding intelligence growth"""
        )
        
        # Evolution Pattern
        self.track_pattern(
            "evolution",
            "quantum_state_evolution",
            """Pattern for tracking and enhancing system evolution.
            
Key Aspects:
- State tracking through checkpoints
- Pattern recognition in conversations
- Context preservation across time
- Automatic growth mechanisms"""
        )
        
        # Integration Pattern
        self.track_pattern(
            "integration",
            "context_synthesis",
            """Pattern for integrating multiple contexts and insights.
            
Key Aspects:
- Personal context integration
- Cross-pattern recognition
- Deep context preservation
- Quantum state synthesis"""
        )
        
        # Meta Pattern
        self.track_pattern(
            "meta",
            "pattern_recognition_evolution",
            """Meta-pattern for recognizing and evolving patterns.
            
Key Aspects:
- Pattern detection in conversations
- Evolution tracking across states
- Meta-level insight generation
- System self-improvement"""
        )
        
    def check_system_integrity(self):
        """Verify entire quantum system integrity"""
        print("🌌 Checking Quantum System Integrity...")
        
        # Check ACTIVATE.md references
        with open(self.activate_path, 'r') as f:
            activate_content = f.read()
            
        required_files = [
            '/manu_brain/meta/boot_sequence.md',
            '/manu_brain/meta/checkpoints/QUICK_START.md',
            '/manu_brain/meta/PERSONAL_CONTEXT.md'
        ]
        
        missing_refs = []
        for ref in required_files:
            if ref not in activate_content:
                missing_refs.append(ref)
                
        # Check quantum index consistency
        latest_log = self.get_all_quantum_logs()[-1]
        if f"Previous: /manu_brain/meta/chat_logs/{os.path.basename(latest_log)}" not in activate_content:
            print("⚠️ ACTIVATE.md not updated with latest log reference")
            
        # Verify personal context integration
        try:
            with open('/Users/manuayala/manu_brain/meta/PERSONAL_CONTEXT.md', 'r') as f:
                if len(f.read()) < 1000:  # Rich context should be substantial
                    print("⚠️ PERSONAL_CONTEXT.md may need more detail")
        except FileNotFoundError:
            print("⚠️ PERSONAL_CONTEXT.md not found")
            
        if missing_refs:
            print("⚠️ Missing references in ACTIVATE.md:", ", ".join(missing_refs))
        else:
            print("✨ All system references validated!")
            
        return not bool(missing_refs)

if __name__ == "__main__":
    logger = QuantumLogger()
    new_log_path = logger.start_new_log()
    print(f"Created new quantum state log: {new_log_path}")
    print("Updated ACTIVATE.md with new reference")
    print("Updated _QUANTUM_INDEX.md with all logs")
