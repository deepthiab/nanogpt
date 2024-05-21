import requests
import os

# URL of the file to download
url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"

# Send a GET request to the URL
response = requests.get(url)

cwd = os.getcwd()
file_name = "input.txt"
file_path = os.path.join(cwd, file_name)
# Save the content to a file

with open(file_path, "w") as file:
    file.write(response.text)

print(f"File downloaded and saved as {file_path}")



