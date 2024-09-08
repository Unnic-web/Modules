__version__ = (1, 0, 2)
#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ© Copyright 2024
#ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤhttps://t.me/unnic
# 🔒ㅤㅤㅤㅤㅤLicensed under the GNU AGPLv3
# 🌐ㅤㅤhttps://www.gnu.org/licenses/agpl-3.0.html
#┏┓━┏┓━━┏┓━━┏┓━━┏━━━━┓━━━━━┏┓━━━━━━━━━━━━
#┃┃━┃┃━━┃┃━━┃┃━━┃┏┓┏┓┃━━━━┏┛┗┓━━━━━━━━━━━
#┃┗━┛┃┏┓┃┃┏┓┃┃┏┓┗┛┃┃┗┛┏┓┏┓┗┓┏┛┏━━┓┏━┓━━━━
#┃┏━┓┃┣┫┃┗┛┛┃┗┛┛━━┃┃━━┃┃┃┃━┃┃━┃┏┓┃┃┏┛━━━━
#┃┃━┃┃┃┃┃┏┓┓┃┏┓┓━┏┛┗┓━┃┗┛┃━┃┗┓┃┗┛┃┃┃━━━━━
#┗┛━┗┛┗┛┗┛┗┛┗┛┗┛━┗━━┛━┗━━┛━┗━┛┗━━┛┗┛━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# meta banner: https://t.me/HikkTutor
# meta developer: @unnic
#██╗░░░██╗███╗░░██╗███╗░░██╗██╗░█████╗░
#██║░░░██║████╗░██║████╗░██║██║██╔══██╗
#██║░░░██║██╔██╗██║██╔██╗██║██║██║░░╚═╝
#██║░░░██║██║╚████║██║╚████║██║██║░░██╗
#╚██████╔╝██║░╚███║██║░╚███║██║╚█████╔╝
#░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░╚════╝

from .. import loader, utils
from telethon.tl.types import Message  # type: ignore
import requests

# ---------------------Module-----------------------#
class CurrencyMod(loader.Module):
    """Модуль для сравнения курсов"""

    strings = {
        "name": "Currency",
        "inc_args": "ℹ️ <b>Неправильные аргументы</b>",
        "keyerror": "ℹ️ <b>Возможно, валюта отсутствует в базе данных сайта или вы ввели неправильное название.</b>",
        "currency_not_supported": "ℹ️ <b>Данная валюта не поддерживается. Пожалуйста, проверьте правильность названия.</b>"
    }

    # ---------------Tagged functionality---------------- #
    async def cvcmd(self, message: Message):
        """Используйте .cv «число» «название валюты»."""
        args = utils.get_args_raw(message)
        tray = "RUB"
        if not args:
            args = "1 " + tray

        args_list = args.split()
        try:
            if len(args_list) == 1 and isinstance(float(args_list[0]), float):
                args_list.append(str(tray))
        except Exception:
            args_list = ["1", args_list[0]]

        currency = args_list[1].upper()
        api_url = f"https://min-api.cryptocompare.com/data/price?fsym={currency}&tsyms=USD,RUB,UAH,KZT,EUR,BYN,GBP,CHF,JPY,TON,NOT"
        api_response = requests.get(api_url).json()

        user = await message.get_sender()
        is_premium = user.premium

        if 'Response' in api_response and api_response['Response'] == 'Error':
            await utils.answer(message, self.strings("currency_not_supported"))
            return

        try:
            count = float(args_list[0])

            form = (
                f"<b>Поиск по курсу: {count} {currency}</b>\n<b>Свежие результаты:</b>\n\n"
                f"{'🇺🇸 ' if not is_premium else '<emoji document_id=5202021044105257611>🇺🇸</emoji>'} "
                f"<code>{round(api_response.get('USD', 0) * count, 2)}$</code> Доллар\n"
                f"{'🇷🇺 ' if not is_premium else '<emoji document_id=5449408995691341691>🇷🇺</emoji>'} "
                f"<code>{round(api_response.get('RUB', 0) * count, 2)}₽</code> Рубль\n"
                f"{'🇺🇦 ' if not is_premium else '<emoji document_id=5447309366568953338>🇺🇦</emoji>'} "
                f"<code>{round(api_response.get('UAH', 0) * count, 2)}₴</code> Гривна\n"
                f"{'🇰🇿 ' if not is_premium else '<emoji document_id=5228718354658769982>🇰🇿</emoji>'} "
                f"<code>{round(api_response.get('KZT', 0) * count, 2)}₸</code> Тенге\n"
                f"{'🇪🇺 ' if not is_premium else '<emoji document_id=5228784522924930237>🇪🇺</emoji>'} "
                f"<code>{round(api_response.get('EUR', 0) * count, 2)}€</code> Евро\n"
                f"{'🇧🇾 ' if not is_premium else '<emoji document_id=5382219601054544127>🇧🇾</emoji>'} "
                f"<code>{round(api_response.get('BYN', 0) * count, 2)}Br</code> Бун\n"
                f"{'🇬🇧 ' if not is_premium else '<emoji document_id=5202196682497859879>🇬🇧</emoji>'} "
                f"<code>{round(api_response.get('GBP', 0) * count, 2)}£</code> Фунт\n"
                f"{'🇨🇭 ' if not is_premium else '<emoji document_id=5442703336266543270>🇨🇭</emoji>'} "
                f"<code>{round(api_response.get('CHF', 0) * count, 2)}₣</code> Франк\n"
                f"{'🇯🇵 ' if not is_premium else '<emoji document_id=5456261908069885892>🇯🇵</emoji>'} "
                f"<code>{round(api_response.get('JPY', 0) * count, 2)}¥</code> Йена\n"
                f"{'🔵 ' if not is_premium else '<emoji document_id=5253691721174234015>💎</emoji>'} "
                f"<code>{round(api_response.get('TON', 0) * count, 2)}₮</code> Тонкоин\n"
                f"{'⚫️ ' if not is_premium else '<emoji document_id=5379965911455256722>💎</emoji>'} "
                f"<code>{round(api_response.get('NOT', 0) * count, 2)}₵</code> Ноткоин\n"
            )
            result_message = await utils.answer(message, form)

        except KeyError:
            await utils.answer(message, self.strings("keyerror"))

        except ValueError:await utils.answer(message, self.strings("inc_args"))

    # -------Functionality with list and with tags------- #
    async def cvicmd(self, message: Message):
        """Список доступных валют"""
    
        user = await message.get_sender()
        is_premium = user.premium
        instruction = (
           "<b>Список валют:</b>\n\n"
           f"{'🇺🇸 ' if not is_premium else '<emoji document_id=5202021044105257611>🇺🇸</emoji>'} "
           "<code>USD</code> <b>(Доллар)</b>\n"
           f"{'🇷🇺 ' if not is_premium else '<emoji document_id=5449408995691341691>🇷🇺</emoji>'} "
           "<code>RUB</code> <b>(Рубль)</b>\n"
           f"{'🇺🇦 ' if not is_premium else '<emoji document_id=5447309366568953338>🇺🇦</emoji>'} "
           "<code>UAH</code> <b>(Гривна)</b>\n"
           f"{'🇰🇿 ' if not is_premium else '<emoji document_id=5228718354658769982>🇰🇿</emoji>'} "
           "<code>KZT</code> <b>(Тенге)</b>\n"
           f"{'🇪🇺 ' if not is_premium else '<emoji document_id=5228784522924930237>🇪🇺</emoji>'} "
           "<code>EUR</code> <b>(Евро)</b>\n"
           f"{'🇧🇾 ' if not is_premium else '<emoji document_id=5382219601054544127>🇧🇾</emoji>'} "
           "<code>BYN</code> <b>(Бун)</b>\n"
           f"{'🇬🇧 ' if not is_premium else '<emoji document_id=5202196682497859879>🇬🇧</emoji>'} "
           "<code>GBP</code> <b>(Фунт)</b>\n"
           f"{'🇨🇭 ' if not is_premium else '<emoji document_id=5442703336266543270>🇨🇭</emoji>'} "
           "<code>CHF</code> <b>(Франк)</b>\n"
           f"{'🇯🇵 ' if not is_premium else '<emoji document_id=5456261908069885892>🇯🇵</emoji>'} "
           "<code>JPY</code> <b>(Йена)</b>\n"
           f"{'🔵 ' if not is_premium else '<emoji document_id=5253691721174234015>💎</emoji>'} "
           "<code>TON</code> <b>(Тонкоин)</b>\n"
           f"{'⚫️ ' if not is_premium else '<emoji document_id=5379965911455256722>💎</emoji>'} "
           "<code>NOT</code> <b>(Ноткоин)</b>\n\n"
           "<b>Использовать через:</b> <code>.cv</code> «число» «название»\n"
           "<b>Пример:</b> <code>.cv 20 RUB</code>"
        )
        await message.edit(instruction, parse_mode='html')
        
        # Хер # Херня # Хератень # Нахер # Захер # Похер
        # Может быть                     # Не может быть
        # Идея Александра              # Кодер Александр 
        # Авторы     модуля    Александр    и     Всякое
        # Код не пиздием и не меняйте иначе засужу нахуй
        # Автор не несёт ответ за твои последствия падла
        # Не    будь    ебланом   не    лезь   в  скрипт
