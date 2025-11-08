from .settings import settings


def load_text(text_id: str) -> str:
    if text_id == "FULL_TORAH":
        return settings.TEXT_FULL.read_text(encoding="utf-8")
    if text_id == "GENESIS_1_5":
        return settings.TEXT_GENESIS_1_5.read_text(encoding="utf-8")
    raise ValueError("unknown text id")
