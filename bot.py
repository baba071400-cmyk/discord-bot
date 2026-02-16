import discord
import os
import asyncio
from discord.ext import commands

# 환경 변수
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

# 봇 설정
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True  # 음성 상태 감지 필수!
bot = commands.Bot(command_prefix="!", intents=intents)

# 추방 제외 역할
EXCLUDED_ROLES = ["55Lv", "55Lv."]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 수동 추방 명령어
@bot.command()
async def kick(ctx, member: discord.Member):
    member_roles = [role.name for role in member.roles]
    if any(role in EXCLUDED_ROLES for role in member_roles):
        await ctx.send(f"{member}님은 제외 역할이라 추방되지 않습니다.")
    else:
        await member.kick(reason="관리자 명령")
        await ctx.send(f"{member}님이 추방되었습니다.")

# 음성채널 나가면 자동 추방
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is not None and after.channel is None:
        member_roles = [role.name for role in member.roles]
        if any(role in EXCLUDED_ROLES for role in member_roles):
            print(f"{member}님은 제외 역할이라 자동추방되지 않습니다.")
            return

        # 10초 대기 후 다시 확인 (실수 방지)
        await asyncio.sleep(10)
        if member.voice is None:
            await member.kick(reason="음성채널 퇴장 자동추방")
            print(f"{member}님이 음성채널을 나가 자동추방되었습니다.")

bot.run(DISCORD_TOKEN)

