from pyngrok import ngrok
import subprocess

# Запуск Flask сервера
print("🚀 Запускаем Flask...")
subprocess.Popen(["python", "web.py"])

# Запуск Ngrok туннеля
print("🌐 Подключаю Ngrok...")
public_url = ngrok.connect(5000)
print(f"🔗 Ваш Mini App доступен по адресу: {public_url}")
