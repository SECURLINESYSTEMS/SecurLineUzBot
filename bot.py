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

    services_keyboard = [
        ["🔥 Пожарная безопасность", "📹 Видеонаблюдение"],
        ["📋 Аудит объекта", "💰 Получить расчёт"],
        ["📞 Связаться с нами"]
    ]

    video_keyboard = [
        ["💰 Узнать стоимость"],
        ["📞 Оставить заявку"],
        ["⬅️ Назад к услугам"]
    ]

    if text == "📹 Видеонаблюдение":
        await update.message.reply_text(
            "📹 Видеонаблюдение\n\n"
            "Установка камер видеонаблюдения для дома, офиса, магазина и предприятия.\n\n"
            "Мы поможем подобрать оборудование и установить систему под ваш объект.",
            reply_markup=ReplyKeyboardMarkup(
                video_keyboard,
                resize_keyboard=True
            )
        )
        return

    if text == "💰 Узнать стоимость":
        await update.message.reply_text(
            "💰 Расчёт стоимости\n\n"
            "Напишите площадь объекта и его адрес.\n"
            "Например:\n"
            "200 м², Ташкент, Юнусабад.\n\n"
            "Специалист подготовит предварительный расчёт."
        )
        return

    if text == "📞 Оставить заявку":
        await update.message.reply_text(
            "📞 Оставить заявку\n\n"
            "Напишите ваше имя и номер телефона.\n"
            "Специалист SecurLineUz свяжется с вами."
        )
        return

    if text == "⬅️ Назад к услугам":
        await update.message.reply_text(
            "Выберите нужную услугу 👇",
            reply_markup=ReplyKeyboardMarkup(
                services_keyboard,
                resize_keyboard=True
            )
        )
        return

    answers = {
        "🔥 Пожарная безопасность":
            "🔥 Пожарная безопасность\n\n"
            "Проектирование и монтаж систем пожарной сигнализации.\n"
            "Обслуживание и проверка оборудования.",

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
