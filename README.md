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
https://link.ingress.com/agent/abc
https://link.ingress.com/agent/xyz
```

## Deploy Free on Koyeb (Webhook)

Koyeb free tier supports web services but not background workers, so we use webhook mode.

### 1. Prepare repo

Commit or upload these files to a GitHub repo:
- `bot.py`
- `requirements.txt`
- `.env.example`

### 2. Create Koyeb app

1. Create a new app from your GitHub repo.
2. Runtime: Python.
3. Build command:

```powershell
python -m pip install -r requirements.txt
```

4. Run command:

```powershell
python bot.py
```

5. Expose port: `8080`.

### 3. Set environment variables in Koyeb

```
TELEGRAM_BOT_TOKEN=your_token_here
WEBHOOK_URL=https://your-app-name.koyeb.app
WEBHOOK_PATH=webhook_7f3a9c2d
PORT=8080
```

### 4. Set Telegram webhook

After deployment, call this once in your browser (replace values):

```
https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://your-app-name.koyeb.app/webhook_7f3a9c2d
```

### 5. Done

Send messages to your bot; it will reply with the links.

## Create Bot Token (BotFather)

1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`.
3. Follow the prompts to set a bot name and username.
4. BotFather will send you a token that looks like `123456:ABCDEF...`.
5. Put that token into `TELEGRAM_BOT_TOKEN`.
