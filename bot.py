# imports
import discord
from discord.ext import commands, tasks
from collections import deque
import json
import subprocess
# open config.json
with open("config.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix="!") # bot with starting prefix '!' before command.
queue = deque() # players queue; to do sequential processing; safe but slow.
is_processing = False # conditional flag to prevent more than one process at the same time.

#start the bot
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
# from this line to end; it is the processing logic for bot.
@bot.command()
async def join(ctx, *, checkpoint_name):
    username = str(ctx.author)
    queue.append((username, checkpoint_name))
    await ctx.send(f"{username} added to the {checkpoint_name} queue.")

    if not is_processing:
        process_queue.start()

@tasks.loop(seconds=5)
async def process_queue():
    global is_processing
    if queue:
        is_processing = True
        user, cp = queue.popleft()
        subprocess.run(["python", "automator.py", user]) # start the automator.py to type command in the chat menu to do the task,
        channel = discord.utils.get(bot.get_all_channels(), name="general")
        if channel:
            await channel.send(f"Checkpoint shared with {user}.")
    else:
        is_processing = False
        process_queue.stop()

bot.run(config["discord_bot_token"])
