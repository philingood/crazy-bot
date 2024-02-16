from aiogram import Router, F
from aiogram.types.message import ContentType
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, LabeledPrice, PreCheckoutQuery, successful_payment

# from bot import bot, PAY_TOKEN
import bot


router = Router()

# prices
PRICE = LabeledPrice(label="Подписка на 1 месяц", amount=79 * 100)  # в копейках (руб)


@router.message(Command("pay"))
async def cmd_pay(message: Message):
    if bot.PAY_TOKEN.split(':')[1] == 'TEST':
        await message.reply(
            "Тестовый платеж!!!\n  Для оплаты используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000.")

    await bot.bot.send_invoice(message.chat.id,
                               title="Подписка на бота",
                               description="Активация подписки на бота на 1 месяц",
                               provider_token=bot.PAY_TOKEN,
                               currency="rub",
                               photo_url="https://hidemy.io/media/img/news/vpn-servisy-otkazali-roskomnadzoru.jpg",
                               photo_width=391,
                               photo_height=261,
                               photo_size=88064,
                               is_flexible=False,
                               prices=[PRICE],
                               start_parameter="one-month-subscription",
                               payload="test-invoice-payload")


# pre checkout  (must be answered in 10 seconds)
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    await bot.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@router.message(F.successful_payment)
async def successful_payment(message: Message):
    print("SUCCESSFUL PAYMENT:")
    print(message.successful_payment)
    # payment_info = message.successful_payment.order_info
    # for k, v in payment_info.items():
    #     print(f"{k} = {v}")

    await bot.bot.send_message(message.chat.id, f"Платеж на сумму {message.successful_payment.total_amount / 100} {message.successful_payment.currency} прошел успешно!!!")
