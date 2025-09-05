# Mizar DevContainer Environment

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![SPONSORED BY E2B FOR STARTUPS](https://img.shields.io/badge/SPONSORED%20BY-E2B%20FOR%20STARTUPS-ff8800?style=for-the-badge)](https://e2b.dev/startups)

A zero-configuration development environment for the **Mizar Proof Assistant**, designed for GitHub Codespaces and local development. This repository provides both a web interface and command-line tools for formal mathematical verification using the Mizar language.

## 🚀 Features

- **🌐 Web Interface**: User-friendly Flask-based web application for writing and verifying Mizar proofs
- **💻 Command Line Tools**: Direct CLI access to Mizar verification with cross-platform scripts
- **📦 Zero Configuration**: Pre-configured Dev Container with Mizar 8.1.15 and MML 5.94.1493
- **🔧 GitHub Codespaces Ready**: One-click development environment setup
- **🧪 Comprehensive Testing**: Full test suite for both web and CLI interfaces
- **📚 Extensive Documentation**: Detailed guides and examples for formal verification

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Development](#-development)
- [File Structure](#-file-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## ⚡ Quick Start

### Using GitHub Codespaces (Recommended)

1. Click the **Code** button on this repository
2. Select **Open with Codespaces**
3. Wait for the environment to build (3-5 minutes)
4. Start the web server:
   ```bash
   python src/main.py
   ```
5. Open the forwarded port (8080) to access the web interface

### Using Local Dev Container

1. Clone this repository
2. Open in VS Code with the Dev Containers extension
3. Select "Reopen in Container" when prompted
4. The Mizar environment will be automatically configured

## 🛠 Installation

### Prerequisites

- **For Dev Container**: Docker and VS Code with Dev Containers extension
- **For Manual Setup**: Ubuntu/Debian-based system with Python 3.8+

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/your-org/mizar-devcontainer.git
cd mizar-devcontainer

# Install Mizar (Ubuntu/Debian)
sudo bash .devcontainer/install-mizar.sh

# Install Python dependencies
pip install -r requirements.txt
```

## 📖 Usage

### Web Interface

Start the Flask web server:

```bash
# Using Python directly
python src/main.py

# Using platform-specific scripts
./start_server.ps1    # Windows PowerShell
./start_server.bat    # Windows Command Prompt
```

Navigate to `http://localhost:8080` to access the web interface.

**Example Mizar Proof:**
```mizar
environ

vocabularies SUBSET_1, TARSKI;
notations SUBSET_1, TARSKI;
constructors TARSKI;

begin

theorem Th1: 1 = 1
proof
  thus 1 = 1;
end;
```

### Command Line Interface

Verify Mizar files directly from the command line:

```bash
# Using Python directly
python verify.py path/to/your/proof.miz

# Using platform-specific scripts
./verify.ps1 proof.miz    # Windows PowerShell
./verify.bat proof.miz    # Windows Command Prompt
```

**Example:**
```bash
python verify.py tests/test.miz
```

## 🔌 API Reference

### Web Server Endpoints

#### `GET /`
Returns the main web interface for entering and verifying Mizar proofs.

**Response:** HTML page with text editor and verification controls

#### `POST /verify`
Verifies a Mizar proof submitted as JSON.

**Request Body:**
```json
{
  "code": "environ\n\nbegin\n\ntheorem T1: 1 = 1;\nproof\n  thus 1 = 1;\nend;"
}
```

**Response:**
```json
{
  "result": "Verification output from Mizar system"
}
```

**Status Codes:**
- `200`: Verification completed (check result for errors)
- `400`: Invalid JSON or missing code field
- `500`: Server error during verification

## 🔧 Development

### Running Tests

The project includes comprehensive tests for all components:

```bash
# Run all tests
python -m pytest tests/

# Run specific test files
python -m pytest tests/test_server.py
python -m pytest tests/test_verify.py
python -m pytest tests/test_integration.py
```

### Development Dependencies

Install additional development tools:

```bash
pip install -r requirements-dev.txt
```

### Code Structure

The application follows a modular architecture:

- **`src/server.py`**: Flask web application with verification endpoints
- **`src/main.py`**: Server startup script
- **`verify.py`**: Command-line verification tool
- **`tests/`**: Comprehensive test suite
- **`.devcontainer/`**: Container configuration and Mizar installation

## 📁 File Structure

```text
mizar-devcontainer/
├── .devcontainer/
│   ├── devcontainer.json          # Dev Container configuration
│   └── install-mizar.sh           # Mizar installation script
├── src/
│   ├── main.py                    # Server startup script
│   ├── server.py                  # Flask web application
│   └── templates/
│       └── index.html             # Web interface template
├── tests/
│   ├── test.miz                   # Sample Mizar proof
│   ├── test_integration.py        # Integration tests
│   ├── test_server.py             # Web server tests
│   └── test_verify.py             # CLI verification tests
├── .gitignore                     # Git ignore patterns
├── LICENSE                        # Apache 2.0 license
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── requirements-dev.txt           # Development dependencies
├── verify.py                      # CLI verification tool
├── start_server.bat              # Windows batch script
├── start_server.ps1              # PowerShell script
├── verify.bat                    # Windows verification script
├── verify.ps1                   # PowerShell verification script
└── documentation/
    ├── AGENTS.md                 # Agent architecture documentation
    ├── CONTRIBUTING.md           # Contribution guidelines
    ├── MIZAR.md                  # Mizar language guide
    └── SECURITY.md               # Security policies
```

## 🔍 Troubleshooting

### Common Issues

**Error: `mizf` command not found**
- Ensure you're running inside the Dev Container or have installed Mizar manually
- Check that `MIZFILES` environment variable is set: `echo $MIZFILES`

**Port 8080 already in use**
- Change the port in `src/main.py`: `app.run(host='0.0.0.0', port=8081, debug=True)`

**Verification timeout**
- Large proofs may exceed the 30-second timeout
- Modify timeout in `src/server.py` or use CLI for complex proofs

**Permission errors on Windows**
- Run PowerShell as Administrator
- Ensure execution policy allows scripts: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

### Environment Variables

The following environment variables are automatically configured:

- `MIZFILES`: Path to Mizar library files (`/usr/local/share/mizar`)
- `PATH`: Updated to include Mizar executables (`/usr/local/bin`)

### Debugging

Enable debug mode for detailed error messages:

```bash
export FLASK_DEBUG=1
python src/main.py
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run the test suite: `python -m pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📚 Additional Resources

- **[MIZAR.md](MIZAR.md)**: Complete guide to the Mizar language and formal verification
- **[AGENTS.md](AGENTS.md)**: Technical documentation of system components
- **[Mizar Project Homepage](http://mizar.org/)**: Official Mizar documentation
- **[Mizar Mathematical Library](http://mml.mizar.org/)**: Browse verified mathematical theorems

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mizar Project**: For providing the formal verification system
- **E2B**: For startup sponsorship support
- **Contributors**: All developers who have contributed to this project

---

**Built with ❤️ for formal verification and mathematical rigor**