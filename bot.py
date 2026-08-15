import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")


# Главное меню
def main_keyboard():
    keyboard = [
        ["🔥 Пожарная безопасность"],
        ["📹 Видеонаблюдение"],
        ["📋 Аудит объекта"],
        ["💰 Получить расчёт"],
        ["📞 Связаться с нами"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# Меню видеонаблюдения
def video_keyboard():
    keyboard = [
        ["💰 Узнать стоимость"],
        ["📞 Оставить заявку"],
        ["⬅️ Назад к услугам"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте! 👋\n\n"
        "Вы обратились в SecurLineUz.\n"
        "Мы поможем обеспечить безопасность вашего объекта.\n\n"
        "Выберите нужную услугу:",
        reply_markup=main_keyboard()
    )


# Обработка сообщений
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Видеонаблюдение
    if text == "📹 Видеонаблюдение":
        await update.message.reply_text(
            "📹 Видеонаблюдение\n\n"
            "Установка камер видеонаблюдения для дома, офиса, "
            "магазина и предприятия.\n\n"
            "Мы поможем подобрать оборудование и установить "
            "систему под ваш объект.",
            reply_markup=video_keyboard()
        )
        return

    # Узнать стоимость
    if text == "💰 Узнать стоимость":
        await update.message.reply_text(
            "💰 Расчёт стоимости\n\n"
            "Напишите площадь объекта и его адрес.\n\n"
            "Например:\n"
            "200 м², Ташкент, Юнусабад.\n\n"
            "Специалист подготовит предварительный расчёт."
        )
        return

    # Оставить заявку
    if text == "📞 Оставить заявку":
        await update.message.reply_text(
            "📞 Оставить заявку\n\n"
            "Напишите ваше имя и номер телефона.\n\n"
            "Специалист SecurLineUz свяжется с вами."
        )
        return

    # Назад
    if text == "⬅️ Назад к услугам":
        await update.message.reply_text(
            "Выберите нужную услугу 👇",
            reply_markup=main_keyboard()
        )
        return

    # Пожарная безопасность
    if text == "🔥 Пожарная безопасность":
        await update.message.reply_text(
            "🔥 Пожарная безопасность\n\n"
            "Проектирование и монтаж систем пожарной сигнализации.\n"
            "Обслуживание и проверка оборудования.",
            reply_markup=main_keyboard()
        )
        return

    # Аудит объекта
    if text == "📋 Аудит объекта":
        await update.message.reply_text(
            "📋 Аудит объекта\n\n"
            "Проверим объект на соответствие требованиям "
            "безопасности и подготовим рекомендации.",
            reply_markup=main_keyboard()
        )
        return

    # Получить расчёт
    if text == "💰 Получить расчёт":
        await update.message.reply_text(
            "💰 Получить расчёт\n\n"
            "Напишите нам площадь объекта и его адрес.\n"
            "Специалист подготовит предварительный расчёт.",
            reply_markup=main_keyboard()
        )
        return

    # Связаться с нами
    if text == "📞 Связаться с нами":
        await update.message.reply_text(
            "📞 Связаться с нами\n\n"
            "Оставьте свой номер телефона или напишите сообщение — "
            "специалист свяжется с вами.",
            reply_markup=main_keyboard()
        )
        return

    # Если сообщение не распознано
    await update.message.reply_text(
        "Пожалуйста, выберите нужную услугу в меню 👇",
        reply_markup=main_keyboard()
    )


# Запуск бота
def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("SecurLineUzBot запущен...")

    app.run_polling()


if __name__ == "__main__":
    main()
