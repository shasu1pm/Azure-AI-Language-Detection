from dotenv import load_dotenv
import os
import http.client
import json
import re

def main():
    global ai_endpoint
    global ai_key

    try:
        load_dotenv()
        ai_endpoint = os.getenv("AI_SERVICE_ENDPOINT")
        ai_key = os.getenv("AI_SERVICE_KEY")

        if not ai_endpoint or not ai_key:
            print("Error: AI_SERVICE_ENDPOINT or AI_SERVICE_KEY not set in .env")
            return

        # Get User input
        userText = ""
        while userText.lower() != 'quit':
            userText = input('Enter some text ("quit" to stop):\n')
            if userText.strip() and userText.lower() != "quit":
                GetLanguages(userText)

    except Exception as ex:
        print(ex)

def GetLanguages(text):
    try:
        # Split text into fragments for per-fragment detection
        fragments = re.split(r'[.!?\n,]', text)
        fragments = [frag.strip() for frag in fragments if frag.strip()]

        # Create documents payload
        documents = [{"id": str(idx + 1), "text": frag} for idx, frag in enumerate(fragments)]

        jsonBody = {
            "documents": documents
        }

        uri = ai_endpoint.rstrip("/").replace("https://", "")
        conn = http.client.HTTPSConnection(uri)

        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': ai_key
        }

        conn.request(
            "POST",
            "/text/analytics/v3.1/languages",
            json.dumps(jsonBody).encode('utf-8'),
            headers
        )

        response = conn.getresponse()
        data = response.read().decode("utf-8")

        if response.status == 200:
            result = json.loads(data)

            detected_languages = set()
            for document in result["documents"]:
                detected_language = document.get("detectedLanguage", {})
                if detected_language:
                    lang_name = detected_language.get("name", "Unknown")
                    detected_languages.add(lang_name)

            if detected_languages:
                print("\nLanguages Detected:", ", ".join(detected_languages))
            else:
                print("No language detected.")
        else:
            print(f"Error: {data}")

        conn.close()
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
