import re

def validate_password(password_dict):
    count = 0
    for i in password_dict["password"]:
        if i == password_dict["letter"]:
            count = count + 1
    return password_dict["max"] >= count >= password_dict["min"]

def validate_password_v2(password_dict):
    password = password_dict["password"]
    min_index = password_dict["min"]
    max_index = password_dict["max"]
    letter_match = password_dict["letter"] 
    if (password[min_index-1] == letter_match
        and password[max_index-1] != letter_match):
        return True
    elif (password[max_index-1] == letter_match
          and password[min_index-1] != letter_match):
        return True
    else:
        return False

if __name__ == "__main__":
    passwords = []
    with open('day_2/input.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            parts = re.findall('([0-9]+)\-([0-9]+)\ ([a-z]):\ ([a-z]+)', line)[0]

            passwords.append({
                "min": int(parts[0]),
                "max": int(parts[1]),
                "letter": parts[2],
                "password": parts[3]
            })

    policy_v1_valid_passwords = []
    policy_v2_valid_passwords = []
    for i in passwords:
        if validate_password(i):
            policy_v1_valid_passwords.append(i)
        if validate_password_v2(i):
            policy_v2_valid_passwords.append(i)

    print(f"Total passwords: {len(passwords)}")
    print(f"Total [policy 1] valid passwords: {len(policy_v1_valid_passwords)}")
    print(f"Total [policy 2] valid passwords: {len(policy_v2_valid_passwords)}")
