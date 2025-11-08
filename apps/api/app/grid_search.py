from __future__ import annotations

from typing import Dict, Generator, Iterable

DIR_VECTORS: Dict[str, tuple[int, int]] = {
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
    "N": (-1, 0),
    "NE": (-1, 1),
    "NW": (-1, -1),
    "SE": (1, 1),
    "SW": (1, -1),
}


def index_to_rc(i: int, N: int) -> tuple[int, int]:
    return i // N, i % N


def rc_to_index(r: int, c: int, N: int) -> int:
    return r * N + c


def step_rc(r: int, c: int, dr: int, dc: int, k: int) -> tuple[int, int]:
    return r + dr * k, c + dc * k


def in_bounds(r: int, c: int, N: int, total: int) -> bool:
    return r >= 0 and c >= 0 and c < N and r * N + c < total


def search_on_grid(
    text: str,
    query: str,
    N: int,
    directions: Iterable[str],
    skip_min: int,
    skip_max: int,
) -> Generator[Dict[str, object], None, None]:
    total = len(text)
    L = len(query)
    if L == 0:
        return
    for start in range(total):
        rs, cs = index_to_rc(start, N)
        for d in directions:
            dr, dc = DIR_VECTORS[d]
            for step in range(skip_min, skip_max + 1):
                ok = True
                for k in range(L):
                    rr, cc = step_rc(rs, cs, dr, dc, k * step)
                    if not in_bounds(rr, cc, N, total):
                        ok = False
                        break
                    idx = rc_to_index(rr, cc, N)
                    if text[idx] != query[k]:
                        ok = False
                        break
                if ok:
                    end_idx = rc_to_index(*step_rc(rs, cs, dr, dc, (L - 1) * step), N)
                    yield {
                        "dir": d,
                        "skip": step,
                        "start": start,
                        "length": L,
                        "span": (start, end_idx),
                        "grid": {"r": rs, "c": cs, "N": N},
                    }


def search_layers(
    text: str,
    query: str,
    base_N: int,
    directions: Iterable[str],
    skip_min: int,
    skip_max: int,
    layers: int,
) -> Generator[Dict[str, object], None, None]:
    for layer in range(1, layers + 1):
        N = base_N * layer
        for hit in search_on_grid(text, query, N, directions, skip_min, skip_max):
            hit["layer"] = layer
            yield hit
