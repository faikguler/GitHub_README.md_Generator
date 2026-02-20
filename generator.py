import os

def generate_readme(answers):
    print("\nGenerating README.md...")
    
    content = f"# {answers['title']}\n"
    content += f"\n## Description\n{answers['description']}\n"
    content += f"\n## Installation\n{answers['installation']}\n"
    content += f"\n## Usage\n{answers['usage']}\n"
    content += f"\n## License\n{answers['license']}\n"
    content += f"\n## Author\n{answers['author']}\n"
    content += f"\n## Contact\n{answers['contact']}\n"
    
    # check output folder
    if not os.path.exists("output"):
        os.makedirs("output")
    
    filepath = os.path.join("output", "README.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath