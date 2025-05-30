# Destiny 2 Checkpoint Bot with Discord Integration

## Requirements
- Python 3.x
- discord.py
- pyautogui

## Setup
1. Fill in `config.json` with your settings.
2. Install dependencies:
```bash
pip install discord.py pyautogui
```
3. Run the bot:
```bash
python bot.py
```

## Usage
Use `!join <checkpoint>` in your Discord server. The bot will queue you and simulate in-game actions to deliver the checkpoint.

## Notes
- Ensure Destiny 2 is running and ready on a secondary machine.
- Regularly update coordinates if game UI changes.
