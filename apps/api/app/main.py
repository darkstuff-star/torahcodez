from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .grid_search import search_layers
from .models import SearchRequest, SearchResponse
from .normalize_he import normalize_hebrew
from .settings import settings
from .storage import load_text
from .translate import Translator

AVAILABLE_TEXTS = [
    {"id": "GENESIS_1_5", "label": "Genesis 1-5", "path": settings.TEXT_GENESIS_1_5},
    {"id": "FULL_TORAH", "label": "Full Torah", "path": settings.TEXT_FULL},
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/texts")
def list_texts():
    return [
        {"id": entry["id"], "label": entry["label"]}
        for entry in AVAILABLE_TEXTS
        if entry["path"].exists()
    ]


@app.get("/texts/{text_id}")
def get_text(text_id: str):
    try:
        t = load_text(text_id)
    except Exception as exc:  # pragma: no cover - narrow scope
        raise HTTPException(404, str(exc)) from exc
    return {"id": text_id, "length": len(t)}


@app.get("/glossary")
def get_glossary():
    return translator.get_glossary()


@app.put("/glossary")
def put_glossary(payload: dict):
    translator.set_glossary(payload)
    return translator.get_glossary()


@app.post("/search", response_model=SearchResponse)
def search(req: SearchRequest):
    text = load_text(req.codex)
    text_norm = normalize_hebrew(text)

    q_he = translator.translate_en_to_he(req.query_en)
    q_norm = normalize_hebrew(q_he)
    if req.reverse:
        q_norm = q_norm[::-1]

    hits = list(
        search_layers(
            text=text_norm,
            query=q_norm,
            base_N=req.gridWidth,
            directions=req.directions,
            skip_min=req.skipMin,
            skip_max=req.skipMax,
            layers=req.layers,
        )
    )

    return {
        "query_he": q_norm,
        "hits": hits,
        "textId": req.codex,
        "expected": None,
    }


if settings.WEB_DIST.exists():
    app.mount("/", StaticFiles(directory=str(settings.WEB_DIST), html=True), name="ui")
