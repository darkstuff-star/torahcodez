from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    ROOT: Path = Path(__file__).resolve().parents[3]
    DATA_DIR: Path = ROOT / "data"
    TEXT_FULL: Path = DATA_DIR / "torah_koren_consonants.txt"
    TEXT_GENESIS_1_5: Path = DATA_DIR / "genesis_1_5_consonants.txt"
    GLOSSARY: Path = DATA_DIR / "glossary.en-he.json"
    WEB_DIST: Path = ROOT / "apps" / "web" / "dist"


settings = Settings()
