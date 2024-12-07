import asyncio
import logging
from generator import generate
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command 
from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.fsm.context import FSMContext
from config import TOKEN
from FSM import Work

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()



@dp.message(CommandStart())
async def Start(message: Message):
    await message.answer(f'{message.from_user.first_name}, Добро пожалувать в бота')


@dp.message(Work.proces)
async def Stop(message: Message):
    await message.answer('Подождите, ваше сообщение генерируется')

@dp.message()
async def ai(message: Message, state: FSMContext):
    await state.set_state(Work.proces)
    res = await generate(message.text)
    await message.answer(res.choices[0].message.content)
    await state.clear()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')        
    asyncio.run(main())