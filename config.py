from pathlib import Path

manusearch_dir = Path(__file__).parent

def load_config():
    config = {}
    config["DefaultPaths"] = read_one_string_per_line(manusearch_dir / "default_paths.txt")
    config["DefaultKeywords"] = read_one_string_per_line(manusearch_dir / "default_keywords.txt")
    return config

def read_one_string_per_line(filepath):
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]