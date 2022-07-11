from aiogram import *
from pytube import YouTube
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
		await bot.send_message(chat_id, f"*Починаю скачування відео*: *{yt.title}*\n"
										f"*Channel*: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
		await download_youtube_video(url, message,bot)

async def download_youtube_video(url, message,bot):
	yt = YouTube(url)
	stream = yt.streams.filter(progressive=True, file_extension="mp4")
	stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
	with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
		await bot.send_video(message.chat.id, video, caption="*Your video*", parse_mode="Markdown")
		os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")
	print("id: ", message.from_user.id, 
	      "\nName: ", message.from_user.full_name, 
	      "\nmessage: ", message.text)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
