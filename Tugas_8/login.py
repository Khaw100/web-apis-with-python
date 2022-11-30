
user_data = {}


def validation(user, password):
    if user_data[user] == password:
        return True
    else:
        return False

    
