import hashlib
from database import connect_to_db

# Функция регистрации
def register(username, email, password):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    # Проверяем, существует ли уже пользователь с таким именем
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    if cursor.fetchone():
        print("Пользователь с таким именем уже существует.")
        return
    # Хешируем пароль
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Создаем учетную запись
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    print("Учетная запись создана успешно!")
# Функция входа в систему
def login(username, password):
    conn = connect_to_db()
    if conn is None:
        return
    cursor = conn.cursor()
    # Проверяем, существует ли пользователь с таким именем
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()
    if not user_data:
        print("Пользователь с таким именем не существует.")
        return
    # Хешируем пароль
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Проверяем, соответствует ли пароль хранящемуся в учетной записи
    if hashed_password == user_data[2]:
        print("Вход в систему успешен!")
    else:
        print("Неправильный пароль.")
    cursor.close()
    conn.close()