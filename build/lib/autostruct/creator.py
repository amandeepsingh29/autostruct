import os
import re
import argparse

def create_project_structure(structure_file, base_path="."):
    with open(structure_file, "r", encoding="utf-8") as f:
        structure_text = f.read()
    
    lines = structure_text.strip().split("\n")
    stack = []
    
    for line in lines:
        item_name = re.sub(r'^[│\s─]+', '', line).strip()
        indent_level = line.count("│")  # Count hierarchy depth based on │
        
        while stack and stack[-1][1] >= indent_level:
            stack.pop()
        
        is_directory = item_name.endswith("/")
        item_name = item_name.rstrip("/")  # Remove trailing slash if present
        
        current_path = os.path.join(base_path, *[folder for folder, _ in stack], item_name)
        
        if is_directory:
            os.makedirs(current_path, exist_ok=True)
            stack.append((item_name, indent_level))
        else:
            os.makedirs(os.path.dirname(current_path), exist_ok=True)
            with open(current_path, "w") as f:
                pass  # Create an empty file

def main():
    parser = argparse.ArgumentParser(description="Create a project structure from a text file.")
    parser.add_argument("structure_file", help="Path to the structure file")
    args = parser.parse_args()
    
    create_project_structure(args.structure_file)

if __name__ == "__main__":
    main()