
import telebot
import os
import time
import schedule
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

bot = telebot.TeleBot(BOT_TOKEN)

quizzes = [
    {"question": "भारत का पहला प्रधानमंत्री कौन था?", "options": ["महात्मा गांधी", "लाल बहादुर शास्त्री", "जवाहरलाल नेहरू", "सरदार पटेल"], "correct": 2},
    {"question": "भारत का राष्ट्रीय पक्षी कौन है?", "options": ["तोता", "मोर", "कौआ", "गौरैया"], "correct": 1},
    {"question": "संविधान सभा के अध्यक्ष कौन थे?", "options": ["बी. आर. अम्बेडकर", "सुभाष चंद्र बोस", "राजेन्द्र प्रसाद", "जवाहरलाल नेहरू"], "correct": 2},
]

def send_quiz():
    for quiz in quizzes:
        bot.send_poll(
            chat_id=GROUP_ID,
            question=quiz["question"],
            options=quiz["options"],
            type="quiz",
            correct_option_id=quiz["correct"],
            is_anonymous=False
        )
        time.sleep(5)

schedule.every().day.at("09:30").do(send_quiz)
schedule.every().day.at("10:00").do(send_quiz)
schedule.every().day.at("13:00").do(send_quiz)
schedule.every().day.at("16:30").do(send_quiz)
schedule.every().day.at("20:00").do(send_quiz)

print("Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
