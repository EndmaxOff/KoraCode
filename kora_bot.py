from roleplay import generar_respuesta_roleplay
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
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de horas objetivo (en UTC)
# Formato: ("HH:MM", "mensaje a enviar")

horarios = {
    "22:30": [
        {
            "canal_id": 1333188803317334157,
            "mensaje": "⏰ ¡<@&1341251656108478516>, quedan 30 minutos para Coop Crab 🎯!"
        }
        ],
    "23:00": [
        {
            "canal_id": 1333188803317334157,
            "mensaje": "🚀 ¡<@&1341251656108478516>, es hora de Coop Crab!"
        }
        ],
    "23:05": [
        {
            "canal_id": 1333188803317334157,
            "mensaje": "🔥 ¡<@&1341251656108478516>, Segundo llamado, el Coop Crab empezara pronto! 💥"
        }
        ],
    "00:00": [
        {
            "canal_id": 1333189062239977593,
            "mensaje": "⏰ ¡<@&1348837394257940490>, quedan 30 minutos para Coop Termitas 🎯!"
        }
        ],
    "00:30": [
        {
            "canal_id": 1333189062239977593,
            "mensaje": "🚀 ¡<@&1348837394257940490>, es hora de la Coop Termitas!"
        }
        ],
    "00:35": [
        {
            "canal_id": 1333189062239977593,
            "mensaje": "🔥 ¡<@&1348837394257940490>, Segundo llamado, el Coop Termitas empezara pronto! 💥"
        }
    ],
    "01:30": [
        {
            "canal_id": 1356678560177192961,
            "mensaje": "⏰ ¡<@&1367673502890590249>, Practicaremos rana, nos vemos en 30 minutos 🎯!"
        }
        ],
    "02:00": [
        {
            "canal_id": 1356678560177192961,
            "mensaje": "🚀 ¡<@&1367673502890590249>, es hora de practicar Coop Rana!"
        }
        ]
}

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    revisar_eventos.start()

@bot.event
async def on_member_join(member):
    canal_bienvenida = bot.get_channel(1284939738867961910)  # Usa el canal que definiste en .env
    if canal_bienvenida:
        await canal_bienvenida.send(
            f"👋 ¡Bienvenid@ {member.mention} a Insanos2! Soy Kora Core, la IA asistente de ester servidor. Si necesitas algo, no me hables... nah, broma, dime `!rol <mensaje>` y charlamos 😏"
        )

@bot.command(name="rol")
async def rol(ctx, *, mensaje_usuario):
    respuesta = generar_respuesta_roleplay(mensaje_usuario)
    await ctx.send(respuesta)

@tasks.loop(minutes=1)
async def revisar_eventos():
    ahora = datetime.utcnow().strftime("%H:%M")  # Hora en UTC
    if ahora in horarios:
        for evento in horarios[ahora]:
            canal = bot.get_channel(evento["canal_id"])
            if canal:
                await canal.send(evento["mensaje"])
                print(f"Mensaje enviado a canal {evento['canal_id']} a las {ahora} UTC")
            else:
                print(f"❌ Canal con ID {evento['canal_id']} no encontrado.")

bot.run(TOKEN)
