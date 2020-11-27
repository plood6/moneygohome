import money


def send():
    send_money = int(input('这月工资发了多少，看看一共有多少存款：'))
    global select_money
    select_money = money.saved_money + send_money
