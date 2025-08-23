
import os

def get_comment_syntax(ext):
    if ext in ['.py', '.sh', '.ps1', '.gitignore', '.gitigonre']:
        return '#', ''
    elif ext in ['.js', '.css']:
        return '/*', '*/'
    elif ext in ['.html']:
        return '<!--', '-->'
    elif ext in ['.bat']:
        return 'REM
    else:
        return '', '' # For .md, .txt

def prepend_art():
    with open('ascii_art.txt', 'r') as f:
        ascii_art = f.read()

    with open('filtered_files.txt', 'r') as f:
        filepaths = [line.strip() for line in f if line.strip()]

    for filepath in filepaths:
        _, ext = os.path.splitext(filepath)
        start_comment, end_comment = get_comment_syntax(ext)

        commented_art = []

            commented_art.append(start_comment)
            commented_art.extend(ascii_art.splitlines())
            commented_art.append(end_comment)
        # For line-by-line comments
        elif start_comment:
            for line in ascii_art.splitlines():
                commented_art.append(f"{start_comment} {line}")

        # For no comment
        else:
            commented_art.extend(ascii_art.splitlines())

        commented_art_str = '\n'.join(commented_art) + '\n\n'

        try:
            with open(filepath, 'r+', encoding='utf-8') as f:
                original_content = f.read()
                f.seek(0, 0)
                f.write(commented_art_str + original_content)
        except UnicodeDecodeError:
            # Fallback for files that are not utf-8
            try:
                with open(filepath, 'r+', encoding='latin-1') as f:
                    original_content = f.read()
                    f.seek(0, 0)
                    f.write(commented_art_str + original_content)
            except Exception as e:
                print(f"Could not process file {filepath}: {e}")
        except Exception as e:
            print(f"Could not process file {filepath}: {e}")


if __name__ == '__main__':
    prepend_art()
