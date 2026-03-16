# PPTX Content Extraction & Template-Based Presentation Generation

## 📌 Overview

This project implements an **end-to-end automated system** that:

1. Extracts meaningful content and layout metadata from any PPTX.
2. Analyses multiple PPT templates to understand layout capability.
3. Selects the most suitable template using interpretable scoring.
4. Rebuilds a new presentation using the selected template layouts and theme.

The goal is to transform **raw / unstructured presentations into visually consistent presentations** aligned with a chosen template design language.

---

## ✅ Assignment Coverage

| Requirement                   | Status        |
| ----------------------------- | ------------- |
| Content Extraction            | ✔ Implemented |
| Template Analysis             | ✔ Implemented |
| Template Scoring & Selection  | ✔ Implemented |
| Final PPT Reconstruction      | ✔ Implemented |
| AI-assisted reasoning         | ✔ Implemented |
| Automated end-to-end pipeline | ✔ Implemented |

---

## 🧠 System Architecture

```
Input PPT
   ↓
Content Extractor
   ↓
Layout / Semantic Analyzer
   ↓
Template Analyzer
   ↓
Template Scoring Engine
   ↓
Template Selector
   ↓
Template-Aware Slide Builder
   ↓
Final Presentation
```

---

## 🧩 Part 1 — Content Extraction

Using `python-pptx`, the system extracts:

* Slide Titles
* Body Text
* Bullet Content
* Spatial Metadata (`left`, `top`)
* Slide Index
* Table placeholders (if present)

Output is converted into structured JSON.

Example:

```json
{
  "slide_index": 0,
  "title": "Example Slide",
  "elements": [
    {
      "text": "Point A",
      "left": 12345,
      "top": 45678
    }
  ]
}
```

This spatial metadata enables detection of:

* Multi-column grid layouts
* Dense content slides
* Logical content grouping

---

## 🧩 Part 2 — Template Analysis

Each template is analysed to understand:

* Available slide layouts
* Placeholder count and type
* Layout diversity
* Content density capability

This allows estimation of which template can best support the **input presentation structure.**

---

## 🧩 Part 3 — Template Selection

A normalized scoring system (0-1) selects the best template.

### Scoring Signals

1. Structural Compatibility
2. Layout Diversity
3. Grid Support
4. Semantic Cohesion (AI-assisted)

### Final Score

```
Final Score =
0.5 × Structural Score
+ 0.3 × Visual/Layout Prior
+ 0.2 × Semantic Cohesion
```

Template with highest score is selected.

---

## 🧩 Part 4 — Final Presentation Generation

Using the selected template:

* Appropriate template layouts are chosen
* Titles mapped to TITLE placeholders
* Body content mapped to BODY placeholders
* Dense grid slides decomposed into readable template-friendly slides
* Template theme (fonts, margins, spacing) preserved

Output:

```
output/final_ppt_with_chosen_template.pptx
```

---

## 🤖 AI Usage

AI is used selectively:

* Semantic clustering of slide text
* Human-interpretable reasoning for template selection

Layout reconstruction remains deterministic for reliability.

---

## 📁 Repository Structure

```
ppt_ai_transformer/

app/
   main.py

pipeline/
   orchestrator.py

extract/
   extractor.py
   semantic_cluster.py

template/
   analyzer.py
   scorer.py
   selector.py

generator/
   builder.py

ai/
   template_reasoner.py

core/
   config.py
   logger.py

templates/
output/
logs/

Dockerfile
docker-compose.yml
requirements.txt
README.md
.env
```

---

## ⚙️ Environment Setup (Conda)

Create environment:

```
conda create -n ppt_ai python=3.11
conda activate ppt_ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔐 Setup .env

Create `.env` file:

```
GROQ_API_KEY=your_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

## ▶️ Run Locally (FastAPI)

```
uvicorn app.main:app --reload
```

API runs on:

```
http://localhost:8000
```

---

## 🐳 Run with Docker

Build:

```
docker build -t ppt-ai .
```

Run:

```
docker run --env-file .env -p 8000:8000 ppt-ai
```

---

## 🐳 Run with Docker-Compose

```
docker compose up --build
```

---

## 📤 Expected API Output Format

```json
{
  "chosen_template": "templates/template2.pptx",
  "template_scores": [
    {"template": "templates/template1.pptx","score": 0.708},
    {"template": "templates/template2.pptx","score": 0.817}
  ],
  "selection_metrics": {
    "avg_content_groups": 6,
    "best_layout_capacity": 6,
    "final_score": 0.817
  },
  "selection_reason_human":
  "Template selected because layout capacity aligns with detected content groups.",
  "ai_plan":[
     {
       "split_required":true,
       "slide_type":"grid",
       "reason":"3 rows × 6 columns detected"
     }
  ],
  "extracted_json":[ ... ],
  "final_ppt":"output/final_ppt_with_chosen_template.pptx"
}
```

---

## 🎯 Evaluation Alignment

This solution demonstrates:

* High-quality structured extraction
* Deep template capability analysis
* Interpretable scoring logic
* AI-assisted reasoning
* Automated presentation reconstruction
* Modular clean architecture

---

## 📌 Design Considerations

* Logical layout reconstruction prioritized over exact visual cloning
* Dense slides decomposed for readability
* Template layouts used instead of arbitrary textboxes

---
