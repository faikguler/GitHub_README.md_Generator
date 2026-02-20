import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import clear_screen, print_welcome
from questions import ask_all_questions

def generate_readme(answers):
    print("\ngenerate_readme() called")
    return "output/README.md"

def main():
    """Main program function"""

    # Clear screen and show welcome message
    clear_screen()
    print_welcome()
    
    print("\n main() calling ask_all_questions()")
    answers = ask_all_questions()
    
    print("\n main() calling generate_readme()")
    output_path = generate_readme(answers)
    
    print("\n === Program Finished ===")
    print(f"README would be saved to: {output_path}")
    
    input("\n Press Enter to exit...")

if __name__ == "__main__":
    main()