# Global variable to store the authorization token
AUTH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOTEzYzk4NjQzMTJiNzY3N2M0Yzc4MTc2MjgzYmE1MTZhYzhlM2NhYjM0ZGM1Yjk0OTU3OTFlNDBlM2Q4NmI0OWNiZjc0ZjFhNTM3ZjcwNTMiLCJpYXQiOjE3Mzg1NTk0MzIuNzc1ODYsIm5iZiI6MTczODU1OTQzMi43NzU4NjMsImV4cCI6MTczOTE2NDIzMi43NjczNjMsInN1YiI6IjgxIiwic2NvcGVzIjpbImFkbWluIl19.dRccXymP-8JoBxRM-fvPjCaZRgbwxedb75V8ryQfcXYspWV-L0P2UyQVzx7HgFKbPmpLBJCM5JDAHifk6ZF1qhHWXKwBXWmwM6lv4a53hgp897dNesSW-Y83IrwJ-ArMmOyBE1CeIyi1SVddicO8GN__3oz_lVEkQjOQ0uZ6g0XDEEb9g-Cu_YYPQJkBcf6H7g47aN5GGY-fqaDQbaHLVOb6GaLJ9obPS8zZsHoss1IooooS3mGo4HH5od3w3Pj18QtY-qoVrRRucHrQ-kvNRzmxRNPJPI-uaV2dxkdgg2BWaoUr1GS0RyP1FnmX0WJ-05rtrhvR5AGdZT0eWi7DL7lyuxPI7AH0J9QAhzrJl9XaP_J3PlfZiXMs6CIml68W1MYun12woRfPYNdkbY2RyUIZgBjxdlMlvbRo2JrmeGI7hv9QmtVd33ekawFnk7wK65tjd2pdLb2eyiNZAJRDoDW2IMlItzrfU-eJKvPdwaoxyipOmsj-Ha4J0EspiaQxZOVW-_lo5tcGV3kivGj0Fn41ChrN3rZ54xX9ZTVq3I9ED0cyoHTuwujxVX3QKeJc-LFsrPI_PDMPl9hpUnnN1kUQ-g2ibZjaPqVUKCwjIJZi_G480dxHzbL7UnTK4zSK_v68G1Rf4f9CnimS2ZGBLKAyd8cKWn-JtrKinIs0dvo"

def get_auth_token():
    return AUTH_TOKEN

def update_auth_token(new_token):
    global AUTH_TOKEN
    AUTH_TOKEN = new_token
    
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'auth.py')
    
    # Read the current content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Replace the AUTH_TOKEN value
    updated_content = re.sub(
        r'AUTH_TOKEN\s*=\s*"[^"]*"',
        f'AUTH_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOTEzYzk4NjQzMTJiNzY3N2M0Yzc4MTc2MjgzYmE1MTZhYzhlM2NhYjM0ZGM1Yjk0OTU3OTFlNDBlM2Q4NmI0OWNiZjc0ZjFhNTM3ZjcwNTMiLCJpYXQiOjE3Mzg1NTk0MzIuNzc1ODYsIm5iZiI6MTczODU1OTQzMi43NzU4NjMsImV4cCI6MTczOTE2NDIzMi43NjczNjMsInN1YiI6IjgxIiwic2NvcGVzIjpbImFkbWluIl19.dRccXymP-8JoBxRM-fvPjCaZRgbwxedb75V8ryQfcXYspWV-L0P2UyQVzx7HgFKbPmpLBJCM5JDAHifk6ZF1qhHWXKwBXWmwM6lv4a53hgp897dNesSW-Y83IrwJ-ArMmOyBE1CeIyi1SVddicO8GN__3oz_lVEkQjOQ0uZ6g0XDEEb9g-Cu_YYPQJkBcf6H7g47aN5GGY-fqaDQbaHLVOb6GaLJ9obPS8zZsHoss1IooooS3mGo4HH5od3w3Pj18QtY-qoVrRRucHrQ-kvNRzmxRNPJPI-uaV2dxkdgg2BWaoUr1GS0RyP1FnmX0WJ-05rtrhvR5AGdZT0eWi7DL7lyuxPI7AH0J9QAhzrJl9XaP_J3PlfZiXMs6CIml68W1MYun12woRfPYNdkbY2RyUIZgBjxdlMlvbRo2JrmeGI7hv9QmtVd33ekawFnk7wK65tjd2pdLb2eyiNZAJRDoDW2IMlItzrfU-eJKvPdwaoxyipOmsj-Ha4J0EspiaQxZOVW-_lo5tcGV3kivGj0Fn41ChrN3rZ54xX9ZTVq3I9ED0cyoHTuwujxVX3QKeJc-LFsrPI_PDMPl9hpUnnN1kUQ-g2ibZjaPqVUKCwjIJZi_G480dxHzbL7UnTK4zSK_v68G1Rf4f9CnimS2ZGBLKAyd8cKWn-JtrKinIs0dvo"',
        content
    )
    
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)
    
    print(f"AUTH_TOKEN updated in {file_path}")

import os
import re

