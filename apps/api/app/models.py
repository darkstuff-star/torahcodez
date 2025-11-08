from typing import Dict, List, Literal, Optional, Tuple

from pydantic import BaseModel, Field

Direction = Literal["N", "S", "E", "W", "NE", "NW", "SE", "SW"]


class SearchRequest(BaseModel):
    query_en: str
    directions: List[Direction] = Field(default_factory=lambda: ["E", "W", "N", "S", "NE", "NW", "SE", "SW"])
    gridWidth: int = 50
    skipMin: int = 1
    skipMax: int = 500
    layers: int = 1
    codex: Literal["GENESIS_1_5", "FULL_TORAH"] = "GENESIS_1_5"
    reverse: bool = False


class GridHit(BaseModel):
    dir: Direction
    skip: int
    start: int
    length: int
    span: Tuple[int, int]
    grid: Dict[str, int]
    layer: int = 1


class SearchResponse(BaseModel):
    query_he: str
    hits: List[GridHit]
    textId: str
    expected: Optional[float] = None
