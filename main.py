import openai
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.executor import start_polling
from background import keep_alive


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
openai.organization = "your_token_openai_organization"
openai.api_key = "your_openai_api_token"
openai.Model.list()


@dp.message_handler(content_types=['text'])
async def handle_message(message: Message):
    if message.chat.type in ('supergroup', 'group') and "your_id_bot" not in message.text:
        return
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}\n",
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5
    )
    # Send the response back to the user
    await bot.send_message(chat_id=message.chat.id, text=response["choices"][0]["text"])


keep_alive()
if __name__ == '__main__':
  start_polling(dp)
