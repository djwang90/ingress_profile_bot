import os
from typing import List

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


BASE_URL = "https://link.ingress.com/agent/"


def build_links(ids: List[str]) -> str:
    return "\n".join(f"{BASE_URL}{agent_id}" for agent_id in ids)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "请发送一个或多个 ID（用空格分隔），我会返回对应链接。\n"
        "示例：abc xyz"
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip()
    if not text:
        await update.message.reply_text("请至少发送一个 ID。")
        return

    ids = [part for part in text.split() if part]
    if not ids:
        await update.message.reply_text("请至少发送一个 ID。")
        return

    response = "为你生成的链接如下：\n" + build_links(ids)
    await update.message.reply_text(response)


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "Missing TELEGRAM_BOT_TOKEN. Set it in your environment before running."
        )

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    webhook_url = os.getenv("WEBHOOK_URL")
    webhook_path = os.getenv("WEBHOOK_PATH", "webhook")
    port = int(os.getenv("PORT", "8080"))

    if webhook_url:
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=webhook_path,
            webhook_url=f"{webhook_url.rstrip('/')}/{webhook_path}",
            allowed_updates=Update.ALL_TYPES,
        )
    else:
        app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
