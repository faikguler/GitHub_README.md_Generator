import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    print("🗒️ GitHub README.md Generator - Welcome")
    print("\nThis tool will help you create a README.md file.")
    print("❔Please answer the following questions.\n")

def print_success(filepath):
    print("✅ README.md successfully created!")
    print(f"📁 File location: {filepath}")
    
def print_error(message):
    print(f"\n❌ Error: {message}")
    
def print_info(message):
    print(f"\nℹ️ {message}")

def print_step(step_number, message):
    print(f"\n Step {step_number}: {message}")    