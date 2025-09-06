# 1. Import necessary libraries
from flask import Flask, request, jsonify, render_template
import subprocess
import tempfile
import os
import re # We use this to find the errors in the text

app = Flask(__name__)

# 2. The main page route stays the same
@app.route('/')
def index():
    return render_template('index.html')

# 3. This is our new, professional API endpoint
@app.route('/verify', methods=['POST'])
def verify_mizar():
    # --- CHANGE 1: We get data from a JSON request body ---
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({"status": "error", "message": "Invalid request. JSON with 'code' key required."}), 400
    mizar_code = data['code']
    # --- END CHANGE 1 ---

    # We use a temporary file to safely handle the user's code
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.miz') as temp_file:
        temp_file.write(mizar_code)
        temp_filename = temp_file.name

    try:
        # Try different Mizar commands based on what's available
        mizar_commands = ['mizf', '/mizar/verifymain', '/usr/local/bin/mizf']
        process = None
        
        for cmd in mizar_commands:
            try:
                process = subprocess.run(
                    [cmd, temp_filename],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                break
            except FileNotFoundError:
                continue
        
        if process is None:
            return jsonify({"status": "error", "message": "Mizar verifier not found. Please ensure Mizar is installed."}), 500
            
        output = process.stdout + process.stderr

        # --- CHANGE 2: We parse the output and create a structured JSON response ---
        errors = []
        # Mizar errors often look like: "Error at line X, character Y: [message]"
        # This regular expression helps us find and capture those details.
        error_pattern = re.compile(r"Error at line (\d+), character (\d+):(.*)")

        for line in output.splitlines():
            match = error_pattern.search(line)
            if match:
                errors.append({
                    "line": int(match.group(1)),
                    "character": int(match.group(2)),
                    "message": match.group(3).strip()
                })

        # Determine the final status based on what we found
        if not errors and "Correct" in output:
            status = "success"
        else:
            status = "failure"

        # This is the professional JSON response structure
        response_data = {
            "status": status,
            "errors": errors,
            "raw_output": output # Including raw output is good for debugging
        }
        return jsonify(response_data)
        # --- END CHANGE 2 ---

    except subprocess.TimeoutExpired:
        return jsonify({"status": "error", "message": "Verification timed out."}), 500
    finally:
        # Always clean up the temporary file
        os.remove(temp_filename)

# This part allows us to run the server directly with "python app.py"
if __name__ == '__main__':
    # We will use port 5000 as it is standard for Flask development
    app.run(host='0.0.0.0', port=5000)