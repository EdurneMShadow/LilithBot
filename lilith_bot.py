from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import logging
import filtros

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

id_grupo = '-310490484'
id_miembros = [169092, 7730198, 39226004, 72263992, 172732847, 173507959, 184637992, 186522250, 188858869,
                197978154, 350932157]
constitucion = open('70-Idioms.pdf', 'rb')
#bandera = open('tests/test.png', 'rb')
#foto = open('tests/test.png', 'rb')
filter_dictadura = filtros.FilterDictadura()

def main():
    updater = Updater(token='462365078:AAEDXX4Wj1_N_Li7Yug1fvXZhvQvuMfLlog')
    dispatcher = updater.dispatcher

    dictadura_handler = MessageHandler(filter_dictadura, modo_dictadura)
    dispatcher.add_handler(dictadura_handler)


    updater.start_polling()
    updater.idle()

def modo_dictadura(bot, update):
    bando = ('Bienvenidos al modo Dictadura Definitiva, activado por el Gran Líder Karakatuchi. Os informo de que a\
    partir de este punto se os eliminarán los siguientes privilegios: \n\
    - Derecho a expulsión (todo el mundo será perseguido por el Gran Líder y su Constitución aún habiendo abandonado\
    el grupo)\n\
    - Se suprimen los artículos ? y ? que permitían el derecho de ?. \n\
    - Se castigará de forma física la deslealtad (?). \n\
    Por otra parte, a nivel de gobierno se adoptarán las siguientes medidas: \n\
    - Las elecciones quedarán suspendidas indefinidamente. \n\
    - Prohibición y eliminación de partidos que no sean el del GLK. \n\
    - Subida de los impuestos. \n\
    Para deshacer este modo, TODO integrante del grupo deberá enviar una foto con el filtro del gato de Instagram.')

    user = update.message.from_user
    logger.info('Nombre del usuario: %s , ID del usuario: %s, Mensaje: %s, ID del grupo: %s',
                user.first_name, user.id, update.message.text, update.message.chat)

    bot.send_message(chat_id= id_grupo, text=bando)

    for i in id_miembros:
        bot.send_message(chat_id = i , text = 'HOLA EDURNE')
        bot.sendDocument(chat_id = i , document = constitucion)
        bot.send_photo(chat_id = i, photo = bandera)
        bot.send_photo(chat_id = i, photo = foto)

if __name__ == '__main__':
    main()
