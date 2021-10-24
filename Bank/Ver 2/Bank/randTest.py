from random import randint, choice

def rand_account(user_list, account_list = ['savings','checking']):
    rand_choice = [choice(user_list), randint(50,100000),choice(account_list)]

    return rand_choice

list_user_names = ['Hank','Tyler','Frank','Sylivia','Randy','Kevin','Connor','Hayden','Skylar','Stella','Rob','Sally']
