import os
import glob

sc2_replay_path = '/ext4/sc2-replays'


def get_all_replays(replay_dir):
    glob_path = os.path.join(f"{replay_dir}", "*.SC2Replay")
    list_of_replays = glob.glob(glob_path)
    return list_of_replays


def get_most_recent_replay(list_of_replays):
    True


def __main__():
    True


__main__()