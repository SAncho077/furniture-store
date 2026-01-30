# check_password.py
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('GMAIL_PASSWORD')

if password:
    print(f"✅ Пароль найден! Длина: {len(password)} символов")
    print(f"Первые 4 символа: {password[:4]}...")
else:
    print("❌ Пароль НЕ найден в .env файле!")
    print("Проверьте что файл .env есть и в нем есть GMAIL_PASSWORD=...")