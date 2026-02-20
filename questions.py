from utils import print_step

def check_empty(text):
    if not text:
        return "This field cannot be empty"
    return True

def ask_question(question_text, validator=None):
    while True:
        answer = input(f"{question_text}: ").strip()
        
        if validator:
            result = validator(answer)
            if result is not True: 
                print(f"{result}")
                continue
        
        return answer
    
def get_project_title():
    print_step(1, "Project Title")
    return ask_question("Enter your project title", check_empty)

def get_project_description():
    print_step(2, "Project Description")
    return ask_question("Enter your project description", check_empty)

def get_installation_instructions():
    print_step(3, "Installation Instructions")
    return ask_question("Enter installation instructions", check_empty)

def get_usage_information():
    print_step(4, "Usage Information")
    return ask_question("Enter usage information", check_empty)

def get_license_type():
    print_step(5, "License Selection")
    
    print("\nAvailable licenses:")
    print("  a) MIT License")
    print("  b) GNU GPLv3")
    print("  c) Apache License 2.0")
    print("  d) BSD 3-Clause")
    print("  e) Mozilla Public License 2.0")
    print("  f) ISC License")
    print("  g) The Unlicense")
    
    licenses = {
        'a': 'MIT License',
        'b': 'GNU GPLv3',
        'c': 'Apache License 2.0',
        'd': 'BSD 3-Clause',
        'e': 'Mozilla Public License 2.0',
        'f': 'ISC License',
        'g': 'The Unlicense'
    }
    
    while True:
        choice = input("Choose a license (a-g): ").strip().lower()
        
        if choice in licenses:
            return licenses[choice]
        else:
            print("Please choose a valid option (a-g)")

def get_author_name():
    print_step(6, "Author Name")
    return ask_question("Enter author name", check_empty)

def get_contact_info():
    print_step(7, "Contact Information")
    return ask_question("Enter contact information (email or GitHub username)", check_empty)

def ask_all_questions():
    print("COLLECTING PROJECT INFORMATION")
    
    answers = {
        'title': get_project_title(),
        'description': get_project_description(),
        'installation': get_installation_instructions(),
        'usage': get_usage_information(),
        'license': get_license_type(),
        'author': get_author_name(),
        'contact': get_contact_info()
    }
    
    print("✅ All information collected!")
    
    return answers