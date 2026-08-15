import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)


TOKEN = os.getenv("BOT_TOKEN")

# Telegram ID, куда будут приходить заявки
ADMIN_ID = 8895567644

NAME, PHONE = range(2)


def main_keyboard():
    keyboard = [
        ["🔥 Пожарная безопасность"],
        ["📹 Видеонаблюдение"],
        ["📋 Аудит объекта"],
        ["💰 Получить расчёт"],
        ["📞 Связаться с нами"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def video_keyboard():
    keyboard = [
        ["💰 Узнать стоимость"],
        ["📞 Оставить заявку"],
        ["⬅️ Назад к услугам"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте! 👋\n\n"
        "Вы обратились в SecurLineUz.\n"
        "Мы поможем обеспечить безопасность вашего объекта.\n\n"
        "Выберите нужную услугу:",
        reply_markup=main_keyboard()
    )


# -------------------------
# ЗАЯВКА
# -------------------------

async def start_application(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "📞 Оставить заявку\n\n"
        "Как вас зовут?"
    )

    return NAME


async def get_name(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["name"] = update.message.text

    await update.message.reply_text(
        "Спасибо! 👍\n\n"
        "Теперь отправьте ваш номер телефона.\n"
        "Например: +998 90 123 45 67"
    )

    return PHONE


async def get_phone(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    name = context.user_data.get("name")
    phone = update.message.text

    user = update.effective_user

    username = (
        f"@{user.username}"
        if user.username
        else "нет username"
    )

    # Отправляем заявку владельцу
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "🔔 НОВАЯ ЗАЯВКА SecurLineUz\n\n"
            f"👤 Имя: {name}\n"
            f"📞 Телефон: {phone}\n"
            f"💬 Telegram: {username}\n"
            f"🆔 ID клиента: {user.id}"
        )
    )

    await update.message.reply_text(
        "✅ Спасибо за заявку!\n\n"
        "Мы получили ваши данные.\n"
        "Специалист SecurLineUz свяжется с вами в ближайшее время.",
        reply_markup=main_keyboard()
    )

    context.user_data.clear()

    return ConversationHandler.END


# -------------------------
# УСЛУГИ
# -------------------------

async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = update.message.text

    if text == "📹 Видеонаблюдение":
        await update.message.reply_text(
            "📹 Видеонаблюдение\n\n"
            "Установка камер видеонаблюдения для дома, "
            "офиса, магазина и предприятия.\n\n"
            "Мы поможем подобрать оборудование и установить "
            "систему под ваш объект.",
            reply_markup=video_keyboard()
        )
        return

    if text == "💰 Узнать стоимость":
        await update.message.reply_text(
            "💰 Расчёт стоимости\n\n"
            "Напишите площадь объекта и его адрес.\n\n"
            "Например:\n"
            "200 м², Ташкент, Юнусабад.\n\n"
            "Специалист подготовит предварительный расчёт."
        )
        return

    if text == "⬅️ Назад к услугам":
        await update.message.reply_text(
            "Выберите нужную услугу 👇",
            reply_markup=main_keyboard()
        )
        return

    if text == "🔥 Пожарная безопасность":
    await update.message.reply_text(
        "🔥 Пожарная безопасность\n\n"
        "Проектирование и монтаж систем пожарной сигнализации.\n\n"
        "Обслуживание и проверка оборудования.\n\n"
        "Поможем обеспечить соответствие объекта требованиям "
        "пожарной безопасности.",
        reply_markup=fire_keyboard()
    )
    return
    
    if text == "💰 Узнать стоимость":
        await update.message.reply_text(
            "💰 Расчёт стоимости\n\n"
            "Напишите площадь объекта и его адрес.\n\n"
            "Например:\n"
            "200 м², Ташкент, Юнусабад.\n\n"
            "Специалист подготовит предварительный расчёт."
        )
        return

    if text == "⬅️ Назад к услугам":
        await update.message.reply_text(
            "Выберите нужную услугу 👇",
            reply_markup=main_keyboard()
        )
        return

    if text == "📋 Аудит объекта":
        await update.message.reply_text(
            "📋 Аудит объекта\n\n"
            "Проверим объект на соответствие требованиям "
            "безопасности и подготовим рекомендации.",
            reply_markup=main_keyboard()
        )
        return

    if text == "💰 Получить расчёт":
        await update.message.reply_text(
            "💰 Получить расчёт\n\n"
            "Напишите площадь объекта и его адрес.\n"
            "Специалист подготовит предварительный расчёт.",
            reply_markup=main_keyboard()
        )
        return

    if text == "📞 Связаться с нами":
        await update.message.reply_text(
            "📞 Связаться с нами\n\n"
            "Чтобы оставить заявку, нажмите кнопку:\n"
            "📞 Оставить заявку",
            reply_markup=video_keyboard()
        )
        return

    await update.message.reply_text(
        "Пожалуйста, выберите нужную услугу 👇",
        reply_markup=main_keyboard()
    )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(TOKEN).build()

    # /start
    app.add_handler(
        CommandHandler("start", start)
    )

    # Форма заявки
    application_handler = ConversationHandler(
        entry_points=[
            MessageHandler(
                filters.Regex("^📞 Оставить заявку$"),
                start_application
            )
        ],
        states={
            NAME: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    get_name
                )
            ],
            PHONE: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    get_phone
                )
            ],
        },
        fallbacks=[],
    )

    app.add_handler(application_handler)

    # Остальные сообщения
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
