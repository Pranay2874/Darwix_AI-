import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from segmentation import split_into_segments
from prompt_refiner import enhance_prompt
from image_gen import generate_image

load_dotenv()

app = FastAPI(title="Pitch Visualizer")

# Mount static files if needed (check if dir exists)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/generate")
async def generate_storyboard(
    text: str = Form(...),
    style: str = Form("digital art")
):
    # 1. Segment the text
    segments = split_into_segments(text)
    if len(segments) < 3:
        return {"error": "Please provide at least 3 sentences/segments."}

    # 2. For each segment, get enhanced prompt and generate image
    results = []
    for seg in segments:
        # Enhance prompt with chosen style
        enhanced = enhance_prompt(seg, style)
        # Generate image (returns data URL or fallback)
        image_url = generate_image(enhanced)
        results.append({
            "original": seg,
            "enhanced_prompt": enhanced,
            "image_url": image_url
        })

    return {"segments": results}
