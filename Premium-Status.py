import re
from datetime import datetime
from telethon import TelegramClient
from .. import loader, utils

@loader.tds
class PremiumStatusMod(loader.Module):
    """Модуль для отображения статуса подписки Telegram Premium через @PremiumBot."""

    strings = {
        "name": "PremiumStatus"
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._client = None

    async def client_ready(self, client: TelegramClient, db):
        self._client = client

    async def otcmd(self, message):
        """Отображает информацию о подписке Telegram Premium. Используйте: .ot"""
        await message.edit("<b>Получаем данные, пожалуйста подождите...</b>")

        try:
            bot_username = 'PremiumBot'
            async with self._client.conversation(bot_username) as conv:
                start_message = await conv.send_message('/start')
                response = await conv.get_response()
                await start_message.delete()

                if response.message and "управлять своими подписками в соответствующем магазине приложений" in response.message:
                    await message.edit("<b>У вас халявная подписка, спросите у того, кто вам её подарил, сколько ещё дней осталось.</b>")
                elif response.message:
                    match = re.search(r'📆 Следующий платёж: (.*?), (\d{2}\.\d{2}\.\d{4})\.', response.message)
                    if match:
                        full_date = match.group(2)
                        expiry_date = datetime.strptime(full_date, '%d.%m.%Y')
                        remaining_days = (expiry_date - datetime.now()).days
                        await message.edit(f"<b>До окончания Premium подписки осталось: <code>{remaining_days}</code> дней.</b>")
                    else:
                        await message.edit("<b>Не удалось извлечь дату окончания подписки.</b>")
                else:
                    await message.edit("<b>Ошибка: Ответ от бота пуст или имеет некорректную структуру.</b>")

        except Exception as e:
            await message.edit(f"<b>Ошибка при получении данных: {e}</b>")