# import math


# def estimate_blocks(slide):

#     xs = sorted([e["left"] for e in slide["elements"]])

#     groups = []
#     threshold = 500000

#     for x in xs:

#         placed = False

#         for g in groups:
#             if abs(g - x) < threshold:
#                 placed = True
#                 break

#         if not placed:
#             groups.append(x)

#     return len(groups)


# def score_template(slides, template_meta):

#     avg_blocks = sum(
#         estimate_blocks(s) for s in slides
#     ) / len(slides)

#     layout_caps = [m["placeholders"] for m in template_meta]

#     best_cap = min(layout_caps, key=lambda x: abs(x - avg_blocks))


#     block_diff = abs(best_cap - avg_blocks)

#     block_score = math.exp(-block_diff / max(avg_blocks, 1))


#     diversity_score = 1 - math.exp(-len(template_meta) / 8)

#     grid_score = 0.8 if avg_blocks >= 4 else 0.4

#     final_score = round(
#         0.6 * block_score +
#         0.25 * diversity_score +
#         0.15 * grid_score,
#         3
#     )

#     explanation = {
#         "avg_content_groups": round(avg_blocks, 2),
#         "best_layout_capacity": best_cap,
#         "block_similarity": round(block_score, 3),
#         "layout_diversity": round(diversity_score, 3),
#         "grid_support": grid_score,
#         "final_score": final_score
#     }

#     return final_score, explanation




import math

from extract.semantic_cluster import semantic_group
# vision embedding will be added later safely


# -----------------------------------------------------
# ESTIMATE STRUCTURAL CONTENT BLOCKS (COLUMN GROUPING)
# -----------------------------------------------------
def estimate_blocks(slide):

    xs = sorted([e["left"] for e in slide["elements"]])

    groups = []
    threshold = 500000

    for x in xs:

        placed = False

        for g in groups:
            if abs(g - x) < threshold:
                placed = True
                break

        if not placed:
            groups.append(x)

    return len(groups)


# -----------------------------------------------------
# SEMANTIC COHESION SCORE
# -----------------------------------------------------
def semantic_density(slides):

    all_texts = []

    for s in slides:
        for e in s["elements"]:
            if e["text"].strip():
                all_texts.append(e["text"])

    if len(all_texts) < 4:
        return 0.6   # neutral

    try:
        groups = semantic_group(all_texts, k=3)

        density = len(groups) / len(all_texts)

        score = 1 - density

        return round(float(score), 3)

    except:
        return 0.6


# -----------------------------------------------------
# VISUAL SIMILARITY SCORE (SAFE PLACEHOLDER)
# -----------------------------------------------------
def visual_similarity_score():

    # until slide image renderer added
    return 0.65


# -----------------------------------------------------
# MAIN TEMPLATE SCORING
# -----------------------------------------------------
def score_template(slides, template_meta):

    avg_blocks = sum(
        estimate_blocks(s) for s in slides
    ) / len(slides)

    layout_caps = [m["placeholders"] for m in template_meta]

    best_cap = min(
        layout_caps,
        key=lambda x: abs(x - avg_blocks)
    )

    # ---------- STRUCTURAL BLOCK MATCH ----------
    block_diff = abs(best_cap - avg_blocks)

    block_score = math.exp(
        -block_diff / max(avg_blocks, 1)
    )

    # ---------- TEMPLATE DIVERSITY ----------
    diversity_score = 1 - math.exp(
        -len(template_meta) / 8
    )

    # ---------- GRID FRIENDLINESS ----------
    grid_score = 0.8 if avg_blocks >= 4 else 0.4

    structural_score = (
        0.6 * block_score +
        0.25 * diversity_score +
        0.15 * grid_score
    )

    # ---------- SEMANTIC ----------
    semantic_score = semantic_density(slides)

    # ---------- VISUAL ----------
    visual_score = visual_similarity_score()

    # ---------- FINAL NORMALIZED SCORE ----------
    final_score = round(
        0.5 * structural_score +
        0.3 * visual_score +
        0.2 * semantic_score,
        3
    )

    explanation = {
        "avg_content_groups": round(avg_blocks, 2),
        "best_layout_capacity": best_cap,
        "block_similarity": round(block_score, 3),
        "layout_diversity": round(diversity_score, 3),
        "grid_support": grid_score,
        "semantic_cohesion": semantic_score,
        "visual_layout_match": visual_score,
        "final_score": final_score
    }

    return final_score, explanation