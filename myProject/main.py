# * - все классы

from classes.Manager import *

# myUser = User(12,"Ilya","Vybornov","19.11.1989","Мужской","qweqwe","1234")
# print(myUser.last_name)
# myUser.update_last_name("Ivanov")
# print(myUser.last_name)

import json
def reg():
    store_list_read = open("store/store.json", "r",encoding="utf-8")
    store_list = json.loads(store_list_read.read())
    store_list_read.close()
    print(store_list)
    regs = Registration()
    regs.create_user(store_list)
    store_list = json.dumps(store_list, ensure_ascii=False)
    store_list_write = open("store/store.json","w",encoding="utf-8")
    store_list_write.write(store_list)
    store_list_write.close()
reg()
   