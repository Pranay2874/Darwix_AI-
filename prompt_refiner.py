import openai
import os

def enhance_prompt(segment, style):
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Check if the key looks like the placeholder
    if not api_key or "your_" in api_key:
        print("Warning: OPENAI_API_KEY is not configured properly.")
        return f"{segment}, in the style of {style}, vibrant and detailed"

    try:
        # Use openai API>1.0.0
        client = openai.OpenAI(api_key=api_key)
        
        system_message = (
            f"You are an expert at creating image generation prompts. "
            f"Enhance the given text into a detailed, visually rich prompt. "
            f"Always include the style: '{style}'. "
            f"Keep it concise but descriptive (max 200 characters)."
        )
        user_message = f"Original text: {segment}\n\nEnhanced prompt:"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        enhanced = response.choices[0].message.content.strip()
        # Ensure style is present (append if not)
        if style.lower() not in enhanced.lower():
            enhanced += f", {style}"
        return enhanced
        
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        # Fallback: simple template
        return f"{segment}, in the style of {style}, vibrant and detailed"
