import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to your Git repository
repo_path = os.getenv("REPO_PATH")

# Commit message with current time
commit_message = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Git commands
commands = [
    ['git', 'add', '.'],
    ['git', 'commit', '-m', commit_message],
    ['git', 'push', 'origin', 'main']
]

#--------------------------------

# Path to your repo and README file
txt_path = os.path.join(repo_path, "commit-here.txt")

# The text you want to add
text_to_add = f"\nAuto-updated on purpose by script on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

# Append text to the commit-here.txt file
with open(txt_path, "w", encoding="utf-8") as file:
    file.write(text_to_add)

print("commit-here.txt updated.")

#----------------------------------

# Change directory to the repo
os.chdir(repo_path)

# Run commands
for cmd in commands:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {cmd}:")
        print(e.stderr)