def detect_layout_ai(slide):

    xs = [e["left"] for e in slide["elements"]]

    if len(set(xs)) > 3:
        return "grid"

    return "bullet"