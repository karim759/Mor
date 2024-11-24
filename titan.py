import os
import subprocess
import json

# Step 1: Install Required Packages
def install_packages():
    print("Installing required packages...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install -y git openssh gh")

# Step 2: Authenticate with GitHub CLI
def authenticate_github():
    print("Authenticating with GitHub...")
    os.system("gh auth login")

# Step 3: List available Codespaces
def list_codespaces():
    print("Fetching available Codespaces...")
    result = subprocess.run(["gh", "codespace", "list", "--json", "name"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error fetching codespaces.")
        return None
    codespaces = json.loads(result.stdout)
    return [cs["name"] for cs in codespaces]

# Step 4: Select and Connect to Codespace
def connect_to_codespace(codespaces):
    print("\nAvailable Codespaces:")
    for i, cs in enumerate(codespaces, 1):
        print(f"{i}. {cs}")
    
    selection = int(input("\nEnter the number of the Codespace you want to open: "))
    if 1 <= selection <= len(codespaces):
        selected_cs = codespaces[selection - 1]
        print(f"Connecting to {selected_cs}...")
        os.system(f"gh codespace ssh --codespace {selected_cs}")
    else:
        print("Invalid selection. Exiting.")

# Main function
def main():
    install_packages()
    authenticate_github()
    codespaces = list_codespaces()
    if codespaces:
        connect_to_codespace(codespaces)
    else:
        print("No Codespaces available.")

if __name__ == "__main__":
    main()
