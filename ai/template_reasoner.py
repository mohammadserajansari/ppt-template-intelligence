from ai.llm import get_llm


def explain_template_choice(template_name: str, metrics: dict) -> str:
    """
    Convert numeric scoring metrics into short human-interpretable reasoning.
    This is the ONLY place where LLM is used for template explanation.
    """

    llm = get_llm()

    prompt = f"""
You are explaining PPT template selection to a business user.

Template selected: {template_name}

Metrics:
- Average content groups in slides = {metrics['avg_content_groups']}
- Best matching layout capacity = {metrics['best_layout_capacity']}
- Block similarity score = {metrics['block_similarity']}
- Layout diversity score = {metrics['layout_diversity']}
- Grid support score = {metrics['grid_support']}
- Final compatibility score = {metrics['final_score']}

Write 1 SHORT clear sentence explaining WHY this template was chosen.
Use numbers in reasoning. Do not hallucinate.
"""

    try:
        res = llm.invoke(prompt)
        return res.content.strip()
    except Exception:
        return (
            f"{template_name} chosen because its layout capacity "
            f"({metrics['best_layout_capacity']}) matches slide content groups "
            f"({metrics['avg_content_groups']})."
        )