import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🔥 Пожарная безопасность"],
        ["📹 Видеонаблюдение"],
        ["📋 Аудит объекта"],
        ["💰 Получить расчёт"],
        ["📞 Связаться с нами"]
    ]

    from telegram import ReplyKeyboardMarkup

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Здравствуйте! 👋\n\n"
        "Вы обратились в SecurLineUz.\n"
        "Мы поможем обеспечить безопасность вашего объекта.\n\n"
        "Выберите нужную услугу:",
        reply_markup=reply_markup
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    answers = {
        "🔥 Пожарная безопасность":
            "🔥 Пожарная безопасность\n\n"
            "Проектирование и монтаж систем пожарной сигнализации.\n"
            "Обслуживание и проверка оборудования.",

        "📹 Видеонаблюдение":
            "📹 Видеонаблюдение\n\n"
            "Установка камер видеонаблюдения для дома, офиса, магазина и предприятия.",

        "📋 Аудит объекта":
            "📋 Аудит объекта\n\n"
            "Проверим объект на соответствие требованиям безопасности и подготовим рекомендации.",

        "💰 Получить расчёт":
            "💰 Получить расчёт\n\n"
            "Напишите нам площадь объекта и его адрес.\n"
            "Специалист подготовит предварительный расчёт.",

        "📞 Связаться с нами":
            "📞 Связаться с нами\n\n"
            "Оставьте свой номер телефона или напишите сообщение — специалист свяжется с вами."
    }

    answer = answers.get(
        text,
        "Пожалуйста, выберите нужную услугу в меню 👇"
    )

    await update.message.reply_text(answer)


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("SecurLineUzBot запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
