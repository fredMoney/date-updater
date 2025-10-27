import os, datetime
from time import sleep


def parseInput(user_in) -> list:
    if user_in == "exit":
        print("Program will now exit.")
        sleep(1)
        exit()

    episodes = list()
    if "-" in user_in:
        ep_limit = user_in.split("-")
        for i in range(int(ep_limit[0]), int(ep_limit[1]) + 1):
            episodes.append(str(i))
    elif "," in user_in:
        episodes = user_in.strip().split(",")
    else:
        episodes.append(user_in)

    return episodes


def modifyDatetime(paths):
    for path in paths:
        sleep(0.5)
        os.utime(path, (datetime.datetime.now().timestamp(), datetime.datetime.now().timestamp()))
        print("Episode " + path.split("\\")[-1] + " updated.", end="\n")
    

def listEpisodes(path):
    print("List of episodes:", end="\n")
    ep_list = sorted(os.scandir(path), key=lambda ep: ep.name)
    i = 1
    for ep in ep_list:
        sleep(0.1)
        print(f"{i:03}", ep.name, sep=". ")
        i = i + 1
    sleep(0.2)
    print("Pick episode(s): ")
    user_in = input()
    episodes = parseInput(user_in)
    paths = [ep_list[int(ep) - 1].path for ep in episodes]
    modifyDatetime(paths)


def changeDir(path):
    dir_list = [entry for entry in os.scandir(path) if entry.is_dir()]
    i = 1
    for dir in dir_list:
        sleep(0.1)
        print(f"{i:03}", dir.name, sep=". ")
        i = i + 1
    sleep(0.2)
    print("Choose dir: ")
    user_in = input()
    path = dir_list[int(user_in) - 1].path
    os.chdir(path)
    return path


def listOptions(path):
    print(
        "You are currently in " + path + ". Choose one of the following:",
        "1. List dir",
        "2. Change dir",
        "3. Move up dir",
        "4. List episodes",
        "5. Exit",
        sep="\n"
    )
    

def main():
    path = os.getcwd()
    print("Welcome!", end=" ")
    while True:
        listOptions(path)
        option = input()

        if option == "1":
            with os.scandir(path) as dir:
                for file in dir:
                    if not file.is_file():
                        sleep(0.2)
                        print(file.name, end="\n")
        elif option == "2":
            path = changeDir(path)
        elif option == "3":
            os.chdir("..")
            path = os.getcwd()
        elif option == "4":
            listEpisodes(path)
        elif option == "5":
            print("Program will now exit.")
            sleep(1)
            exit()
        else:
            print("Invalid option. Please consult the list.")
        sleep(1)

main()