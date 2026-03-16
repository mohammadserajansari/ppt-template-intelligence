def select_template(slides, templates, analyzer, scorer):

    best_template = None
    best_score = -1
    best_metrics = None

    report = []

    for t in templates:

        meta = analyzer(t)

        score, metrics = scorer(slides, meta)

        report.append({
            "template": t,
            "score": score
        })

        if score > best_score:
            best_score = score
            best_template = t
            best_metrics = metrics

    return best_template, report, best_metrics