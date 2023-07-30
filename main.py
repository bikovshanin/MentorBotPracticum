import logging
import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.utils.markdown import hlink
from aiogram.types.message import ContentType
from aiogram.dispatcher.filters import Text

import keyboards as kb
from static import texts, links
from config import TOKEN


async def start_command(message: types.Message):
    await message.reply(
        f'Приветствую тебя <b>{message.from_user.username}</b>!\n'
        f'{texts["start"]}',
        reply_markup=kb.inl_kb
    )


async def help_command(message: types.Message):
    await message.reply(texts['help'])


async def text_command(message: types.Message):
    await message.bot.send_message(
        message.from_user.id, texts['hobby']
    )


async def link_command(message: types.Message):
    await message.bot.send_message(
        message.from_user.id,
        text=hlink(
            'Репозиторий',
            links['repository']
        )
    )


async def get_media(callback_query: types.CallbackQuery):
    action = callback_query.data.split("_")[1]
    voice1 = types.InputFile(links['voice1'])
    voice2 = types.InputFile(links['voice2'])
    voice3 = types.InputFile(links['voice3'])
    photo = open(links['photo1'], 'rb')
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(links['photo2']), caption='11 класс')
    media.attach_photo(types.InputFile(links['photo3']), caption='10 класс')
    if action == 'btn1':
        await callback_query.message.edit_text(
            texts['btn11'],
            reply_markup=kb.inl_kb2
        )
        await callback_query.answer()
    elif action == 'btn3':
        await callback_query.message.edit_text(
            texts['btn3'],
            reply_markup=kb.inl_kb3
        )
        await callback_query.answer()
    elif action == 'btn4':
        await callback_query.message.edit_text(
            texts['btn4'],
            reply_markup=kb.inl_kb4
        )
        await callback_query.answer()
    elif action == 'btn5':
        await callback_query.message.edit_text(
            texts["start"],
            reply_markup=kb.inl_kb
        )
        await callback_query.answer()
    elif action == 'btn11':
        await callback_query.message.edit_text(
            texts['btn11'],
            reply_markup=kb.inl_kb2
        )
        await callback_query.answer()
    elif action == 'btn6':
        await callback_query.bot.send_photo(
            callback_query.message.chat.id,
            photo=photo,
            caption='Это я'
        )
        await callback_query.answer()
    elif action == 'btn7':
        await callback_query.bot.send_media_group(
            callback_query.message.chat.id,
            media=media
        )
        await callback_query.answer()
    elif action == 'btn8':
        await callback_query.bot.send_voice(
            callback_query.message.chat.id,
            voice=voice1
        )
        await callback_query.answer()
    elif action == 'btn9':
        await callback_query.bot.send_voice(
            callback_query.message.chat.id,
            voice=voice2
        )
        await callback_query.answer()
    elif action == 'btn10':
        await callback_query.bot.send_voice(
            callback_query.message.chat.id,
            voice=voice3
        )
        await callback_query.answer()


async def unknown_message(msg: types.Message):
    await msg.reply(texts['unknown'])


async def main():
    print('Бот запустился!')
    bot = Bot(
        token=TOKEN,
        parse_mode=types.ParseMode.HTML,
        timeout=3
    )
    dp = Dispatcher(bot)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(help_command, commands="help")
    dp.register_message_handler(text_command, commands="text")
    dp.register_message_handler(link_command, commands="link")
    dp.register_callback_query_handler(get_media, Text(startswith='inl_'))
    dp.register_message_handler(unknown_message, content_types=ContentType.ANY)
    try:
        await dp.skip_updates()
        await dp.start_polling()
    except Exception as ex:
        logging.error(f'[!!! exception] - {ex}', exc_info=True)
    finally:
        await (await bot.get_session()).close()


if __name__ == '__main__':
    asyncio.run(main())
