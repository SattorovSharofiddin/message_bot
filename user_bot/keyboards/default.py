from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from json import load
from config import conf
from utils.misc import car_names

main_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text='🧍‍♂️ Haydovchi kerak')],
    [KeyboardButton(text='🚕 Haydovchiman')],
    [KeyboardButton(text='🆘 Aloqa')],
    [KeyboardButton(text='🔰 Panel')]
])
main_menu.adjust(2)

menu = [KeyboardButton(text='🔝 Asosiy Menyu')]

back_to_main = ReplyKeyboardBuilder([menu])

panel_menu = ReplyKeyboardBuilder()
panel_menu.row(KeyboardButton(text='💳 Balans'),
               KeyboardButton(text='📈 Kanal / Guruh'), )

panel_menu.row(KeyboardButton(text="♾ Majburiy a'zo bot"))

panel_menu.row(KeyboardButton(text="👥 Referal"),
               KeyboardButton(text="⚙️ Sozlamalar"),
               )
panel_menu.row(KeyboardButton(text="🆘 Yordam"),
               KeyboardButton(text='🔝 Asosiy Menyu'))

panel_channel = ReplyKeyboardBuilder([
    [KeyboardButton(text="Kanal qo'shish")],
    [KeyboardButton(text="Guruh qo'shish ")],
    menu
])
panel_channel.adjust(2)

# majburiy
panel_mandatory = ReplyKeyboardBuilder([
    [KeyboardButton(text="Majbur guruh qo'shish")],
    menu
])

panel_referal = ReplyKeyboardBuilder([
    [KeyboardButton(text="Reklama posti")],
    [KeyboardButton(text="Reklama post video")],
    [KeyboardButton(text="Referallar ro'yxati")],
    [KeyboardButton(text="🔙 Orqaga")],
    menu
])
panel_referal.adjust(2)

"""passenger"""

passenger_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text="Yetib borish")],
    [KeyboardButton(text="Yetkazib berish")],
    menu
])
passenger_menu.adjust(2)

"""driver"""

driver_menu = ReplyKeyboardBuilder([
    [KeyboardButton(text="Yo'lovchi kutish")],
    [KeyboardButton(text="Hisobingiz")],
    [KeyboardButton(text="Ma'lumotlarni o'zgartirish")],
    [KeyboardButton(text="🔙 Orqaga")],
    menu
])
driver_menu.adjust(2)

# hisob
driver_accaunt = ReplyKeyboardBuilder([
    [KeyboardButton(text="CLICK")],
    [KeyboardButton(text="PAYME")],
    menu
])

driver_accaunt.adjust(2)

send_phone = ReplyKeyboardBuilder([
    [KeyboardButton(text='Raqamni yuborish', request_contact=True)]
])

accept_or_not = ReplyKeyboardBuilder([
    [KeyboardButton(text='✅ Tasdiqlayman')],
    [KeyboardButton(text='❌ Rad etish')],
])
accept_or_not.adjust(2)

treaty = ReplyKeyboardBuilder([
    [KeyboardButton(text='Kelishuv')]
])
treaty.row(KeyboardButton(text="🔙 Orqaga"), *menu)

skip = ReplyKeyboardBuilder([
    [KeyboardButton(text="O'tkazib yuborish")]
])
skip.row(KeyboardButton(text="🔙 Orqaga"), *menu)

button_1234 = ReplyKeyboardBuilder()
button_1234.row(
    KeyboardButton(text='1'),
    KeyboardButton(text='2'),
    KeyboardButton(text='3'),
    KeyboardButton(text='4')
)
button_1234.row(KeyboardButton(text="🔙 Orqaga"), *menu)

button_1234_driver = ReplyKeyboardBuilder([
])
button_1234_driver.row(
    KeyboardButton(text='1'),
    KeyboardButton(text='2'),
    KeyboardButton(text='3'),
    KeyboardButton(text='4')
)
button_1234_driver.row(KeyboardButton(text="🔙 Orqaga"), *menu)
button_1234_driver.adjust(2)

cancel_driver = ReplyKeyboardBuilder([
    [KeyboardButton(text='❌ Haydovchini kutishni bekor qilish')]
])

cancel_client = ReplyKeyboardBuilder([
    [KeyboardButton(text="❌ Yo'lovchini kutishni bekor qilish")]
])

cars_button = ReplyKeyboardBuilder([
    [KeyboardButton(text=car)] for car in car_names
])
cars_button.row(*menu)
cars_button.adjust(2)

where_you_go = ReplyKeyboardBuilder([
    [KeyboardButton(text="Shahar bo'ylab")],
    [KeyboardButton(text="Viloyatlarga")]
])
where_you_go.adjust(2)

"""region_district"""
list_reg = []
with open(conf.bot.ROOT_FOLDER + 'reg_dis.json') as f:
    d: dict = load(f)
    for i in d.keys():
        list_reg += [[KeyboardButton(text=i)]]
region = ReplyKeyboardBuilder(list_reg + [menu])
region.adjust(2)


def make_district(region_name):
    with open(conf.bot.ROOT_FOLDER + 'reg_dis.json') as f:
        data: dict = load(f)
        districts = data.get(region_name)
        buttons = [[KeyboardButton(text=district)] for district in districts]
    districts_buttons = ReplyKeyboardBuilder(buttons + [menu])
    districts_buttons.adjust(2)
    return districts_buttons
