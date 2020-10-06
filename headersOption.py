import time
from configUtils import Config


def main():
    print(111)
    config = Config()
    time.sleep(3)
    cookie = config.get_value("Cookie")
    print(cookie)
    time.sleep(10)


if __name__ == '__main__':
    main()
