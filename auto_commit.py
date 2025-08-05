import subprocess
import os
from datetime import datetime


# Path to your Git repository
repo_path = r"C:\Users\randy\PycharmProjects\Daily-Commits"

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
readme_path = os.path.join(repo_path, "README.md")

# The text you want to add
text_to_add = f"\nAuto-updated on purpose by script on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

# Append text to the README.md file
with open(readme_path, "a", encoding="utf-8") as file:
    file.write(text_to_add)

print("README.md updated.")

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