import os, datetime
from time import sleep
from pathlib import Path


DELAY_SHORT = 0.1
DELAY_LONG = 0.4


def parseInput(user_in) -> list:
    if user_in == "exit":
        print("Program will now exit.")
        sleep(DELAY_LONG)
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
        sleep(DELAY_SHORT)
        os.utime(path, (datetime.datetime.now().timestamp(), datetime.datetime.now().timestamp()))
        print("Episode " + path.split("\\")[-1] + " updated.", end="\n")
    

def listEpisodes(path):
    print("List of episodes:", end="\n")
    ep_list = sorted(os.scandir(path), key=lambda ep: ep.name)
    i = 1
    for ep in ep_list:
        sleep(DELAY_SHORT)
        print(f"{i:03}", ep.name, sep=". ")
        i = i + 1
    sleep(DELAY_LONG)
    print("Pick episode(s): ")
    user_in = input()
    episodes = parseInput(user_in)
    paths = [ep_list[int(ep) - 1].path for ep in episodes]
    modifyDatetime(paths)


def changeDir(path):
    dir_list = [entry for entry in os.scandir(path) if entry.is_dir()]
    i = 1
    for dir in dir_list:
        sleep(DELAY_SHORT)
        print(f"{i:03}", dir.name, sep=". ")
        i = i + 1
    sleep(DELAY_LONG)
    print("Choose dir: ")
    user_in = input()
    path = dir_list[int(user_in) - 1].path
    os.chdir(path)
    path = os.getcwd()
    print(path)


def listHelp():
    print(
        "Usage:",
        "Navigate to the folder the series is in on disk. List the episodes. Pick an episode(s) to update the date.",
        "To specify multiple episodes, delimitate them by commas (eg. 2, 3, 4); to specify a range, use hyphen",
        "(eg. 2-6). Type \"exit\" to exit.",
        sep="\n"
    )


def listDirs(path):
    with os.scandir(path) as dir:
        for file in dir:
            if not file.is_file():
                sleep(DELAY_SHORT)
                print(file.name, end="\n")


def listDirOptions(path):
    print(
        "You are currently in " + path + ". Paste the absolute path to dir or choose one of the following:",
        "1. List dirs in current path",
        "2. Move to dir in current path",
        "3. Move up dir",
        "4. Go back",
        sep="\n"
    )


def navigateDirs(path):
    while True:
        sleep(DELAY_LONG)
        listDirOptions(path)
        option = input()

        if option == "1":
            listDirs(path)
        elif option == "2":
            changeDir(path)
        elif option == "3":
            os.chdir("..")
            path = os.getcwd()
        elif option == "4":
            break
        else:
            pathTo = Path(option)
            if pathTo.is_absolute():
                os.chdir(option)
                path = os.getcwd()
            else:
                print("Path is invalid! Try again...")


def listOptions(path):
    print(
        "You are currently in " + path + ". Choose one of the following:",
        "1. Process episode(s)",
        "2. Navigate to dir",
        "3. List help",
        "4. Exit",
        sep="\n"
    )


def main():
    path = os.getcwd()
    print("Welcome!", end=" ")
    while True:
        listOptions(path)
        option = input()

        if option == "1":
            listEpisodes(path)
        elif option == "2":
            navigateDirs(path)
        elif option == "3":
            listHelp()
        elif option == "4":
            print("Goodbye!")
            sleep(1)
            exit()
        else:
            print("Invalid option. Please consult option 3.")
        sleep(DELAY_LONG)

main()