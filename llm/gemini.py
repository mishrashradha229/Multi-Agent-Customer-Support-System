import google.generativeai as genai

genai.configure(
    api_key="your api key"
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"