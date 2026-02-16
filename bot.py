import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("봇 실행 완료")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None and after.channel is None:

        protected_roles = ["55Lv", "55Lv."]

        member_role_names = [role.name for role in member.roles]

        if not any(role in member_role_names for role in protected_roles):
            await member.kick(reason="외부인 자동 추방")

bot.run(TOKEN)
