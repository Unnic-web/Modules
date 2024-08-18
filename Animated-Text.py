__version__ = (1, 0, 0)
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
import asyncio
from telethon import TelegramClient
from telethon.tl.custom import Message
from .. import loader, utils
import re

@loader.tds
class AnimatedTextMod(loader.Module):
    """Модуль для создания текста из эмодзи букв"""

    strings = {
        "name": "AnimatedText"
    }

    def init(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client: TelegramClient, db):
        self._db = db
        self._client = client

    @staticmethod
    def text_to_emoji_1(text):
        """<b>Эмодзи версия 1</b>"""
        emoji_alphabet = {
            'А': '<emoji document_id=5431799754331796642>🔤</emoji>', 'Б': '<emoji document_id=5431770230726603434>🔤</emoji>',
            'В': '<emoji document_id=5431713653122415203>🔤</emoji>', 'Г': '<emoji document_id=5431600712662398240>🔤</emoji>',
            'Д': '<emoji document_id=5431522531372709363>🔤</emoji>', 'Е': '<emoji document_id=5431442795304859349>🔤</emoji>',
            'Ё': '<emoji document_id=5429637367147280645>🔤</emoji>', 'Ж': '<emoji document_id=5431745199657202064>🔤</emoji>',
            'З': '<emoji document_id=5431890992322063045>🔤</emoji>', 'И': '<emoji document_id=5431760214862868782>🔤</emoji>',
            'Й': '<emoji document_id=5429237449857449550>🔤</emoji>', 'К': '<emoji document_id=5431675904654851368>🔤</emoji>',
            'Л': '<emoji document_id=5431394206339838877>🔤</emoji>', 'М': '<emoji document_id=5431858165887023468>🔤</emoji>',
            'Н': '<emoji document_id=5429502823001765231>🔤</emoji>', 'О': '<emoji document_id=5431534054769964878>🔤</emoji>',
            'П': '<emoji document_id=5431588021034037318>🔤</emoji>', 'Р': '<emoji document_id=5429122516532607244>🔤</emoji>',
            'С': '<emoji document_id=5429356506350891927>🔤</emoji>', 'Т': '<emoji document_id=5431412202252811166>🔤</emoji>',
            'У': '<emoji document_id=5431488124389700446>🔤</emoji>', 'Ф': '<emoji document_id=5431663161486881606>🔤</emoji>',
            'Х': '<emoji document_id=5431471949542864847>🔤</emoji>', 'Ц': '<emoji document_id=5429217254921223083>🔤</emoji>',
            'Ч': '<emoji document_id=5429557197287733096>🔤</emoji>', 'Ш': '<emoji document_id=5431447867661234937>🔤</emoji>',
            'Щ': '<emoji document_id=5431729183724154963>🔤</emoji>', 'Ъ': '<emoji document_id=5429190570289411763>🔤</emoji>',
            'Ы': '<emoji document_id=5429288263615526499>🔤</emoji>', 'Ь': '<emoji document_id=5431769517762034600>🔤</emoji>',
            'Э': '<emoji document_id=5431456302977004527>🔤</emoji>', 'Ю': '<emoji document_id=5429307754177116651>🔤</emoji>',
            'Я': '<emoji document_id=5431557539651142784>🔤</emoji>', '0': '<emoji document_id=5431795725652472535>0️⃣</emoji>',
            '1': '<emoji document_id=5429510081496496215>1️⃣</emoji>', '2': '<emoji document_id=5431497367159320438>2️⃣</emoji>',
            '3': '<emoji document_id=5431709809126686430>3️⃣</emoji>', '4': '<emoji document_id=5429090029399980221>4️⃣</emoji>',
            '5': '<emoji document_id=5431382807496635927>5️⃣</emoji>', '6': '<emoji document_id=5431692332904756522>6️⃣</emoji>',
            '7': '<emoji document_id=5431496886122983854>7️⃣</emoji>', '8': '<emoji document_id=5431605767838906399>9️⃣</emoji>',
            '9': '<emoji document_id=5429574471646198158>9️⃣</emoji>', '?': '<emoji document_id=5431681312018675197>❓</emoji>',
            '!': '<emoji document_id=5429188895252167663>❗️</emoji>', '₽': '<emoji document_id=5429596564957969664>❗️</emoji>',
            ',': '<emoji document_id=5431623411564557335>🔤</emoji>', '.': '<emoji document_id=5431886005865035166>🔤</emoji>',
        }
        return ''.join([emoji_alphabet.get(char.upper(), char) if char != ' ' else '   ' for char in text]) + 'ㅤ'

    @staticmethod
    def text_to_emoji_2(text):
        """<b>Эмодзи версия 2</b>"""
        emoji_alphabet = {
            'А': '<emoji document_id=5442667851246742007>🔤</emoji>', 'Б': '<emoji document_id=5442708515997100433>🔤</emoji>',
            'В': '<emoji document_id=5449413294953606262>🔤</emoji>', 'Г': '<emoji document_id=5452141660043488430>🔤</emoji>',
            'Д': '<emoji document_id=5451814740017817067>🔤</emoji>', 'Е': '<emoji document_id=5195169080914486911>🔤</emoji>',
            'Ё': '<emoji document_id=5197457624173389781>🔤</emoji>', 'Ж': '<emoji document_id=5452108017564657802>🔤</emoji>',
            'З': '<emoji document_id=5472327074326786286>🔤</emoji>', 'И': '<emoji document_id=5449768699202381205>🔤</emoji>',
            'Й': '<emoji document_id=5195365902085792989>🔤</emoji>', 'К': '<emoji document_id=5456289915551622074>🔤</emoji>',
            'Л': '<emoji document_id=5474517911374668774>🔤</emoji>', 'М': '<emoji document_id=5469720553164122863>🔤</emoji>',
            'Н': '<emoji document_id=5469708475716085118>🔤</emoji>', 'О': '<emoji document_id=5449645429346020359>🔤</emoji>',
            'П': '<emoji document_id=5456332233864391674>🔤</emoji>', 'Р': '<emoji document_id=5465662534918875863>🔤</emoji>',
            'С': '<emoji document_id=5463032576119679082>🔤</emoji>', 'Т': '<emoji document_id=5442819107110004737>🔤</emoji>',
            'У': '<emoji document_id=5188633966051076002>🔤</emoji>', 'Ф': '<emoji document_id=5199539798548687111>🔤</emoji>',
            'Х': '<emoji document_id=5453904585204704787>🔤</emoji>', 'Ц': '<emoji document_id=5199431226070412282>🔤</emoji>',
            'Ч': '<emoji document_id=5204235000962098442>🔤</emoji>', 'Ш': '<emoji document_id=5451785663089224462>🔤</emoji>',
            'Щ': '<emoji document_id=5201857350016708252>🔤</emoji>', 'Ъ': '<emoji document_id=5472079100094982899>🔤</emoji>',
            'Ы': '<emoji document_id=5190588236300296545>🔤</emoji>', 'Ь': '<emoji document_id=5472419270094760054>🔤</emoji>',
            'Э': '<emoji document_id=5447451113374624122>🔤</emoji>', 'Ю': '<emoji document_id=5188362206290388816>🔤</emoji>',
            'Я': '<emoji document_id=5204256643302303428>🔤</emoji>', '0': '<emoji document_id=5238055991517390123>0️⃣</emoji>',
            '1': '<emoji document_id=5235776368905562305>1️⃣</emoji>', '2': '<emoji document_id=5237704680372447424>2️⃣</emoji>',
            '3': '<emoji document_id=5238044171767393675>3️⃣</emoji>', '4': '<emoji document_id=5235533321001250232>4️⃣</emoji>',
            '5': '<emoji document_id=5238171599152097811>5️⃣</emoji>', '6': '<emoji document_id=5235500881113263583>6️⃣</emoji>',
            '7': '<emoji document_id=5237875542761417785>7️⃣</emoji>', '8': '<emoji document_id=5238067300166281132>8️⃣</emoji>',
            '9': '<emoji document_id=5237872922831367023>9️⃣</emoji>', '?': '<emoji document_id=5210880311801423356>🔤</emoji>',
            '!': '<emoji document_id=5211108619377977503>🔤</emoji>', '₽': '<emoji document_id=5256065601138337797>🔤</emoji>',
            ',': '<emoji document_id=5255809805771090545>🔤</emoji>', '.': '<emoji document_id=5255831662859660095>🔤</emoji>',
        }
        return ''.join([emoji_alphabet.get(char.upper(), char) if char != ' ' else '   ' for char in text]) + 'ㅤ'

    async def atcmd(self, message: Message):
        """Использование: .at <номер> <текст> - Создает текст из эмодзи"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("<b>Введите номер и текст для конвертации!</b>")
            return

        parts = args.split(maxsplit=1)
        if len(parts) < 2:
            await message.edit("<b>Введите номер и текст для конвертации!</b>")
            return

        number = parts[0]
        text = parts[1]

        if number.isdigit():
            if number == '1':
                emojified_text = self.text_to_emoji_1(text)
            elif number == '2':
                emojified_text = self.text_to_emoji_2(text)
            # Вы можете добавить больше условий для других версий здесь
            else:
                await message.edit("<b>Неверный номер! Пожалуйста, используйте 1, или 2.</b>")
                return
        else:
            await message.edit("<b>Неверный номер! Пожалуйста, используйте только целые числа.</b>")
            return

        await message.edit(emojified_text)
        
    async def atxelpcmd(self, message: Message):
    """Информация о модуле"""
    instruction = (
        "<b>Информация о паках и их пример как будет выглядеть текст</b>\n"
        "№ - пример текста (Доступно 2 эмодзи пака)\n\n"
        "1 - <emoji document_id=5296400742821673630>💙</emoji>\n"
        "2 - <emoji document_id=5442667851246742007>🔤</emoji>\n\n"
        "<emoji document_id=5818865088970362886>❕</emoji> <b>В этих функционалах нету, знаков ?!+-= и так далее.\n"
        "Это не потому что я не смог добавить, а потому что в некоторых паках их просто нету</b>\n\n"
        "<emoji document_id=5875452644599795072>🔞</emoji> <b>Разработчик: @unnic</b>\n"
    )
    await message.edit(instruction, parse_mode="html")

