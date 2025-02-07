import re
from auth import update_auth_token

def extract_auth_from_curl(curl_command):
    # Regular expression to match the Authorization header
    auth_pattern = r"Authorization:\s*Bearer\s+([^\s'\"]+)"
    
    # Search for the pattern in the curl command
    match = re.search(auth_pattern, curl_command)
    
    if match:
        # Extract the token
        token = match.group(1)
        return token
    else:
        return None

def main():
    print("Please paste your curl command (press Enter twice when done):")
    curl_lines = []
    while True:
        line = input()
        if line:
            curl_lines.append(line)
        else:
            break
    
    curl_command = " ".join(curl_lines)
    
    token = extract_auth_from_curl(curl_command)
    
    if token:
        print(f"Extracted token: {token[:10]}...{token[-10:]}")
        confirm = input("Do you want to update the auth token in auth.py? (y/n): ").lower()
        if confirm == 'y':
            update_auth_token(token)
            print("Auth token updated successfully in auth.py")
        else:
            print("Auth token update cancelled")
    else:
        print("No authorization token found in the curl command")

if __name__ == "__main__":
    main()

