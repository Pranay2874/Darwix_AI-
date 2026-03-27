# The Pitch Visualizer: From Words to Storyboard 🖼️

A powerful utility that instantly transforms a narrative text into a fully visual storyboard using cutting-edge Generative AI. 

## Features
- **Smart Text Segmentation**: Splits long paragraphs into logical scenes using NLTK sentence tokenization.
- **LLM-Powered Prompt Engineering**: Leverages an LLM text generation model (OpenAI GPT-3.5-turbo) to enhance simple sentences into vivid, descriptive text-to-image prompts.
- **Dynamic Visual Consistency**: Automatically locks the user's chosen artistic style (e.g. Cyberpunk, Digital Art, Watercolor) across all prompts to ensure a unified storyboard.
- **Seamless Storyboarding**: Communicates with the Stability AI API (Stable Diffusion 1.6) to fetch base64 encoded images, elegantly displayed in a customized, responsive Tailwind UI.

## Technology Stack
- **Backend**: Python 3.9+, FastAPI, Uvicorn
- **NLP**: NLTK (`punkt`)
- **LLM Refiner**: `openai` Python SDK 
- **Image Generation**: Stability AI text-to-image API (`requests`)
- **Frontend**: Vanilla Javascript & Tailwind CSS via CDN (Jinja2 Template)

---

## 🛠️ Setup Instructions (Local Execution)

### 1. Prerequisites
- Python 3.9+
- An [OpenAI API Key](https://platform.openai.com/api-keys) OR valid endpoint.
- A [Stability AI API Key](https://platform.stability.ai/).

### 2. Configure Environment Variables
Inside the project root, modify the provided `.env` file or create a new one:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
STABILITY_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Create a Virtual Environment and Install Dependencies
Open your terminal and run:
```bash
python -m venv venv

# Windows Prompt:
venv\Scripts\activate
# MacOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn main:app --reload
```
Navigate to `http://localhost:8000` in your web browser.

---

## 🎨 Why This Approach? (Design Choices)
1. **User-Selectable Style:** Added a `<select>` dropdown to allow the narrator to determine the tone and flavor of their visual output, satisfying a core bonus objective.
2. **Visual Consistency:** Simply generating images from segmented text results in confusing styles across storyboards. By instructing the LLM to weave the *selected style* directly into every prompt definition, we dramatically increase generation coherence.
3. **No-Build Frontend:** The entire frontend is served as a single `index.html` file using Tailwind via CDN and Jinja2. This dramatically simplifies deployment (e.g., to Render/Netlify) without managing Webpack/Vite pipelines.
4. **Rich Aesthetics:** Even without a build system, the UI features smooth micro-animations, glassmorphism elements, CSS-driven loading spinners, and modern flex/grid composition to stun the user.

Enjoy visualizing your ideas!
