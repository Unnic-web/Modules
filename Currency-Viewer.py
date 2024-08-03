__version__ = (1, 0, 0)
#┏┓━┏┓━━┏┓━━┏┓━━┏━━━━┓━━━━━┏┓━━━━━━━━━━━━
#┃┃━┃┃━━┃┃━━┃┃━━┃┏┓┏┓┃━━━━┏┛┗┓━━━━━━━━━━━
#┃┗━┛┃┏┓┃┃┏┓┃┃┏┓┗┛┃┃┗┛┏┓┏┓┗┓┏┛┏━━┓┏━┓━━━━
#┃┏━┓┃┣┫┃┗┛┛┃┗┛┛━━┃┃━━┃┃┃┃━┃┃━┃┏┓┃┃┏┛━━━━
#┃┃━┃┃┃┃┃┏┓┓┃┏┓┓━┏┛┗┓━┃┗┛┃━┃┗┓┃┗┛┃┃┃━━━━━
#┗┛━┗┛┗┛┗┛┗┛┗┛┗┛━┗━━┛━┗━━┛━┗━┛┗━━┛┗┛━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# meta developer: @unnic
#██╗░░░██╗███╗░░██╗███╗░░██╗██╗░█████╗░
#██║░░░██║████╗░██║████╗░██║██║██╔══██╗
#██║░░░██║██╔██╗██║██╔██╗██║██║██║░░╚═╝
#██║░░░██║██║╚████║██║╚████║██║██║░░██╗
#╚██████╔╝██║░╚███║██║░╚███║██║╚█████╔╝
#░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░╚════╝

from .. import loader, utils
from telethon.tl.types import Message
import requests
import asyncio

class ВалютаMod(loader.Module):
    """Модуль для просмотра валют"""

    strings = {
        "name": "Валюта",
        "inc_args": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Неправильные аргументы</b>",
        "keyerror": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Возможно, валюта отсутствует в базе данных сайта или вы ввели неправильное название.</b>",
        "currency_not_supported": "<emoji document_id=5787544344906959608>ℹ️</emoji> <b>Данная валюта не поддерживается. Пожалуйста, проверьте правильность названия.</b>"
    }

    async def cryptocmd(self, message: Message):
        """Используйте .crypto <число> <название валюты>."""
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
        api_url = f"https://min-api.cryptocompare.com/data/price?fsym={currency}&tsyms=USD,RUB,UAH,KZT,EUR,BYN,TON,NOT"
        api_response = requests.get(api_url).json()

        # Проверяем, доступна ли валюта
        if 'Response' in api_response and api_response['Response'] == 'Error':
            await utils.answer(message, self.strings("currency_not_supported"))
            return
        
        try:
            count = float(args_list[0])
            form = (
                "<b>Поиск по курсу: {} {}</b>\n<b>Свежие результаты:</b>\n\n"
                "<emoji document_id=5202021044105257611>🇺🇸</emoji> <code>{}$ </code> Долар\n"
                "<emoji document_id=5449408995691341691>🇷🇺</emoji> <code>{}₽ </code> Рубль\n"
                "<emoji document_id=5447309366568953338>🇺🇦</emoji> <code>{}₴ </code> Гривна\n"
                "<emoji document_id=5228718354658769982>🇰🇿</emoji> <code>{}₸ </code> Тенге\n"
                "<emoji document_id=5228784522924930237>🇪🇺</emoji> <code>{}€ </code> Евро\n"
                "<emoji document_id=5382219601054544127>🇧🇾</emoji> <code>{}Br</code> Бун\n"
                "<emoji document_id=5253691721174234015>💎</emoji> <code>{}₮ </code> Тонкоин\n"
                "<emoji document_id=5379965911455256722>💎</emoji> <code>{}₵ </code> Ноткоин\n"
            ).format(
                count,
                currency,
                round(api_response.get("USD", 0) * count, 2),
                round(api_response.get("RUB", 0) * count, 2),
                round(api_response.get("UAH", 0) * count, 2),
                round(api_response.get("KZT", 0) * count, 2),
                round(api_response.get("EUR", 0) * count, 2),
                round(api_response.get("BYN", 0) * count, 2),
                round(api_response.get("TON", 0) * count, 2),
                round(api_response.get("NOT", 0) * count, 2) 
            )

            result_message = await utils.answer(message, form)
        except KeyError:
            await utils.answer(message, self.strings("keyerror"))
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))

