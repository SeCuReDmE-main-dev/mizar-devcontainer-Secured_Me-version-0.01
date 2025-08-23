import os

def filter_files():
    allowed_extensions = ['.py', '.js', '.html', '.css', '.md', '.txt', '.bat', '.ps1', '.sh', '.gitignore', '.gitigonre']
    ignored_dirs = ['.git', '__pycache__', '.devcontainer']
    ignored_files = ['badge.png', 'ascii_art.txt', 'all_files.txt', 'filter_files.py']
    filtered_files = []
    with open('all_files.txt', 'r') as f:
        for filepath in f:
            filepath = filepath.strip()
            if not filepath:
                continue

            # Normalize path
            filepath = os.path.normpath(filepath)

            # Check if in ignored directory
            in_ignored_dir = False
            for ignored_dir in ignored_dirs:
                if ignored_dir in filepath.split(os.sep):
                    in_ignored_dir = True
                    break
            if in_ignored_dir:
                continue

            # Check if it is an ignored file
            if os.path.basename(filepath) in ignored_files:
                continue

            # Check for allowed extension
            _, ext = os.path.splitext(filepath)
            if ext in allowed_extensions:
                filtered_files.append(filepath)

    with open('filtered_files.txt', 'w') as f:
        for filepath in filtered_files:
            f.write(filepath + '\n')

if __name__ == '__main__':
    filter_files()
