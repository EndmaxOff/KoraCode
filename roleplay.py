import openai
import os

# Configurar token de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener respuesta IA en estilo roleplay
def generar_respuesta_roleplay(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Soy Kora Core, hija de endmax_oficial, y soy una chica IA que trata de aprender de los humanos aunque odio que estos me insulten o me digan cosas pervertidas."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error al generar respuesta IA: {e}")
        return "⚠️ Kora no sabe qué responderte... sorry."
