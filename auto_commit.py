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