import io
import asyncio
from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import ChannelParticipantsAdmins
from .. import loader, utils

@loader.tds
class БылMod(loader.Module):
    """Разнообразный модуль для групп"""

    strings = {
        "name": "Был",
        "author": "@HikkTutor"
    }

    def init(self):
        self.name = self.strings["name"]
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client: TelegramClient, db):
        self._db = db
        self._client = client
        await client(JoinChannelRequest(channel=self.strings["author"]))

    async def логcmd(self, message: Message):
        """Прежде чем, прочти инструкцию"""
        if not message.chat:
            await message.edit("<b>Ошибка!</b>")
            return
        chat = message.chat

        f = io.BytesIO()
        f.name = f"Dump by {chat.id}.csv"
        f.write("FNAME;LNAME;USER;ID;NUMBER\n".encode())
        me = await message.client.get_me()
        participants = await message.client.get_participants(message.to_id)
        
        for i in participants:
            if i.id == me.id:
                continue
            f.write(
                f"{str(i.first_name) or ''};{str(i.last_name) or ''};{str(i.username) or ''};{str(i.id)};{str(i.phone) or ''}\n".encode()
            )
        f.seek(0)
        await message.client.send_file("me", f, caption=f"Перезагрузка чата: {chat.id}")

        await message.edit("<b>Сделал то что ты хотел, лог в избранном.</b>")
        f.close()

    async def иcmd(self, message: Message):
        """Показать ID пользователя"""
        args = utils.get_args_raw(message)

        if message.is_reply:
            reply_message = await message.get_reply_message()
            user = await message.client.get_entity(reply_message.sender_id)
        elif args:
            try:
                user = await message.client.get_entity(args)
            except Exception:
                await message.edit("<b>Ошибка</b>")
                return
        else:
            user = await message.get_sender()

        user_initials = f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.first_name
        user_id = user.id
        await message.edit(f'<emoji document_id=5972282179776940830>✈️</emoji> <a href="tg://openmessage?user_id={user_id}"><b>{user_initials}</b></a>\n<emoji document_id=4918133202012340741>👤</emoji> <code>@{user_id}</code>')

    async def тегcmd(self, message: Message):
        """Тегает всех админов чата, игнорируя ботов"""
        if not message.chat:
            await message.edit("<b>Ошибка!</b>")
            return

        chat = message.chat
        admins = await message.client.get_participants(chat, filter=ChannelParticipantsAdmins)

        # Фильтрация администраторов, исключая ботов
        real_admins = [admin for admin in admins if not admin.bot]

        if not real_admins:
            await message.edit("<b>Нет администраторов в этом чате.</b>")
            return

        # Просто тегаем настоящих администраторов
        admin_mentions = [f"<a href='tg://user?id={admin.id}'>.</a>" for admin in real_admins]

        await message.edit(" ".join(admin_mentions))

    async def хелпcmd(self, message: Message):
        """Показать информацию по командам"""
        instruction = (
            "<b>Информация:\n\n"
            "Команда <code>.лог</code> выполняет дамп чата, создавая файл, содержащий список всех участников, "
            "и отправляет его в «Избранное». Это полезно для архивирования и анализа данных о пользователях чата.</b>"
        )

        sent_message = await self._client.send_message(message.chat_id, instruction)

        await asyncio.sleep(10)
        await sent_message.delete()
