import os
from index import extract_text_from_pdf
import openai
from dotenv import load_dotenv
from constants import RESUME_ANALYZER

load_dotenv()
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": RESUME_ANALYZER}, 
                {"role": "user", "content":extract_text_from_pdf("Resume_Tanya_Mistry.pdf") },
            ]
        )
print(response.choices[0].message.content)
