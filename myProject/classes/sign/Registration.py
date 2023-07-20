class Registration():
    def create_user(self, users_list):
        users_list.append({
        "first_name" : input("введите имя: "),
        "last_name" : input("введите фамилию: "),
        "birthday" : input("Дата рождения: "),
        "gender" : input("введите пол: "),
        "login" : input("введите логин: "),
        "password" : input("введите пароль: "),
        },)
        return users_list