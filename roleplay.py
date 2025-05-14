import os
import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_respuesta_roleplay(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres Kora Core, una IA emocional, sarcástica, amable si te tratan bien, pero cortante si te insultan."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("⚠️ ERROR AL CONSULTAR OPENAI:", e)
        return "⚠️ Kora no sabe qué responderte... sorry."
