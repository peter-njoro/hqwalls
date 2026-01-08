import tomllib
from constants import CONFIG_DIR

def load_config():
    config_path = CONFIG_DIR / "config.toml"
    if not config_path.exists():
        raise FileNotFoundError(f"Missing config file: {config_path}")

    with open(config_path, "rb") as f:
        return tomllib.load(f)
