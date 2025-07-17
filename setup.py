from setuptools import setup
import os
import subprocess

# Dependencies for Stock Market Streamlit project
dependencies = [
    "numpy",
    "pandas",
    "plotly",
    "nbformat",
    "requests",
    "ipykernel",
    "streamlit",
]


def create_project_structure():
    """Create project files and directories."""
    # .streamlit/secrets.toml
    os.makedirs(".streamlit", exist_ok=True)
    secrets_path = os.path.join(".streamlit", "secrets.toml")
    if not os.path.exists(secrets_path):
        with open(secrets_path, "w") as f:
            f.write("# Add your Streamlit secrets here (e.g. API keys)\n")

    # notebook.ipynb in project root
    notebook_path = "notebook.ipynb"
    if not os.path.exists(notebook_path):
        with open(notebook_path, "w") as f:
            f.write("")

    # app.py and utils.py
    for filename, comment in [
        ("app.py", "# Streamlit app entry point\n"),
        ("utils.py", "# Utility functions and classes\n"),
    ]:
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(comment)

    print("✅ Project structure created successfully!")


def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("⬆️ Upgrading pip...")
    subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)


def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    subprocess.run(["pip", "install"] + dependencies, check=True)


def create_requirements_file():
    """Create a requirements.txt file with dependencies."""
    with open("requirements.txt", "w") as f:
        for dep in dependencies:
            f.write(dep + "\n")
    print("✅ requirements.txt created successfully!")


def update_gitignore():
    """Add .streamlit/ to .gitignore if not already present."""
    gitignore_path = ".gitignore"
    line_to_add = ".streamlit/\n"

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            lines = f.readlines()

        if line_to_add not in lines:
            with open(gitignore_path, "a") as f:
                f.write(line_to_add)
            print("✅ Added `.streamlit/` to .gitignore")
        else:
            print("ℹ️ `.streamlit/` already in .gitignore")
    else:
        with open(gitignore_path, "w") as f:
            f.write(line_to_add)
        print("✅ Created .gitignore and added `.streamlit/`")


# Execute setup steps
create_project_structure()
upgrade_pip()
install_dependencies()
create_requirements_file()
update_gitignore()

# Setup metadata
setup(
    name="StockMarketStreamlitApp",
    version="0.1",
    description="A Streamlit app for visualizing stock market data using RapidAPI",
    install_requires=dependencies,
)
