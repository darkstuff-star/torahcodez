def search_1d(text: str, query: str, skip_min: int, skip_max: int):
    n = len(text)
    m = len(query)
    hits = []
    if m == 0:
        return hits
    for step in range(skip_min, skip_max + 1):
        last_start = n - (m - 1) * step
        if last_start <= 0:
            break
        for start in range(last_start):
            ok = True
            for k in range(m):
                if text[start + k * step] != query[k]:
                    ok = False
                    break
            if ok:
                hits.append(
                    {
                        "dir": "E",
                        "skip": step,
                        "start": start,
                        "length": m,
                        "span": (start, start + (m - 1) * step),
                        "grid": {"r": 0, "c": 0, "N": n},
                        "layer": 1,
                    }
                )
    return hits
