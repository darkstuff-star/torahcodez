import json
from typing import Dict

from .settings import settings


class Translator:
    def __init__(self) -> None:
        self.glossary: Dict[str, str] = {}
        if settings.GLOSSARY.exists():
            data = json.loads(settings.GLOSSARY.read_text(encoding="utf-8"))
            self.glossary = {entry["en"].lower(): entry["he"] for entry in data.get("entries", [])}

    def translate_en_to_he(self, text: str) -> str:
        key = text.strip().lower()
        return self.glossary.get(key, text)

    def translate_he_to_en(self, text: str) -> str:
        rev = {v: k for k, v in self.glossary.items()}
        return rev.get(text, text)

    def get_glossary(self) -> dict:
        return {"entries": [{"en": k, "he": v} for k, v in self.glossary.items()]}

    def set_glossary(self, payload: dict) -> None:
        entries = payload.get("entries", [])
        settings.GLOSSARY.write_text(
            json.dumps({"entries": entries}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        self.glossary = {e["en"].lower(): e["he"] for e in entries}
