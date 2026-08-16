import os

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

# Telegram ID, куда приходят заявки
ADMIN_ID = 8895567644

# Ссылка на Telegram-группу
GROUP_URL = "https://t.me/securlinesystems"

NAME, PHONE = range(2)


# =========================
# ГЛАВНОЕ МЕНЮ
# =========================

def main_keyboard():
    keyboard = [
        ["🔥 Пожарная безопасность"],
        ["📹 Видеонаблюдение"],
        ["📋 Аудит объекта"],
        ["💰 Получить расчёт"],
        ["📞 Связаться с нами"],
        ["🏆 Выполненные объекты"],
        ["👥 Наша группа"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# =========================
# МЕНЮ УСЛУГИ
# =========================

def service_keyboard():
    keyboard = [
        ["💰 Узнать стоимость"],
        ["📞 Оставить заявку"],
        ["⬅️ Назад к услугам"],
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "Здравствуйте! 👋\n\n"
        "Вы обратились в SecurLineUz.\n"
        "Мы поможем обеспечить безопасность вашего объекта.\n\n"
        "Выберите нужную услугу:",
        reply_markup=main_keyboard()
    )


# =========================
# НАЧАЛО ЗАЯВКИ
# =========================

async def start_application(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "📞 Оставить заявку\n\n"
        "Как вас зовут?\n\n"
        "Если хотите отменить заявку, нажмите:\n"
        "⬅️ Назад к услугам"
    )

    return NAME


# =========================
# ОТМЕНА ЗАЯВКИ
# =========================

async def cancel_application(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    context.user_data.clear()

    await update.message.reply_text(
        "↩️ Заявка отменена.\n\n"
        "Выберите нужную услугу 👇",
        reply_markup=main_keyboard()
    )

    return ConversationHandler.END


# =========================
# ПОЛУЧАЕМ ИМЯ
# =========================

async def get_name(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["name"] = update.message.text

    await update.message.reply_text(
        "Спасибо! 👍\n\n"
        "Теперь отправьте ваш номер телефона.\n\n"
        "Например:\n"
        "+998 90 123 45 67\n\n"
        "Чтобы отменить заявку, нажмите:\n"
        "⬅️ Назад к услугам"
    )

    return PHONE


# =========================
# ПОЛУЧАЕМ ТЕЛЕФОН
# =========================

async def get_phone(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    name = context.user_data.get(
        "name",
        "Не указано"
    )

    phone = update.message.text

    user = update.effective_user

    username = (
        f"@{user.username}"
        if user.username
        else "нет username"
    )

    service = context.user_data.get(
        "service",
        "Не указана"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "🔔 НОВАЯ ЗАЯВКА SecurLineUz\n\n"
            f"🛠 Услуга: {service}\n"
            f"👤 Имя: {name}\n"
            f"📞 Телефон: {phone}\n"
            f"💬 Telegram: {username}\n"
            f"🆔 ID клиента: {user.id}"
        )
    )

    await update.message.reply_text(
        "✅ Спасибо за заявку!\n\n"
        "Мы получили ваши данные.\n"
        "Специалист SecurLineUz свяжется с вами.",
        reply_markup=main_keyboard()
    )

    context.user_data.clear()

    return ConversationHandler.END


# =========================
# ОБРАБОТКА УСЛУГ
# =========================

async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = update.message.text

    # -------------------------
    # ПОЖАРНАЯ БЕЗОПАСНОСТЬ
    # -------------------------

    if text == "🔥 Пожарная безопасность":

        context.user_data["service"] = (
            "🔥 Пожарная безопасность"
        )

        await update.message.reply_text(
            "🔥 Пожарная безопасность\n\n"
            "Проектирование и монтаж систем "
            "пожарной сигнализации.\n\n"
            "Обслуживание и проверка оборудования.\n\n"
            "Поможем обеспечить безопасность "
            "вашего объекта.",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # ВИДЕОНАБЛЮДЕНИЕ
    # -------------------------

    if text == "📹 Видеонаблюдение":

        context.user_data["service"] = (
            "📹 Видеонаблюдение"
        )

        await update.message.reply_text(
            "📹 Видеонаблюдение\n\n"
            "Установка камер видеонаблюдения "
            "для дома, офиса, магазина и предприятия.\n\n"
            "Подберём оборудование и установим "
            "систему под ваш объект.",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # АУДИТ
    # -------------------------

    if text == "📋 Аудит объекта":

        context.user_data["service"] = (
            "📋 Аудит объекта"
        )

        await update.message.reply_text(
            "📋 Аудит объекта\n\n"
            "Проверим объект на соответствие "
            "требованиям безопасности.\n\n"
            "Подготовим рекомендации по устранению "
            "выявленных нарушений.",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # ПОЛУЧИТЬ РАСЧЁТ
    # -------------------------

    if text == "💰 Получить расчёт":

        context.user_data["service"] = (
            "💰 Получить расчёт"
        )

        await update.message.reply_text(
            "💰 Получить расчёт\n\n"
            "Чтобы подготовить предварительный расчёт, "
            "оставьте заявку.\n\n"
            "Нажмите кнопку:\n"
            "📞 Оставить заявку",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # УЗНАТЬ СТОИМОСТЬ
    # -------------------------

    if text == "💰 Узнать стоимость":

        await update.message.reply_text(
            "💰 Узнать стоимость\n\n"
            "Оставьте заявку, и специалист "
            "уточнит параметры объекта "
            "и подготовит стоимость.",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # СВЯЗАТЬСЯ С НАМИ
    # -------------------------

    if text == "📞 Связаться с нами":

        context.user_data["service"] = (
            "📞 Общий запрос"
        )

        await update.message.reply_text(
            "📞 Связаться с нами\n\n"
            "Чтобы специалист связался с вами, "
            "оставьте заявку.",
            reply_markup=service_keyboard()
        )

        return

    # -------------------------
    # ВЫПОЛНЕННЫЕ ОБЪЕКТЫ
    # -------------------------

    if text == "🏆 Выполненные объекты":

        context.user_data.clear()

        await update.message.reply_text(
            "🏆 Выполненные объекты\n\n"

            "🏢 Бизнес-центры\n"
            "📹 Установка систем видеонаблюдения.\n"
            "🔥 Монтаж пожарной сигнализации.\n\n"

            "🏪 Магазины и торговые объекты\n"
            "📹 Установка камер видеонаблюдения.\n"
            "🔥 Системы пожарной безопасности.\n\n"

            "🏭 Производственные предприятия\n"
            "🔥 Комплексная пожарная безопасность.\n"
            "📹 Видеонаблюдение и контроль территории.\n\n"

            "🛡️ SecurLineUz — безопасность "
            "вашего объекта под ключ.",
            reply_markup=main_keyboard()
        )

        return

    # -------------------------
    # НАША TELEGRAM-ГРУППА
    # -------------------------

    if text == "👥 Наша группа":

        context.user_data.clear()

        keyboard = [
            [
                InlineKeyboardButton(
                    "👥 Вступить в группу",
                    url=GROUP_URL
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "👥 Наша группа SecurLineUz\n\n"
            "Присоединяйтесь к нашей Telegram-группе! 🔥\n\n"
            "Там мы будем публиковать:\n"
            "🏢 Выполненные объекты\n"
            "📸 Фото наших работ\n"
            "🔥 Советы по пожарной безопасности\n"
            "📹 Видеонаблюдение\n"
            "🎁 Акции и специальные предложения\n\n"
            "Нажмите кнопку ниже 👇",
            reply_markup=reply_markup
        )

        return

    # -------------------------
    # НАЗАД К УСЛУГАМ
    # -------------------------

    if text == "⬅️ Назад к услугам":

        context.user_data.clear()

        await update.message.reply_text(
            "Выберите нужную услугу 👇",
            reply_markup=main_keyboard()
        )

        return

    # -------------------------
    # НЕИЗВЕСТНОЕ СООБЩЕНИЕ
    # -------------------------

    await update.message.reply_text(
        "Пожалуйста, выберите нужную услугу 👇",
        reply_markup=main_keyboard()
    )


# =========================
# MAIN
# =========================

def main():

    if not TOKEN:
        raise ValueError(
            "BOT_TOKEN не найден"
        )

    app = Application.builder().token(
        TOKEN
    ).build()

    # -------------------------
    # /start
    # -------------------------

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # -------------------------
    # ФОРМА ЗАЯВКИ
    # -------------------------

    application_handler = ConversationHandler(

        entry_points=[
            MessageHandler(
                filters.Regex(
                    "^📞 Оставить заявку$"
                ),
                start_application
            )
        ],

        states={

            NAME: [
                MessageHandler(
                    filters.Regex(
                        "^⬅️ Назад к услугам$"
                    ),
                    cancel_application
                ),
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    get_name
                )
            ],

            PHONE: [
                MessageHandler(
                    filters.Regex(
                        "^⬅️ Назад к услугам$"
                    ),
                    cancel_application
                ),
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    get_phone
                )
            ],

        },

        fallbacks=[
            MessageHandler(
                filters.Regex(
                    "^⬅️ Назад к услугам$"
                ),
                cancel_application
            )
        ],
    )

    app.add_handler(
        application_handler
    )

    # -------------------------
    # ОСТАЛЬНЫЕ СООБЩЕНИЯ
    # -------------------------

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print(
        "SecurLineUzBot запущен..."
    )

    app.run_polling()


if __name__ == "__main__":
    main()
