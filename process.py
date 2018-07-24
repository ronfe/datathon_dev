from pymongo import MongoClient
import config

cfg = config.Config()


# Data init
def init_data():
    with MongoClient(cfg.db_path) as conn:
        db = conn[cfg.db_name]

        # 1. add users
        col = db['users']
        users = cfg.gamers

        for user in users:
            col.insert_one(user)


if __name__ == '__main__':
    init_data()
