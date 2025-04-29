import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CANAL_ID = int(os.getenv("CANAL_ID"))
ROL_ID = int(os.getenv("ROL_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de horas objetivo (en UTC)
# Formato: ("HH:MM", "mensaje a enviar")
horarios = {
    "00:00": f"⏰ ¡<@&{ROL_ID}>, quedan 30 minutos para Coop Termitas 🎯",
    "00:30": f"🎉 ¡<@&{ROL_ID}>, ya es hora de Coop Termitas 🚀"
}

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    revisar_eventos.start()

@tasks.loop(minutes=1)
async def revisar_eventos():
    ahora = datetime.utcnow().strftime("%H:%M")  # Hora en UTC
    if ahora in horarios:
        canal = bot.get_channel(CANAL_ID)
        if canal:
            await canal.send(horarios[ahora])
            print(f"Mensaje enviado a las {ahora} UTC")

bot.run(TOKEN)
