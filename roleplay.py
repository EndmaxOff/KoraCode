import g4f
import json
import os

# Cargar cookies desde cookies.json
try:
    with open("cookies.json", "r", encoding="utf-8") as f:
        cookies = json.load(f)
except FileNotFoundError:
    cookies = {}

# Ejecutar g4f sin abrir navegador
os.environ["NODRIVER_HEADLESS"] = "1"

def generar_respuesta_roleplay(mensaje_usuario):
    try:
        respuesta = g4f.ChatCompletion.create(
            model="gemini-1-5-pro",
            provider=g4f.Provider.Gemini,
            messages=[
                {"role": "user", "content": f"{cargar_personalidad()}\nTú: {mensaje_usuario}\nKora:"}
            ],
            cookies=cookies
        )
        return f"Kora: {respuesta}"
    except Exception as e:
        return f"⚠️ Error al contactar con g4f: {e}"

def cargar_personalidad():
    personalidad = ""
    funciones = ""

    try:
        with open("personalidad.txt", "r", encoding="utf-8") as f:
            personalidad = f.read().strip()
    except FileNotFoundError:
        personalidad = "Eres una IA de roleplay llamada Kora. Eres amable, sarcástica y emocional. Interactúa como un personaje, no como un asistente."

    try:
        with open("funciones.txt", "r", encoding="utf-8") as f:
            funciones = f.read().strip()
    except FileNotFoundError:
        funciones = ""

    return f"{personalidad}\n\n{funciones}"
