import getpass
from models import register, login

# Основная функция
def main():
    while True:
        print("1. Регистрация")
        print("2. Вход в систему")
        print("3. Выход")
        choice = input("Введите ваш выбор: ")
        if choice == "1":
            username = input("Введите имя пользователя: ")
            email = input("Введите электронную почту: ")
            password = getpass.getpass("Введите пароль: ")
            register(username, email, password)
        elif choice == "2":
            username = input("Введите имя пользователя: ")
            password = getpass.getpass("Введите пароль: ")
            login(username, password)
        elif choice == "3":
            break
        else:
            print("Неправильный выбор.")
# Запускаем основную функцию
if __name__ == "__main__":
    main()
