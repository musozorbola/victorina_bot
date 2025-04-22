import os
import random

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from keyboards import level_buttons

router = Router()

@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    photo =FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    text = ("Hush kelibsiz Muso bilag'on,sizga bir nechta savolar berib bilimingizni tekshirib berami!")
    await message.answer_photo(photo=photo, caption=text, reply_markup=level_buttons)

@router.message(F.text == "LEVEL 1️⃣")
async def level_1(message: Message):
    print(message.text)
    question = (f"{random.randint(1,11)}{random.choice(['+', '-', '*'])}"
                f"{random.randint(1,11)}")
    await message.answer(text=f"SAVOL: {question} = ?")

@router.message(F.text == "LEVEL 2️⃣")
async def level_2(message: Message):
    print(message.text)
    question = (f"{random.randint(100, 500)}{random.choice(['+', '-'])}"
                f"{random.randint(100, 500)}")
    await message.answer(text=f"SAVOL: {question} = ?")

@router.message(F.text == "LEVEL 3️⃣")
async def level_3(message: Message):
    print(message.text)
    question = (f"{random.randint(600, 1500)}{random.choice([':', '*','+'])}"
                f"{random.randint(600, 1500)}")
    await message.answer(text=f"SAVOL: {question} = ?")