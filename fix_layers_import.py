#!/usr/bin/env python3
"""
Holographic Horizon Shield - Layers Import Migration Fix
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

def backup_file(file_path: Path):
    if file_path.exists():
        backup_dir = Path(".backup") / datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_dir / file_path.name)
        print(f"   Backed up: {file_path}")

def main():
    print("🔧 Holographic Horizon Shield - Layers Migration Fix\n")

    # Pull latest
    print("1. Pulling latest changes...")
    os.system("git pull origin main --ff-only")

    # Verify target
    entropy_path = Path("layers/entropy_layer.py")
    if not entropy_path.exists():
        print("❌ ERROR: layers/entropy_layer.py not found after pull.")
        print("   You already added it manually — that's fine.")
    else:
        print(f"✅ entropy_layer found at {entropy_path}")

    # Find Python files and fix imports
    print("\n2. Fixing imports (entropy_layer → layers.entropy_layer)...")
    patterns = [
        r'^(\s*)from entropy_layer import',
        r'^(\s*)import entropy_layer',
        r'^(\s*)from \.entropy_layer import',
        r'^(\s*)from \.\.entropy_layer import',
    ]

    fixed_count = 0
    for py_file in sorted(Path(".").rglob("*.py")):
        if py_file.name.startswith("fix_") or "backup" in str(py_file):
            continue

        try:
            content = py_file.read_text(encoding="utf-8")
            original = content
            backup_file(py_file)

            for pattern in patterns:
                content = re.sub(pattern, r'\1from layers.entropy_layer import', content)

            if content != original:
                py_file.write_text(content, encoding="utf-8")
                print(f"   ✓ Fixed: {py_file}")
                fixed_count += 1
        except Exception as e:
            print(f"   ⚠️ Skipped {py_file}: {e}")

    print(f"\n✅ Done. Updated {fixed_count} file(s).")
    print("\nTry running: streamlit run shield_v2_dashboard.py")

if __name__ == "__main__":
    main()
