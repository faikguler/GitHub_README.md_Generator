import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import clear_screen, print_welcome, print_error
from questions import ask_all_questions
from generator import generate_readme 

def main():
    try:
        # Clear screen and show welcome message
        clear_screen()
        print_welcome()
        
        answers = ask_all_questions()
        
        output_path = generate_readme(answers)
        
        print("\n === Program Finished ===")
        print(f"README saved to: {output_path}")
    except Exception as e:
        print_error(f"An error occurred: {e}")
    
    input("\n Press Enter to exit...")

if __name__ == "__main__":
    main()