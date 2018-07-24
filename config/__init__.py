import os

class Config(object):
    db_path = 'localhost:27017'
    db_name = 'ronfe'
    local_path = os.path.dirname(os.path.realpath(__file__))
    local_path = local_path.split("/")
    local_path = local_path[:-1]
    local_path = "/".join(local_path)

    gamers = [
        {
           "name": "苏嘉锐",
           "shortname": "JR",
           "joinedTeam": None
        },
        {
           "name": "王国杰",
           "shortname": "GJ",
           "joinedTeam": None
        },
        {
           "name": "史晓峰",
           "shortname": "XF",
           "joinedTeam": None
        },
        {
           "name": "宿玲玲",
           "shortname": "LL",
           "joinedTeam": None
        },
        {
           "name": "陈琪湉",
           "shortname": "QT",
           "joinedTeam": None
        },
        {
           "name": "徐小晴",
           "shortname": "XQ",
           "joinedTeam": None
        },
        {
           "name": "陈乐琪",
           "shortname": "LQ",
           "joinedTeam": None
        },
        {
           "name": "李雨韵",
           "shortname": "YY",
           "joinedTeam": None
        },
        {
           "name": "李夏依",
           "shortname": "XY",
           "joinedTeam": None
        },
        {
           "name": "边靖媛",
           "shortname": "JY",
           "joinedTeam": None
        },
        {
            "name": "芮文豪",
            "shortname": "WH",
            "joinedTeam": None
        }
    ]
