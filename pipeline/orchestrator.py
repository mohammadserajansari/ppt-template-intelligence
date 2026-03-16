import asyncio
from core.logger import logger
from ai.template_reasoner import explain_template_choice
from extract.extractor import extract_ppt
from ai.slide_reasoner import reason_slide
from template.analyzer import analyze_template
from template.scorer import score_template
from template.selector import select_template
from generator.builder import build


async def run_pipeline(input_ppt, templates):

    logger.info("Pipeline started")


    slides = await asyncio.to_thread(extract_ppt, input_ppt)


    ai_plan = await asyncio.gather(*[
        asyncio.to_thread(reason_slide, s)
        for s in slides
    ])


    best, report, metrics = await asyncio.to_thread(
    select_template,
    slides,
    templates,
    analyze_template,
    score_template
)
    prs = await asyncio.to_thread(
        build,
        best,
        slides,
        ai_plan
    )
    human_reason = await asyncio.to_thread(
    explain_template_choice,
    best,
    metrics
)

    logger.info("Pipeline finished")
    logger.info(f"Template Scores: {report}")
    logger.info(f"Chosen Template: {best}")
    logger.info(f"AI Plan: {ai_plan}")

    return slides, ai_plan, best, report, metrics, human_reason, prs