# Destiny 2 Checkpoint Bot with Discord Integration

## Requirements
- Python $\geq$ 3.8
- discord.py
- pyautogui

## Setup
1. **Configure `config.json`**:
   - **Discord Bot Token**: Replace `"YOUR_DISCORD_BOT_TOKEN"` with a valid token from a Discord bot created via the [Discord Developer Portal](https://discord.com/developers/applications). You’ll need to:
     - Create a bot, generate a token, and invite it to your Discord server with appropriate permissions (e.g., read/send messages, access channels).
   - **Admin IDs**: Replace `"YOUR_DISCORD_ID"` with the Discord user ID(s) of the bot admin.
   - **Verify Coordinates**: Ensure the `destiny2_coords` (`start_button`: [1000, 800], `leave_button`: [100, 100]) match your *Destiny 2* game UI for your screen resolution (default is 1920x1080). If your resolution differs or the game UI updates, you’ll need to update these coordinates by:
     - Using a tool like `pyautogui.position()` to find the exact pixel coordinates for the "start" and "leave" buttons in *Destiny 2*.
       
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the bot:
```bash
python bot.py
```

## Usage
Use `!join <checkpoint>` in your Discord server. The bot will queue you and simulate in-game actions to deliver the checkpoint.

## Notes
- Ensure Destiny 2 is running and ready on a secondary machine **THIS IS A MUST**.
- Regularly update coordinates if game UI changes.
