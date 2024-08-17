__version__ = (1, 0, 0)
# ┏┓ ┏┓  ┏┓  ┏┓  ┏━━━━┓     ┏┓
# ┃┃ ┃┃  ┃┃  ┃┃  ┃┏┓┏┓┃    ┏┛┗┓
# ┃┗━┛┃┏┓┃┃┏┓┃┃┏┓┗┛┃┃┗┛┏┓┏┓┗┓┏┛┏━━┓┏━┓
# ┃┏━┓┃┣┫┃┗┛┛┃┗┛┛  ┃┃  ┃┃┃┃ ┃┃ ┃┏┓┃┃┏┛
# ┃┃ ┃┃┃┃┃┏┓┓┃┏┓┓ ┏┛┗┓ ┃┗┛┃ ┃┗┓┃┗┛┃┃┃
# ┗┛ ┗┛┗┛┗┛┗┛┗┛┗┛ ┗━━┛ ┗━━┛ ┗━┛┗━━┛┗┛
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# meta banner: https://t.me/HikkTutor
# meta developer: @unnic
# ██    ██ ███   ██ ███   ██ ██  █████
# ██    ██ ████  ██ ████  ██ ██ ██   ██ 
# ██    ██ ██ ██ ██ ██ ██ ██ ██ ██
# ██    ██ ██  ████ ██  ████ ██ ██   ██ 
#  ██████  ██   ███ ██   ███ ██  █████  
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
            'А': '<emoji document_id=5242434345603441736>😀</emoji>', 'Б': '<emoji document_id=5242670122128123193>😤</emoji>',
            'В': '<emoji document_id=5242247729274432503>🤔</emoji>', 'Г': '<emoji document_id=5242715811990218731>😞</emoji>',
            'Д': '<emoji document_id=5242410607319197689>😉</emoji>', 'Е': '<emoji document_id=5242375027810117782>😃</emoji>',
            'Ё': '<emoji document_id=5242412123442652870>😞</emoji>', 'Ж': '<emoji document_id=5242302288243992483>🤨</emoji>',
            'З': '<emoji document_id=5242222066844837762>😠</emoji>', 'И': '<emoji document_id=5242217552834208944>🤣</emoji>',
            'Й': '<emoji document_id=5244571285106731156>😃</emoji>', 'К': '<emoji document_id=5242275530597738033>🤣</emoji>',
            'Л': '<emoji document_id=5242579223440271422>😣</emoji>', 'М': '<emoji document_id=5242459020190558814>😃</emoji>',
            'Н': '<emoji document_id=5242602875825170178>😍</emoji>', 'О': '<emoji document_id=5242627876829800669>😶‍🌫️</emoji>',
            'П': '<emoji document_id=5244611911202384851>😯</emoji>', 'Р': '<emoji document_id=5242204762421602006>😚</emoji>',
            'С': '<emoji document_id=5242459346608072238>😞</emoji>', 'Т': '<emoji document_id=5242686125176269211>🤔</emoji>',
            'У': '<emoji document_id=5242260313528609101>😶‍🌫️</emoji>', 'Ф': '<emoji document_id=5242738253194340808>😠</emoji>',
            'Х': '<emoji document_id=5242454179762416237>😀</emoji>', 'Ц': '<emoji document_id=5244927153211975204>😋</emoji>',
            'Ч': '<emoji document_id=5242262001450757430>🤔</emoji>', 'Ш': '<emoji document_id=5242492035604162920>🤔</emoji>',
            'Щ': '<emoji document_id=5244945119060175623>😡</emoji>', 'Ъ': '<emoji document_id=5242672054863408501>🥺</emoji>',
            'Ы': '<emoji document_id=5244805081651488041>😱</emoji>', 'Ь': '<emoji document_id=5242420429909404389>🤔</emoji>',
            'Э': '<emoji document_id=5244842241708535702>😕</emoji>', 'Ю': '<emoji document_id=5244733402942286508>😊</emoji>',
            'Я': '<emoji document_id=5244596891701750883>😐</emoji>', '0': '<emoji document_id=5242296064836381345>☹️</emoji>',
            '1': '<emoji document_id=5242633284193626695>🤥</emoji>', '2': '<emoji document_id=5242725385472322786>😯</emoji>',
            '3': '<emoji document_id=5244493370105014334>🥶</emoji>', '4': '<emoji document_id=5244864519703898337>😦</emoji>',
            '5': '<emoji document_id=5244881686688180520>🫢</emoji>', '6': '<emoji document_id=5242334521973550934>🫥</emoji>',
            '7': '<emoji document_id=5242235256689405269>😴</emoji>', '8': '<emoji document_id=5244793171707177560>😱</emoji>',
            '9': '<emoji document_id=5244684556279229932>😖</emoji>',
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
            '9': '<emoji document_id=5237872922831367023>9️⃣</emoji>',
    }
        return ''.join([emoji_alphabet.get(char.upper(), char) if char != ' ' else '   ' for char in text]) + 'ㅤ'

    @staticmethod
    def text_to_emoji_3(text):
        """<b>Эмодзи версия 3</b>"""
        emoji_alphabet = {
            'А': '<emoji document_id=5233393203222160353>😤</emoji>', 'Б': '<emoji document_id=5233545124805354637>☹️</emoji>',
            'В': '<emoji document_id=5233304400478349373>🤔</emoji>', 'Г': '<emoji document_id=5235922642606762184>😣</emoji>',
            'Д': '<emoji document_id=5233599305817793124>😫</emoji>', 'Е': '<emoji document_id=5233468730222061383>🥶</emoji>',
            'Ё': '<emoji document_id=5233637217494116743>😒</emoji>', 'Ж': '<emoji document_id=5233304061175933555>🤓</emoji>',
            'З': '<emoji document_id=5233708453821686259>😣</emoji>', 'И': '<emoji document_id=5235803371364952007>😒</emoji>',
            'Й': '<emoji document_id=5233226081749708119>😤</emoji>', 'К': '<emoji document_id=5233402682214982503>😣</emoji>',
            'Л': '<emoji document_id=5233582121653644840>☹️</emoji>', 'М': '<emoji document_id=5233278415926209618>😤</emoji>',
            'Н': '<emoji document_id=5233557176483587475>😠</emoji>', 'О': '<emoji document_id=5235891826216414492>😒</emoji>',
            'П': '<emoji document_id=5233261193107351431>😉</emoji>', 'Р': '<emoji document_id=5233388577542382746>🤗</emoji>',
            'С': '<emoji document_id=5233524792430176328>🤓</emoji>', 'Т': '<emoji document_id=5233183286695569723>🧐</emoji>',
            'У': '<emoji document_id=5235946565574601197>😄</emoji>', 'Ф': '<emoji document_id=5233548762642655633>😣</emoji>',
            'Х': '<emoji document_id=5233307394070555562>😖</emoji>', 'Ц': '<emoji document_id=5233399027197814140>😣</emoji>',
            'Ч': '<emoji document_id=5233302935894500615>😚</emoji>', 'Ш': '<emoji document_id=5233461037935633303>😁</emoji>',
            'Щ': '<emoji document_id=5235565245493159972>😞</emoji>', 'Ъ': '<emoji document_id=5233710485341218239>😡</emoji>',
            'Ы': '<emoji document_id=5233440057020393005>😏</emoji>', 'Ь': '<emoji document_id=5235626032165300081>🥲</emoji>',
            'Э': '<emoji document_id=5235898741113760451>😤</emoji>', 'Ю': '<emoji document_id=5233628915322332331>😒</emoji>',
            'Я': '<emoji document_id=5233447049227151454>😶‍🌫️</emoji>', '0': '<emoji document_id=5233423753324537640>😞</emoji>',
            '1': '<emoji document_id=5233275564067922970>😩</emoji>', '2': '<emoji document_id=5233549226499126168>😛</emoji>',
            '3': '<emoji document_id=5233227975830283678>😡</emoji>', '4': '<emoji document_id=5233435899492050382>😲</emoji>',
            '5': '<emoji document_id=5233194303286683804>🫣</emoji>', '6': '<emoji document_id=5233206866066024559>😞</emoji>',
            '7': '<emoji document_id=5233580712904369541>😔</emoji>', '8': '',
            '9': '',
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
            elif number == '3':
                emojified_text = self.text_to_emoji_3(text)
            # Ты можешь добавить больше условий для других версий здесь!
            else:
                await message.edit("<b>Неверный номер! Пожалуйста, используйте 1-2-3</b>")
                return
        else:
            await message.edit("<b>Неверный номер! Пожалуйста, используйте только целые числа.</b>")
            return

        await message.edit(emojified_text)

    async def tsxelpcmd(self, message: Message):
        """Информация о модуле"""
        instruction = (
            "<b>Информация о паках и их пример как будет выглядеть текст</b>\n"
            "№ - пример текста (Доступно 4 эмодзи пака)\n\n"
            "1 - <emoji document_id=5242434345603441736>😀</emoji>\n"
            "2 - <emoji document_id=5442667851246742007>🔤</emoji>\n"
            "3 - \n\n"
            "<emoji document_id=5818865088970362886>❕</emoji> <b>INFO - В этих функционалах нету, знаков ?!+-= и так делее.\n"
            "Это не потому что я не смог добавить, а потому что в некоторых паках их просто нету</b>\n\n"
            "<emoji document_id=5875452644599795072>🔞</emoji> <b>Разработчик: @unnic</b>\n"
        )
        await message.edit(instruction, parse_mode='html')
