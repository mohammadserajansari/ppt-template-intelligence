import os

def render_template_slides(template):

    os.system(
        f"libreoffice --headless --convert-to png {template}"
    )