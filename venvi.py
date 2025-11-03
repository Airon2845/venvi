#!/usr/bin/env python3
import os
import subprocess
import sys

def main():
    project_name = input("Введите имя вашего нового Python-проекта: ").strip()
    
    # 1. Создаем папку проекта
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    print(f"[+] Папка проекта '{project_name}' создана.")
    
    # 2. Создаем виртуальное окружение
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("[+] Виртуальное окружение 'venv' создано.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Ошибка при создании venv: {e}")
        return
    
    # 3. Определяем команду активации в зависимости от ОС
    if os.name == 'nt':  # Windows
        activate_script = "venv\\Scripts\\activate"
        activate_command = f"{activate_script}"
        print(f"\n[*] Для активации окружения выполните: {activate_command}")
    else:  # Linux/MacOS
        activate_script = "venv/bin/activate"
        activate_command = f"source {activate_script}"
        print(f"\n[*] Для активации окружения выполните: {activate_command}")
    
    # 4. Создаем requirements.txt
    with open("requirements.txt", "w") as f:
        f.write("# Добавьте сюда ваши зависимости\n")
    print("[+] Файл requirements.txt создан.")
    
    # 5. Создаем базовый main.py
    with open("main.py", "w") as f:
        f.write('print("Hello from your new project!")\n')
    print("[+] Файл main.py создан.")
    
    # 6. Создаем README.md
    with open("README.md", "w") as f:
        f.write(f"# {project_name}\n\nОписание вашего проекта.\n")
    print("[+] Файл README.md создан.")
    
    print(f"\n🎉 Проект '{project_name}' успешно инициализирован!")
    print("Следующие шалы:")
    print(f"1. Активируйте окружение: {activate_command}")
    print("2. Установите зависимости: pip install -r requirements.txt")
    print("3. Начните кодить!")

if __name__ == "__main__":
    main()
