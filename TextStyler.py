# meta developer: @unnic
# meta banner: https://t.me/HikkTutor
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
                lambda: "Символ, указывающий на игнорирование сообщения",
                validator=loader.validators.String(min_len=1, max_len=1)
            ),
            loader.ConfigValue(
                "enable_bold",
                False,
                lambda: "Включить/выключить автоматическое жирное форматирование текста",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_italic",
                False,
                lambda: "Включить/выключить автоматическое курсивное форматирование текста",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_strikethrough",
                False,
                lambda: "Включить/выключить автозачёркнутый текст",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_underlined",
                False,
                lambda: "Включить/выключить автоматическое подчеркивание текста",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "enable_mono",
                False,
                lambda: "Включить/выключить автоматический моноширинный текст",
                validator=loader.validators.Boolean()
            ),
            loader.ConfigValue(
                "ignore_channels",
                True,
                lambda: "Игнорировать сообщения в каналах",
                validator=loader.validators.Boolean()
            )
        )
        super().__init__()

    def format_symbol(self, char, config_name, tag):
        if self.config[config_name]:
            return f"<{tag}>{char}</{tag}>"
        return char

    async def client_ready(self, client: TelegramClient, db):
        self._client = client
        client.add_event_handler(self.message_handler, events.NewMessage(outgoing=True))

    async def message_handler(self, event: events.NewMessage.Event):
        if self.config["ignore_channels"] and event.is_channel:
            return

        if event.message.media:
            return

        original_message = event.raw_text
        if original_message.startswith(self.config["ignore_char"]):
            return 

        # Проверка на наличие только эмодзи (без текстовых символов)
        if all(char in emoji.EMOJI_DATA for char in original_message):
            return

        formatted_message = ''.join(
            self.format_symbol(
                self.format_symbol(
                    self.format_symbol(
                        self.format_symbol(
                            self.format_symbol(
                                char,
                                "enable_bold", "b"
                            ),
                            "enable_mono", "code"
                        ),
                        "enable_underlined", "u"
                    ),
                    "enable_strikethrough", "s"
                ),
                "enable_italic", "i"
            ) for char in original_message
        )

        # Проверка, был ли текст изменён
        if formatted_message != original_message:
            await event.edit(formatted_message, parse_mode='html')

    async def струкcmd(self, message: Message):
        """Показывает инструкцию по использованию модуля."""
        instruction = (
            "<b>Информация о модуле и его функционале</b>\n\n"
            "<b><emoji document_id=4971987363145188045>🛑</emoji> Все исходящие сообщения автоматически форматируются, если включено то или инное форматирование.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Если сообщение начинается с символа игнорирования, оно не будет изменено.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Модуль не изменяет текст, содержащий только эмодзи, стикеры, GIF и медиафайлы.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Модуль не действует в каналах.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Эмодзи и стикеры в тексте останутся без изменений, если выключены все форматирования.</b>\n\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Управление настройками:</b>\n"
            f"<emoji document_id=4971987363145188045>🛑</emoji> <b>Символ игнорирования по умолчанию: .{ignore_char}</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Ты можешь изменить игнорируемый символ на любой другой символ.</b>\n"
            "<emoji document_id=4971987363145188045>🛑</emoji> <b>Ты можешь включить/выключить игнор для каналов.</b>\n"
        )
        await message.edit(instruction, parse_mode='html')