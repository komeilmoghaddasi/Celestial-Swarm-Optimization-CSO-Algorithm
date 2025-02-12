import yaml
import os

def load_config(config_path):
    """Load YAML configuration file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file {config_path} not found!")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def save_to_file(filename, content):
    """Save content to a text file."""
    with open(filename, "w") as f:
        f.write(content)

def log(message):
    """Prints and logs messages."""
    print(f"📌 {message}")
