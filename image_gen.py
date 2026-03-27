import requests
import os

STABILITY_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

def generate_image(prompt):
    api_key = os.getenv("STABILITY_API_KEY")
    
    # Check for placeholder API Key
    if not api_key or "your_" in api_key:
        print("Warning: STABILITY_API_KEY is not configured properly.")
        return "https://placehold.co/512x512/png?text=API+Key+Missing"
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }
    
    try:
        response = requests.post(STABILITY_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            image_base64 = data["artifacts"][0]["base64"]
            return f"data:image/png;base64,{image_base64}"
        else:
            print(f"Stability Error [{response.status_code}]: {response.text}")
            return f"https://placehold.co/512x512/png?text=Error+{response.status_code}"
    except Exception as e:
        print(f"Error calling Stability API: {e}")
        return "https://placehold.co/512x512/png?text=Connection+Error"
