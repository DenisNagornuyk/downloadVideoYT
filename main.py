from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from moviepy.editor import VideoFileClip
from aiogram.utils import executor
from pytube import YouTube
from gtts import gTTS
from aiogram import *
import os
print('bot started')

API_TOKEN = '5113551442:AAHE7YHc1dNr5K2bVUaeq9pp0JOrf3eoQLk'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['download'])
async def download(message: types.Message):
	chat_id = message.chat.id
	await bot.send_message(chat_id, "Пришліть посилання для встановлення")
@dp.message_handler()
async def text_message(message:types.Message):
	chat_id = message.chat.id
	url = message.text
	yt = YouTube(url)
	if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
		await bot.send_message(chat_id, f"*Починаю скачування відео* та конвертую в mp3: *{yt.title}*\n"
										f"*Channel*: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
		await download_youtube_video(url, message,bot)
async def download_youtube_video(url, message,bot):
	try:
		yt = YouTube(url)
		stream = yt.streams.filter(progressive=True, file_extension="mp4")
		stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
		with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
			await bot.send_video(message.chat.id, video, caption=f"{yt.title}", parse_mode="Markdown")
			os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")
	except Exception as net:
		print(Exception)
		print(net)
		message_text = f'''<i>"Дуже велике відео для встановлення" </i>\n {net}'''
		await bot.send_message(message.chat.id, message_text, parse_mode="HTML")
		await message.reply("Натомість конвертую в mp3")
		stream = yt.streams.filter(only_audio=True).first()
		stream.download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
	with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as mp3:
		# так ож прописати відправку аудіо
		await bot.send_audio(message.chat.id, mp3, caption=f"{yt.title}", parse_mode="Markdown")
		os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")



# @dp.message_handler(commands=['mp3'])
# async def mp3(message: types.Message):
# 	chat_id = message.chat.id
# 	await bot.send_message(chat_id, "Пришліть посилання з для встановлення mp3")
# @dp.message_handler()
# async def text_message(message:types.Message):
# 	chat_id = message.chat.id
# 	url = message.text
# 	yt = YouTube(url)
# 	if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
# 		await bot.send_message(chat_id, f"*Починаю скачування відео та конвертування в mp3*: *{yt.title}*\n"
# 										f"*Channel*: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
# 		await download_youtube_video(url, message,bot)

# async def download_youtube_video(url, message,bot):
# 	yt = YouTube(url)
# 	# потрібно вказати only_audio=True замість progressive=True, file_extension="mp4"
	stream = yt.streams.filter(only_audio=True).first()
	stream.download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
	with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as mp3:
		# так ож прописати відправку аудіо
		await bot.send_audio(message.chat.id, mp3, caption=f"{yt.title}", parse_mode="Markdown")
		os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


# kb1 = InlineKeyboardButton(text='Українській', callback_data='uk')
# kb2 = InlineKeyboardButton(text='Русский'    , callback_data='ru')
# kb3 = InlineKeyboardButton(text='English'    , callback_data='en')
# delete = InlineKeyboardButton('Видалити|Удалить|Delete'      , callback_data='message_delete')
# markup = InlineKeyboardMarkup().add(kb1, kb2, kb3).insert(delete)

# #Реагируем на команду /start, при этом выводим сообщение с инлайн кнопкой
# @dp.message_handler(commands='voice')
# async def del_mes(message: types.Message):
#     await bot.send_message(message.chat.id, 'Мова/Язык/Language', reply_markup=markup)

# #Если нажимаем на кнопку - удаляется сообщение.
# @dp.callback_query_handler(lambda c: c.data == 'message_delete')
# async def send_msg_to_user(call: types.CallbackQuery):
#     await call.answer('Удалено')
#     await bot.delete_message(call.message.chat.id, call.message.message_id)


# #UK
# @dp.callback_query_handler(lambda c: c.data == 'uk')
# async def send_uk(call: types.CallbackQuery):
# 	await call.answer('Українська')# повідомлення на єкран
# 	if call.data == 'uk':
# 		await bot.send_message(call.message.chat.id, 'Напишіть ваш текст для Озвучення')
# @dp.message_handler()
# async def mesuk(message: types.Message):
# 	t = gTTS(text=message.text, lang='uk', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")


# #RU
# @dp.callback_query_handler(lambda c: c.data == 'ru')
# async def send_ru(call: types.CallbackQuery):
# 	await call.answer('Русский')# повідомлення на єкран
# 	if call.data == 'ru':
# 		await bot.send_message(call.message.chat.id, 'Напишите ваш текст для Озвучивания')
# @dp.message_handler()
# async def mesru(message: types.Message):
# 	t = gTTS(text=message.text, lang='ru', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")


# #EN

# @dp.callback_query_handler(lambda c: c.data == 'en')
# async def send_en(call: types.CallbackQuery):
# 	await call.answer('English')# повідомлення на єкран
# 	if call.data == 'en':
# 		await bot.send_message(call.message.chat.id, 'Write your text for Voiceover')
# @dp.message_handler()
# async def mesen(message: types.Message):
# 	t = gTTS(text=message.text, lang='en', slow=False)
# 	t.save(f"{message.text}.mp3")
# 	await bot.send_audio(message.chat.id, open(f'{message.text}.mp3', 'rb'))
# 	os.remove(f"{message.text}.mp3")


CHAT_ID=1833097824
async def main():
    bot = Bot(TOKEN)
    await bot.send_message(CHAT_ID, "I'm started")
    await bot.session.close()  # replace with `await bot.close()` on 2.x
    # await asyncio.sleep(0.1)
# print("id: ", message.from_user.id, 
	# 	  "\nName: ", message.from_user.full_name, 
	# 	  "\nmessage: ", message.text)
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
	asyncio.run(main())
