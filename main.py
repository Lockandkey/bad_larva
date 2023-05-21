import glob
import os
import sc2reader

sc2_replay_path = '/ext4/sc2-replays'


def get_all_replays(replay_dir):
    glob_path = os.path.join(f"{replay_dir}", "*.SC2Replay")
    list_of_replays = glob.glob(glob_path)
    return list_of_replays


def get_most_recent_replay(list_of_replays=None):
    if list_of_replays is None:
        list_of_replays = get_all_replays(sc2_replay_path)
    latest_file = max(list_of_replays, key=os.path.getctime)
    return latest_file


def __main__():
    True


__main__()
