# Telegram Bot: Ingress Agent Links

Send one or more IDs to the bot, separated by spaces. It will reply with a link for each ID.

## Setup (Local Polling)

1. Install Python 3.10+.
2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Create a `.env` file from the example and set your bot token:

```
TELEGRAM_BOT_TOKEN=your_token_here
```

4. Run the bot:

```powershell
python bot.py
```

## Example

Input:

```
abc xyz
```

Output:

```
abc -> https://link.ingress.com/agent/abc
xyz -> https://link.ingress.com/agent/xyz
```
