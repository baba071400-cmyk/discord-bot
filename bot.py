import os
import discord
from discord.ext import commands

# 환경 변수 불러오기
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # GitHub 기능 필요시 사용

# 봇 설정
intents = discord.Intents.default()
intents.members = True  # 멤버 관리 기능 필요시
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 예시 명령: !kick @user
@bot.command()
async def kick(ctx, member: discord.Member):
    await member.kick(reason="자동추방")
    await ctx.send(f"{member}님이 추방되었습니다.")

bot.run(DISCORD_TOKEN)
