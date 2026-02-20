def get_project_title():
    print("get_project_title() called")
    return "My Project"

def get_project_description():
    print("get_project_description() called")
    return "Project description"

def get_installation_instructions():
    print("get_installation_instructions() called")
    return "Installation instructions" 

def get_usage_information():
    print("get_usage_information() called")
    return "Usage information" 

def get_license_type():
    print("get_license_type() called")
    return "MIT License"

def get_author_name():
    print("get_author_name() called")
    return "Author name" 

def get_contact_info():
    print("get_contact_info() called")
    return "Contact info" 

def ask_all_questions():
    print("\nask_all_questions() called")
    
    answers = {
        'title': get_project_title(),
        'description': get_project_description(),
        'installation': get_installation_instructions(),
        'usage': get_usage_information(),
        'license': get_license_type(),
        'author': get_author_name(),
        'contact': get_contact_info()
    }
    

    return answers