__version__ = (1, 0, 0)
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
from telethon import TelegramClient, events
from telethon.tl.types import Message
from .. import loader, utils
import emoji

@loader.tds
class TextStylerMod(loader.Module):
    """Модуль для автоматического форматирования текста"""

    strings = {
        "name": "TextStyler"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "ignore_char",
                ".",
                lambda: "Символ, указывающий на игнорирование сообщения.",
                validator=loader.validators.String(min_len=1, max_len=1)
            ),
            loader.ConfigValue(
                "enable_bold",
                False,
                lambda: "Включить/выключить автоматическое жирное форматирование текста.",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_italic",
                False,
                lambda: "Включить/выключить автоматическое курсивное форматирование текста.",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_strikethrough",
                False,
                lambda: "Включить/выключить автозачеркнутый текст.",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_underlined",
                False,
                lambda: "Включить/выключить автоматическое подчеркивание текста.",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_mono",
                False,
                lambda: "Включить/выключить автоматический моноширинный текст.",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "ignore_channels",
                True,
                lambda: "Игнорировать сообщения в каналах.",
                validator=loader.validators.Boolean()
            )
        )
        super().__init__()

    async def client_ready(self, client, db):
        self._client = client
        client.add_event_handler(self.message_handler, events.NewMessage(outgoing=True))

    def format_text(self, text):
        if self.config["enable_bold"]:
            text = f"<b>{text}</b>"
        if self.config["enable_italic"]:
            text = f"<i>{text}</i>"
        if self.config["enable_underlined"]:
            text = f"<u>{text}</u>"
        if self.config["enable_strikethrough"]:
            text = f"<s>{text}</s>"
        if self.config["enable_mono"]:
            text = f"<code>{text}</code>"
        return text

    async def message_handler(self, event):
        # Мы хотим обрабатывать личные сообщения и групповые, но игнорировать каналы
        if self.config["ignore_channels"] and event.is_channel:
            return

        # Если есть медиа, игнорируем сообщение
        if event.message.media:
            return

        original_message = event.raw_text
        if original_message.startswith(self.config["ignore_char"]):
            return 

        # Форматирование всего сообщения
        formatted_message = self.format_text(original_message)

        # Проверка, был ли текст изменён
        if formatted_message != original_message:
            await event.edit(formatted_message, parse_mode='html')

    async def tsxelpcmd(self, message: Message):
        """Показывает инструкцию по использованию модуля."""
        instruction = (
            "<b>Информация о модуле и его функционале</b>\n\n"
            "<b><emoji document_id=4971987363145188045>🛑</emoji> Все исходящие сообщения автоматически форматируются, если включено то или инное форматирование.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Если сообщение начинается с символа игнорирования, оно не будет изменено.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Модуль не изменяет текст, содержащий только эмодзи, стикеры, GIF и медиафайлы.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Модуль не действует в каналах.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Эмодзи и стикеры в тексте останутся без изменений, если выключены все форматирования.</b>\n\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Информация настроек:</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Символ игнорирования по умолчанию: «<code>.</code>»</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Ты можешь изменить игнорируемый символ на любой другой 1 символ, через конфиг.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Ты можешь включить/выключить игнор для каналов.</b>\n\n"
            "<emoji document_id=5875452644599795072>🔞</emoji> <b>Разработчик: @unnic</b>\n"
        )
        await message.edit(instruction, parse_mode='html')
# Хер
