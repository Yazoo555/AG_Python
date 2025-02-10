import os
import re

# Global variable to store the authorization token
AUTH_TOKEN = "your-initial-auth-token-here"

def get_auth_token():
    return AUTH_TOKEN

def update_auth_token(new_token):
    global AUTH_TOKEN
    AUTH_TOKEN = new_token  # Update the global variable

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'auth.py')

    # Read the current content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the AUTH_TOKEN value in the file
    updated_content = re.sub(
        r'AUTH_TOKEN\s*=\s*"[^"]+"',
        f'AUTH_TOKEN = "{new_token}"',
        content
    )

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"AUTH_TOKEN updated successfully in {file_path}")

# Call function with your given token
new_auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNDUxNTViMDI2ODU5ZjhmZDAxZTdkOTFmYTc2YmNjMTM1YmNiZTRhZDc1YTdjZjkxMTg2ZWQ2MDVkN2E5NTEwY2FlNGZmNjMzNjRjZGQzYzEiLCJpYXQiOjE3MzkxODE5OTcuMzM2NTYzLCJuYmYiOjE3MzkxODE5OTcuMzM2NTY2LCJleHAiOjE3Mzk3ODY3OTcuMzIyMzg0LCJzdWIiOiI4MSIsInNjb3BlcyI6WyJhZG1pbiJdfQ.DW6j_zNW4dPiVC-MccEq3KKKO6okrEA8KXSj-ioEcGUzg_RoAxwiRb5bbryKVC3dgxejgOzwzm8qgsyKhw3cUapQl6E9eBDgjo1yJ1iIZGYIGl5KW0XiSZ4qyG_aRRsLg-NLNzIxQkZ3MOizEpH3FGzBG5WN2LDb8DNlB8uPLTJtJwB14FJo-eMnfpjqGZRFMFJPW9tr5dh3fmuDlWHvXilWyelOCjuegpHhdvUqt0MP4tqH7EUcNSEwHcw5HN6Lgqajd2WduoHt1kmXlEy0imW3-iJe0goP694yXrmXBaVgjT7MFskOEOWHwUqYz6amNIEjdiyJDjP3Bepqo2te4tQzR7-ci5qkSlELTPVq6JOuXPW552Z01R96sruf49x3aBgeBPdKgDBkKxkYkHnZN90rLtARWg5B7gEEaJwUUypJGY3UNH6SbIvo2NqQ-_lU5eSP5oNQQ2ssTHjz60GYFe_xrtShdz4yjaEVYguLWOo3YLSIAdWo4BQhkEA49QmJXDuzvVLc8KZw7lWVH5Y9A_I6Gi1v8KMLJVJZH_At2Dm6fxTiyNFC_22RL5Ayo3j9xWA7fdmq-El_MD3Hb7SKqKaJBbbdsRELhzf5WOe2ro1sRTobwOjiAlkStLsrlNoGTxsp1IJNE-riX2AzdO72MeNCTCjVpxeJJEXxrtJyFDg"

update_auth_token(new_auth_token)
