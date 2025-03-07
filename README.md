# AutoStruct

## Tagline

**Organize. Scaffold. Develop.**

## Motto

**From Blueprint to Code in One Command.**

## Overview

AutoStruct is a powerful command-line tool that transforms a simple text file into a complete directory structure for your project. Designed for developers who value efficiency and organization, AutoStruct automates the tedious task of manual project scaffolding, so you can focus on what truly matters—coding!

## Core Features

### Quick Setup

- Generate complex directory trees with a single command.

### Flexible Formatting

- Define both directories and files using an intuitive, plain text format.

### Cross-Platform

- Works seamlessly on any operating system with Python 3.6+.

### No External Dependencies

- Built entirely with Python's standard libraries, ensuring hassle-free installation.

## Benefits

- **Time Saving:** Automate repetitive folder and file creation to start coding faster.
- **Consistency:** Maintain a standardized project structure across all your projects.
- **Simplified Workflow:** Easily set up new projects with a predefined scaffold.
- **Error Reduction:** Minimize manual mistakes in creating directories and files.
- **Enhanced Productivity:** Focus on development instead of spending time on setup.

## Getting Started

### Installation

Install AutoStruct from PyPI:

```bash
pip install autostruct-tool==0.1.5
```
Using AutoStruct:

```bash
autostruct structure.txt
```



**Note:** The package is named `autostruct-tool` on PyPI, but the command-line tool is accessed via the `autostruct` command.

## How It Works

1. **Plan:** Create a structure file (e.g., `structure.txt`) that defines your project’s layout.
2. **Generate:** Run the command in your terminal to generate the directories and files.
3. **Develop:** Open your newly created project structure and start coding!

### Example Structure File

```plaintext
my_project/
  ├── my_project/
  │   ├── __init__.py
  │   ├── main.py
  │   ├── utils.py
  ├── tests/
  ├── docs/
  ├── README.md
  ├── requirements.txt
  ├── LICENSE
```

### Generated Project Structure

```plaintext
my_project/
  ├── my_project/
  │   ├── __init__.py
  │   ├── main.py
  │   ├── utils.py
  ├── tests/
  ├── docs/
  ├── README.md
  ├── requirements.txt
  ├── LICENSE
```

## Development

Interested in contributing or modifying AutoStruct? Follow these steps to set up your development environment:

### Clone the Repository:

```bash
git clone https://github.com/amandeepsingh29/autostruct.git
cd autostruct
```

### Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install in Editable Mode:

```bash
pip install -e .
```

### Run Tests:

(When tests are added in the future, run them with your preferred test runner, e.g., `pytest`.)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions, suggestions, or issues, please open an issue on GitHub or contact the project maintainer, **Amandeep Singh**.

**Happy Coding!**

