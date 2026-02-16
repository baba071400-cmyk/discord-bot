import os
import discord
from discord.ext import commands

# 환경 변수
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # 필요시 사용

# 봇 설정
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 추방 제외 역할
EXCLUDED_ROLES = ["55Lv", "55Lv."]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 명령어 예시: !kick @user
@bot.command()
async def kick(ctx, member: discord.Member):
    member_roles = [role.name for role in member.roles]
    if any(role in EXCLUDED_ROLES for role in member_roles):
        await ctx.send(f"{member}님은 제외 역할이 있어 추방되지 않습니다.")
    else:
        await member.kick(reason="자동추방")
        await ctx.send(f"{member}님이 추방되었습니다.")

# 새로 들어온 멤버 자동 추방
@bot.event
async def on_member_join(member):
    member_roles = [role.name for role in member.roles]
    if any(role in EXCLUDED_ROLES for role in member_roles):
        print(f"{member}님은 제외 역할이 있어 자동추방되지 않습니다.")
    else:
        await member.kick(reason="자동추방")
        print(f"{member}님이 자동추방되었습니다.")

bot.run(DISCORD_TOKEN)
