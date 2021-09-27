import os


def config_vars():
    if not os.environ.get('token') or not os.environ.get('app_name')\
            or not os.environ.get('mongo_link'):
        from dotenv import load_dotenv
        load_dotenv()
