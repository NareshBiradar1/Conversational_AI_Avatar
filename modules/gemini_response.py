import google.generativeai as genai
from IPython.display import display


class GeminiResponse:

    chat=None
    
    def __init__(self):
        print("Chat initiated")
        GOOGLE_API_KEY='AIzaSyAQd9TBxwP11uE98o5ebOwu0dv-dt_lCVI'
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        GeminiResponse.chat = model.start_chat(history=[])
        response = GeminiResponse.chat.send_message(
            "Pretend you\'re a chat assistant")
        print(response.text)
    
    def get_gemini_response(self,message):
        try:
            response = GeminiResponse.chat.send_message(message)
            print(response.text)
            responseText = response.text.replace('*', '')
            return responseText
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while fetching the response."
