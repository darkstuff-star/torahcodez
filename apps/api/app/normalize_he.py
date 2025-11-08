import regex as re

NIQQUD = re.compile(r"[\p{Mn}]+", flags=re.UNICODE)
NON_HEB = re.compile(r"[^\p{Hebrew}]", flags=re.UNICODE)


def normalize_hebrew(text: str) -> str:
    t = NIQQUD.sub("", text)
    t = NON_HEB.sub("", t)
    return t
