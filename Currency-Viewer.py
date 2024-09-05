__version__ = (1, 0, 1)
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

from .. import loader, utils # Александр
from telethon.tl.types import Message # type: ignore
import requests

class CurrencyMod(loader.Module): # Александр
    """Модуль для сравнения курсов"""

    strings = {
        "name": "Currency",
        "inc_args": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Неправильные аргументы</b>",
        "keyerror": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Возможно, валюта отсутствует в базе данных сайта или вы ввели неправильное название.</b>",
        "currency_not_supported": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Данная валюта не поддерживается. Пожалуйста, проверьте правильность названия.</b>"
    }

    async def cvcmd(self, message: Message): # Александр
        """Используйте .cv <число> <название валюты>."""
        args = utils.get_args_raw(message)
        tray = "RUB"
        if not args:
            args = "1 " + tray

        args_list = args.split(" ")
        try:
            if len(args_list) == 1 and isinstance(float(args_list[0]), float):
                args_list.append(str(tray))
        except Exception:
            args_list = ["1", args_list[0]]
        
        currency = args_list[1].upper()
        api_url = f"https://min-api.cryptocompare.com/data/price?fsym={currency}&tsyms=USD,RUB,UAH,KZT,EUR,BYN,GBP,CHF,JPY,TON,NOT"
        api_response = requests.get(api_url).json()

        if 'Response' in api_response and api_response['Response'] == 'Error':
            await utils.answer(message, self.strings("currency_not_supported"))
            return
        
        try:
            count = float(args_list[0])
            form = (
                "<b>Поиск по курсу: {} {}</b>\n<b>Свежие результаты:</b>\n\n"
                "<code>{}$ </code> Долар\n"
                "<code>{}₽ </code> Рубль\n"
                "<code>{}₴ </code> Гривна\n"
                "<code>{}₸ </code> Тенге\n"
                "<code>{}€ </code> Евро\n"
                "<code>{}Br</code> Бун\n"
                "<code>{}£ </code> Фунт\n"
                "<code>{}₣ </code> Франк\n"
                "<code>{}¥ </code> Йена\n"
                "<code>{}₮ </code> Тонкоин\n"
                "<code>{}₵ </code> Ноткоин\n"
            ).format(
                count,
                currency,
                round(api_response.get("USD", 0) * count, 2),
                round(api_response.get("RUB", 0) * count, 2),
                round(api_response.get("UAH", 0) * count, 2),
                round(api_response.get("KZT", 0) * count, 2),
                round(api_response.get("EUR", 0) * count, 2),
                round(api_response.get("BYN", 0) * count, 2),
                round(api_response.get("GBP", 0) * count, 2), 
                round(api_response.get("CHF", 0) * count, 2),
                round(api_response.get("JPY", 0) * count, 2),
                round(api_response.get("TON", 0) * count, 2),
                round(api_response.get("NOT", 0) * count, 2)
            )

            result_message = await utils.answer(message, form)
        except KeyError:
            await utils.answer(message, self.strings("keyerror"))
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))


    async def cvicmd(self, message: Message): # Всякое и Александр
        """Список доступных валют"""
        instruction = (
            "<b>Список валют</b>\n\n"
            "<code>USD</code> <b>(Долар)</b>\n"
            "<code>RUB</code> <b>(Рубль)</b>\n"
            "<code>UAH</code> <b>(Гривна)</b>\n"
            "<code>KZT</code> <b>(Тенге)</b>\n"
            "<code>EUR</code> <b>(Евро)</b>\n"
            "<code>BYN</code> <b>(Бун)</b>\n"
            "<code>JPY</code> <b>(Йена)</b>\n"
            "<code>GBP</code> <b>(Фунт)</b>\n"
            "<code>CHF</code> <b>(Франк)</b>\n\n"
            "<code>TON</code> <b>(Тонкоин)</b>\n"
            "<code>NOT</code> <b>(Ноткоин)</b>\n\n"
            "<b>Использовать через:</b> <code>.cv</code> <количество> <название>"
        )
        await message.edit(instruction, parse_mode='html')
        # Хер # Херня # Хератень # Нахер # Захер # Похер
        # Может быть                     # Не может быть
		# Идея Александра              # Кодер Александр 
	    # Авторы    модуля    Александр     и     Всякое
