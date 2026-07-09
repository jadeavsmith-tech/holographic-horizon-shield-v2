#!/usr/bin/env python3
"""
Simple migration script for entropy_layer.py after refactor.
- Pulls latest changes
- Updates imports across the project
"""

import os
import re
import subprocess
from pathlib import Path

def run_command(cmd):
    print(f"→ Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)
    return result.returncode == 0

def main():
    print("🔄 Starting entropy_layer migration...")

    # 1. Pull latest changes
    print("\n1. Pulling latest from main...")
    run_command("git pull origin main")

    # 2. Verify file location
    layer_path = Path("layers/entropy_layer.py")
    if layer_path.exists():
        print(f"✅ Found entropy layer at {layer_path}")
    else:
        print("❌ entropy_layer.py not found in layers/ — check git pull")
        return

    # 3. Find and fix old imports
    print("\n2. Updating imports across project...")
    old_import_patterns = [
        r'from entropy_layer import',
        r'import entropy_layer',
        r'from \.entropy_layer import',   # relative
    ]

    new_import = "from layers.entropy_layer import"

    for py_file in Path(".").rglob("*.py"):
        if py_file.name == "migrate_entropy_layer.py":
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
            updated = content
            for pattern in old_import_patterns:
                updated = re.sub(pattern, new_import, updated)
            
            if updated != content:
                py_file.write_text(updated, encoding="utf-8")
                print(f"   Updated: {py_file}")
        except Exception as e:
            print(f"   Skip {py_file}: {e}")

    print("\n✅ Migration complete!")
    print("\nNext: Run `python -m pytest` or test your shield to verify.")

if __name__ == "__main__":
    main()
