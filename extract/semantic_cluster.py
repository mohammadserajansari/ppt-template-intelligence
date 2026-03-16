from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

_model = None


def get_semantic_model():

    global _model

    if _model is None:
        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model


def semantic_group(texts, k=3):

    model = get_semantic_model()

    emb = model.encode(texts)

    km = KMeans(n_clusters=min(k, len(texts)))

    labels = km.fit_predict(emb)

    groups = {}

    for t, l in zip(texts, labels):
        groups.setdefault(l, []).append(t)

    return list(groups.values())