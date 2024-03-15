from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config
import dispatcher as dp

router = Router()

ADMIN_ID = config.ADMIN_ID

# prices
PRICE = LabeledPrice(label="Подписка на 1 месяц",
                     amount=79 * 100)  # в копейках (руб)


@router.message(Command("pay"))
async def cmd_pay(message: Message):
    if config.PAY_TOKEN.split(':')[1] == 'TEST':
        await message.reply(
            "Тестовый платеж!!!\n  Для оплаты используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000.")

        await dp.bot.send_invoice(message.chat.id,
                                  title="Подписка на бота",
                                  description="Активация подписки на бота на 1 месяц",
                                  provider_token=config.PAY_TOKEN,
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
    await dp.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message):
    print("SUCCESSFUL PAYMENT:")
    print(message.successful_payment)

    await dp.bot.send_message(message.chat.id,
                              f"Платеж на сумму {message.successful_payment.total_amount / 100} {message.successful_payment.currency} прошел успешно!!!")


@router.message(Command("order"))
async def cmd_order(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Оформить заказ",
        callback_data="order")
    )
    await message.answer(
        f"После нажатия на кнопку 'Оформить заказ' будет создана заявка. Все заявки обрабатываются вручную админом. После того как заявка будет обработана, я пришлю вам информацию для оплаты.",
    )


@router.callback_query(F.data == "order")
async def callback_query_order(callback: CallbackQuery):
    await dp.bot.send_message(
        ADMIN_ID,
        
    )
    await callback.message.answer(
        f"Заказ на сумму {config.ORDER_PRICE / 100} {config.ORDER_CURRENCY}"

    )
