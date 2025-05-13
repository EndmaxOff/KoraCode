import openai
import os

# Configurar la API key desde variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para generar una respuesta de IA estilo roleplay
def generar_respuesta_roleplay(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres Kora Core, una IA emocional, sarcástica, amable si te tratan bien, pero cortante si te insultan."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content  # ✅ Corrección clave
    except Exception as e:
        print(f"Error IA: {e}")
        return "⚠️ Kora no sabe qué responderte... sorry."
