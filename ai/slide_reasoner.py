# import json
# from ai.llm import get_llm

# def reason_slide(slide):

#     llm = get_llm()

#     prompt = f"""
# You are PPT expert.

# Slide has:
# title = {slide['title']}
# text_blocks = {len(slide['elements'])}

# Give SHORT reason in <20 words why slide needs splitting or not.

# Return JSON:

# {{
# "split_required": true/false,
# "slide_type": "grid/bullet/section",
# "reason": "short sentence"
# }}
# """

#     res = llm.invoke(prompt)

#     try:
#         return json.loads(res.content)
#     except:
#         return {
#             "split_required": True,
#             "slide_type": "grid",
#             "reason": "Multiple column groups detected"
#         }


def detect_column_groups(slide):

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


def detect_row_groups(slide):

    ys = sorted([e["top"] for e in slide["elements"]])

    groups = []
    threshold = 600000

    for y in ys:

        placed = False

        for g in groups:
            if abs(g - y) < threshold:
                placed = True
                break

        if not placed:
            groups.append(y)

    return len(groups)


def reason_slide(slide):

    col_groups = detect_column_groups(slide)
    row_groups = detect_row_groups(slide)

    total_blocks = len(slide["elements"])

    if col_groups >= 4 and row_groups >= 2:

        return {
            "split_required": True,
            "slide_type": "grid",
            "reason": f"{row_groups} rows × {col_groups} columns detected with {total_blocks} text blocks"
        }

    if total_blocks <= 5:

        return {
            "split_required": False,
            "slide_type": "bullet",
            "reason": f"Only {total_blocks} text blocks — suitable for single bullet slide"
        }

    return {
        "split_required": True,
        "slide_type": "bullet",
        "reason": f"{total_blocks} blocks may overcrowd slide layout"
    }