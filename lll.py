import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

token='7630853977:AAGrnl9XdzC-8eONDIp-8NM-uqimlYboFcc'
bot=telebot.TeleBot(token)
ADMIN_CHAT_ID=1853800972
# Manejar el comando /start
@bot.message_handler(commands=['start'])

def send_welcome(message):

    # Crear botones
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='⚽️ FIFA 14', callback_data='button1')
    button14= telebot.types.InlineKeyboardButton(text='✅ PES 2017',callback_data='button14')
    button30= telebot.types.InlineKeyboardButton(text='❗️ Otros',callback_data='button30')
    markup.add(button1,button14,button30)


    # Enviar mensaje de bienvenida con botones
    bot.reply_to(message, f"👋 Hola @{message.from_user.username}! soy BotFi un bot que le ayudará a encontrar todo lo que busca para mantener actualizado su FIFA 14 \n\n✍️ Le damos la bienvenida de parte del equipo de @fifacuba.\n\n🔍 Esperamos que este bot sea de su ayuda y que encuentre todo lo que necesite.",reply_markup=markup)
 #Manejar el comando /archivo1

@bot.message_handler(commands=['archivo1'])
def send_file1(message):
    # Responder al comando

    # Lista de nombres de archivos
    files = ['https://t.me/fifacubar/44', 'https://t.me/fifacubar/45','https://t.me/fifacubar/46',]

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

@bot.message_handler(commands=['archivo2'])
def send_file2(message):
    # Responder al comando

    # Lista de nombres de archivos
    files = ['https://t.me/fifacubar/3?single','https://t.me/fifacubar/23?single','https://t.me/fifacubar/24?single','https://t.me/fifacubar/26?single','https://t.me/fifacubar/29?single','https://t.me/fifacubar/30?single','https://t.me/fifacubar/31?single','https://t.me/fifacubar/61?single',]

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

@bot.message_handler(commands=['archivo3'])
def send_file3(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/fifacubar/35?single','https://t.me/fifacubar/36?single','https://t.me/fifacubar/37?single','https://t.me/fifacubar/38?single','https://t.me/fifacubar/39?single','https://t.me/fifacubar/40?single','https://t.me/fifacubar/63?single']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo4'])
def send_file4(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/2','https://t.me/leviumwnia/4','https://t.me/leviumwnia/5','https://t.me/leviumwnia/6','https://t.me/leviumwnia/7',]

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo5'])
def send_file5(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/8?single','https://t.me/leviumwnia/9?1single']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo6'])
def send_file6(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/10?single','https://t.me/leviumwnia/11?single']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo7'])
def send_file7(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/14?single','https://t.me/leviumwnia/15?single']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo8'])
def send_file8(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/16?single']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo9'])
def send_file9(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/17','https://t.me/leviumwnia/18','https://t.me/leviumwnia/19','https://t.me/leviumwnia/20','https://t.me/leviumwnia/21','https://t.me/leviumwnia/22','https://t.me/leviumwnia/23','https://t.me/leviumwnia/24','https://t.me/leviumwnia/25','https://t.me/leviumwnia/26']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo10'])
def send_file10(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/27']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo11'])
def send_file11(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/28','https://t.me/leviumwnia/29']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo12'])
def send_file12(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/35']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo13'])
def send_file13(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/36']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo14'])
def send_file14(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/34']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo15'])
def send_file15(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/37 ','https://t.me/leviumwnia/38','https://t.me/leviumwnia/39','https://t.me/leviumwnia/40','https://t.me/leviumwnia/41','https://t.me/leviumwnia/42','https://t.me/leviumwnia/43','https://t.me/leviumwnia/44','https://t.me/leviumwnia/45','https://t.me/leviumwnia/46','https://t.me/leviumwnia/47','https://t.me/leviumwnia/48']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
bot.message_handler(commands=['archivo16'])
def send_file16(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/53','https://t.me/leviumwnia/54','https://t.me/leviumwnia/55']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)

bot.message_handler(commands=['archivo17'])
def send_file17(message):
    # Responder al comando

    # Lista de nombres de archivo
    files = ['https://t.me/leviumwnia/56','https://t.me/leviumwnia/57','https://t.me/leviumwnia/58','https://t.me/leviumwnia/59','https://t.me/leviumwnia/60','https://t.me/leviumwnia/61','https://t.me/leviumwnia/62']

    # Enviar cada archivo en la lista
    for file in files:
        bot.send_document(message.chat.id, file)
# Manejar los botones
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):


    if call.data == 'archivo1':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/44')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/45')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/46')


    if call.data == 'archivo2':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/3?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/23?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/24?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/26?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/29?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/30?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/31?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/61?single')


    if call.data == 'archivo3':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/35?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/36?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/37?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/38?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/39?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/40?single')
        bot.send_document(call.message.chat.id, 'https://t.me/fifacubar/63?single')


    if call.data == 'archivo4':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/2')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/4')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/5')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/6')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/7')

    if call.data=='archivo5':
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/8?single')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/9?single')
    if call.data=='archivo6':
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/10?single')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/11?single')
    if call.data=='archivo7':
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/14?single')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/15?single')
    if call.data=='archivo8':
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/16?single')

    if call.data == 'archivo9':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/17')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/18')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/19')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/20')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/21')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/22')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/23')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/24')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/25')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/26')

    if call.data == 'archivo10':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/27')
    if call.data == 'archivo11':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/28')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/29')
    if call.data == 'archivo12':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/35')
    if call.data == 'archivo13':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/36')
    if call.data == 'archivo14':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/34')
    if call.data == 'archivo15':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/37')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/38')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/39')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/40')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/41')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/42')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/43')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/44')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/45')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/46')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/47')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/48')
    if call.data == 'archivo16':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/53')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/54')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/55')
    if call.data == 'archivo17':
        # Enviar archivo1 previamente subido a Telegram
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/56')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/57')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/58')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/59')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/60')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/61')
        bot.send_document(call.message.chat.id, 'https://t.me/leviumwnia/62')

    elif call.data=='button1':
        # Crear botones
        markup = telebot.types.InlineKeyboardMarkup()
        button3 = telebot.types.InlineKeyboardButton(text='🆕 FIFA 14 Sin Mod', callback_data='archivo1')
        button2 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        button4= telebot.types.InlineKeyboardButton(text='📚 MODS',callback_data='button4')
        markup.add(button3,button2,button4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***⚽️ FIFA 14:***\n\n🔍 Aquí puedes encontrar todo lo relacionado con parches para FIFA 14', reply_markup=markup, parse_mode='Markdown')


    elif call.data=='back':
        # Crear botones
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='⚽️ FIFA 14', callback_data='button1')
        button14= telebot.types.InlineKeyboardButton(text='✅ PES 2017',callback_data='button14')
        button30= telebot.types.InlineKeyboardButton(text='❗️ Otros',callback_data='button30')
        markup.add(button1,button14,button30)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='👋 Hola\n\n🤗 ¿Qué hay de nuevo?\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')


    elif call.data=='button4':
        markup = telebot.types.InlineKeyboardMarkup()
        button5 = telebot.types.InlineKeyboardButton(text='🆕 FIP14 V5.0.0', callback_data='button5')
        button6 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        button6 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button5,button6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***📚 MODS:***\n\n✍️ Estos son los ***mods*** más usados:\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')


    elif call.data=='button5':
        markup = telebot.types.InlineKeyboardMarkup()
        button7 = telebot.types.InlineKeyboardButton(text='🔥 Parche', callback_data='archivo2')
        button8 = telebot.types.InlineKeyboardButton(text='👱‍♂️ FACEPACK ', callback_data='archivo3')
        button13= telebot.types.InlineKeyboardButton(text='🏟 PACK DE ESTADIOS',callback_data='archivo4' )
        button9 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button7,button8,button9,button13)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***🆕 FIP14 V5.0.0:***\n\n👷‍♂️ Este mod es desarrollado por Harry Bull Zack(HBZ) y es uno de los más completos por no decir el que más.\n\n⚙️ Para su instalacíon se requiere de un espacio de: +80 GB, los archivos comprimidos que le proporcinaré solo pesan 16gb(Parche + FACEPACK). Al descomprimirlos es que pesa tanto.\n\n🔑 La contraseña para descomprimir los archivos es ```HarryBullZakMods```\n\n🧏 Debe tener en cuenta que tiene que instalar los mods en el orden que se los envió el bot.\n\n👨🏻‍💻Si tiene algún problema con la instalación del parche consulte al administrador, en la descripción.\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')

    elif call.data=='button14':
        markup=telebot.types.InlineKeyboardMarkup()
        button15=telebot.types.InlineKeyboardButton(text='⚽️ PES 17 Sin Mods',callback_data='button15')
        button25=telebot.types.InlineKeyboardButton(text='🔥 Parche', callback_data='button25')
        button16 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button15,button16,button25)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***✅ PES 2017:***\n\n🔍 Aquí puedes encontrar todo lo relacionado con parches para PES 2017', reply_markup=markup, parse_mode='Markdown')

    elif call.data=='button15':
        markup=telebot.types.InlineKeyboardMarkup()
        button17=telebot.types.InlineKeyboardButton(text='Parte 1',callback_data='archivo5')
        button19=telebot.types.InlineKeyboardButton(text='Parte 2',callback_data='archivo6')
        button20=telebot.types.InlineKeyboardButton(text='Parte 3',callback_data='archivo7')
        button21=telebot.types.InlineKeyboardButton(text='Parte 4',callback_data='archivo8')
        button18 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button17,button18,button19,button20,button21)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***⚽️ PES 17 Sin Mods:***\n\n🔍 Aquí puedes encontrar el PES 17 sin ningun mod, para poder anexarle luego los mods y que no de ningun error.\n\n🔑 La Contraseña de los archivos es: ```esva```', reply_markup=markup, parse_mode='Markdown')

    elif call.data=='button25':
        markup=telebot.types.InlineKeyboardMarkup()
        button26=telebot.types.InlineKeyboardButton(text='🆕 PES PP 2023',callback_data='archivo9')
        button27=telebot.types.InlineKeyboardButton(text='🆕 Option File PP 2023',callback_data='archivo10')
        button28 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button26,button27,button28)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***🔥 Parche:***\n\n✍️ Professional Patch es uno de los mejores mods para PES 17 y lo recomiendo 100%.', reply_markup=markup, parse_mode='Markdown')

    elif call.data=='button30':
        markup=telebot.types.InlineKeyboardMarkup()
        button31=telebot.types.InlineKeyboardButton(text='👨🏻‍💻 FM 2023',callback_data='button31')
        button35=telebot.types.InlineKeyboardButton(text='📱 FIFA 14 a 23 Mobile',callback_data='button35')
        button41=telebot.types.InlineKeyboardButton(text='🆕 FIFA 15',callback_data='button41')
        button45=telebot.types.InlineKeyboardButton(text='🆕 PES 13',callback_data='button45')
        button48=telebot.types.InlineKeyboardButton(text='🏀 NBA 2K14',callback_data='button48')
        button33 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button31,button33,button35,button41,button45,button48)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***❗️ Otros:***\n\n⚽️ Aquí puedes encontrar otros juegos de Fútbol', reply_markup=markup, parse_mode='Markdown')
    elif call.data=='button31':
        markup=telebot.types.InlineKeyboardMarkup()
        button32=telebot.types.InlineKeyboardButton(text='⬇️ Descargar',callback_data='archivo11')
        button34 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button32,button34)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***👨🏻‍💻 FM 2023:***\n\n✍️ Descripción del juego:\n\n***- Football Manager 2023 es un videojuego de simulación de gestión de fútbol que está disponible en varias plataformas.\n\n Requisitos:\n-64 bits\n-SO: Windows 7\n-Procesador: Intel Core 2 or AMD Athlon 64 X2\n-Memoria: 4 GB de RAM\n-Gráficos: Intel GMA X4500, NVIDIA GeForce 9600M GT, AMD/ATI Mobility Radeon HD 3650\n-DirectX: Versión 11\n-Almacenamiento: 7 GB de espacio disponible***', reply_markup=markup, parse_mode='Markdown')
    elif call.data=='button35':
        markup=telebot.types.InlineKeyboardMarkup()
        button38=telebot.types.InlineKeyboardButton(text='⬇️ APK',callback_data='archivo12')
        button39=telebot.types.InlineKeyboardButton(text='⬇️ OBB',callback_data='archivo13')
        button40=telebot.types.InlineKeyboardButton(text='⬇️ DATA',callback_data='archivo14')
        button37 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button38,button39,button40,button37)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***📱 FIFA 14 a 23 Mobile:***\n\n✍️ FIFA 14 actualizado a 2023 con modo carrera de manager, creado por FABIX7\n\n🔑 Contraseña:```byfabix7```', reply_markup=markup, parse_mode='Markdown')
    elif call.data=='button41':
        markup=telebot.types.InlineKeyboardMarkup()
        button42=telebot.types.InlineKeyboardButton(text='⬇️ Descargar',callback_data='archivo15',)
        button43 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button42,button43)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***🆕 FIFA 15:***\n\n***⚽️ FIFA 15 es un videojuego de simulación de fútbol que incluye equipos y jugadores reales con mejores gráficos y animaciones.***\n\n👨🏻‍💻 Los requisitos mínimos para PC para poder jugar FIFA 15 son los siguientes:\n\n💻 Sistema operativo: Windows V/7/8/8.1 de 64 bits\n💾 Procesador: Intel Core2 Quad Q6600 @ 2.4 GHz o AMD Phenom II X4 965 @ 3.4 GHz\n🎮 Tarjeta gráfica: NVIDIA GTX 460 o AMD Radeon R7 260\n💾 Memoria RAM: 4 GB\n💾 Espacio en disco duro: 13 GB\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')
    elif call.data=='button45':
        markup=telebot.types.InlineKeyboardMarkup()
        button46=telebot.types.InlineKeyboardButton(text='⬇️ Descargar',callback_data='archivo16',)
        button47 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button46,button47)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***🔥 PES 13:***\n\n***⚽️ PES 13 es un videojuego de fútbol que incluye equipos de la liga brasileña y competiciones europeas.***\n\n👨🏻‍💻 Los requisitos mínimos para PC para poder jugar PES 13 son los siguientes:\n\n💻 Sistema operativo: Windows XP SP3, Vista SP2, 7\n💻 Procesador: Intel Pentium IV 2.4 GHz o procesador equivalente\n💻 Memoria RAM: 1 GB\n💻 Tarjeta gráfica: NVIDIA GeForce 6600 o ATI Radeon X1300 o superior\n💻 Espacio en disco duro: 8 GB de espacio libre en el disco duro\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')
    elif call.data=='button48':
        markup=telebot.types.InlineKeyboardMarkup()
        button49=telebot.types.InlineKeyboardButton(text='⬇️ Descargar',callback_data='archivo17',)
        button50 = telebot.types.InlineKeyboardButton(text='⏮ Atras', callback_data='back')
        markup.add(button49,button50)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='***🏀 NBA 2K14:***\n\n***Requisitos:\n\n -Sistema Operativo: Windows.\n-Procesador: Pentium 4 2.4 Ghz Single Core Procesador ó equivalente (2.8 Ghz for Vista/Win 7/Win 8)\n-Memoria: 512 MB RAM.\n-Tarjeta gráfica: CPU: Intel Core 2 Duo Procesador ó equivalente DirectX 9.0c compatible card con Shader Model 3.0 support.\n-DirectX: Versión 9.0c.***\n\n🇨🇺 Únete a @fifacuba', reply_markup=markup, parse_mode='Markdown')


if __name__=='__main__':
    print('iniciando')
    bot.infinity_polling()
