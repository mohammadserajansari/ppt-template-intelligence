from fastapi import FastAPI, UploadFile
import shutil, os

from pipeline.orchestrator import run_pipeline

app = FastAPI()

TEMPLATES = [
    "templates/template1.pptx",
    "templates/template2.pptx"
]


@app.post("/transform")
async def transform(file: UploadFile):

    os.makedirs("tmp", exist_ok=True)

    path = f"tmp/{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)


    slides, ai, best, report, metrics, human_reason, prs = await run_pipeline(
        path,
        TEMPLATES
    )

    out = "output/final_ppt_with_chosen_template.pptx"

    prs.save(out)

    return {
    "chosen_template": best,
    "template_scores": report,
    "selection_metrics": metrics,
    "selection_reason_human": human_reason,
    "ai_plan": ai,
    "extracted_json": slides,
    "final_ppt": out
}