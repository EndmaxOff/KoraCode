import requests
import os

# Carga la cookie "p-b" desde variable de entorno o reemplaza aquí directamente
POE_TOKEN = os.getenv("POE_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {POE_TOKEN}",
    "Content-Type": "application/json",
}

BOT = "gpt-3-5-turbo"  # Puedes cambiar a "capybara", "chinchilla", "claude-instant", etc.

# Cargar personalidad desde el archivo
def cargar_personalidad():
    try:
        with open("personalidad.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "Eres una IA amigable que responde de forma breve."

def generar_respuesta_roleplay(prompt):
    personalidad = cargar_personalidad()
    mensaje = f"{personalidad}\n\nUsuario: {prompt}\nKora:"

    try:
        # ⚠️ Este endpoint es ilustrativo: debes tener un backend o proxy tipo poe-proxy o similar.
        response = requests.post(
            f"https://poe.com/api/gql_POST_placeholder",
            headers=HEADERS,
            json={"query": mensaje, "bot": BOT}
        )

        if response.status_code == 200:
            return response.text  # ← ajustar si se obtiene JSON
        elif response.status_code == 403:
            return "⚠️ Acceso denegado. Verifica si la cookie 'p-b' ha expirado."
        else:
            return f"⚠️ Error Poe {response.status_code}: {response.text}"

    except Exception as e:
        return f"⚠️ Error al contactar Poe: {e}"
