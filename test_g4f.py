import g4f

# Cargar personalidad
with open("personalidad.txt", "r", encoding="utf-8") as f:
    personalidad = f.read()

# Mensaje del usuario
mensaje_usuario = input("Tú: ")

try:
    respuesta = g4f.ChatCompletion.create(
        model="gemini-1-5-pro",
        provider="Gemini",  # Como string, funciona aunque no esté definido como objeto
        messages=[
            {"role": "system", "content": personalidad},
            {"role": "user", "content": mensaje_usuario}
        ]
    )
    print("Kora:", respuesta)
except Exception as e:
    print("⚠️ Error al contactar con g4f:", e)
