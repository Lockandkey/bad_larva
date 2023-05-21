import glob
import os
import sc2reader
from dotenv import load_dotenv


def get_all_replays(replay_dir):
    glob_path = os.path.join(f"{replay_dir}", "*.SC2Replay")
    list_of_replays = glob.glob(glob_path)
    return list_of_replays


def get_most_recent_replay(list_of_replays=None, replay_path=None):
    if list_of_replays is None:
        list_of_replays = get_all_replays(replay_path)
    latest_file = max(list_of_replays, key=os.path.getctime)
    return latest_file


def parse_replay(path_to_replay):
    # Parse the replay file
    replay = sc2reader.load_replay(path_to_replay, load_map=True)

    # Accessing replay information
    print("Replay version:", replay.release_string)
    print(f"Category: {replay.category}")
    print("Map name:", replay.map_name)
    print(f"{replay.real_type} Game lasted {replay.game_length}:", )

    # Iterate through players
    for player in replay.players:
        print(f"Player: {player.name}, {player.pick_race}")

    for event in replay.events:
        if type(event) == sc2reader.events.tracker.PlayerStatsEvent:
            print(f"{event.} | {event.player} Supply: {event.food_used} / {event.food_made}")
        # else:
        #     print(f"type - {type(event)} | {event}")



def __main__():
    # Load environment variables from .env file
    load_dotenv()
    sc2_replay_path = os.getenv('sc2_replay_path')

    all_replay_list = get_all_replays(sc2_replay_path)
    active_replay = get_most_recent_replay(all_replay_list)

    parse_replay(active_replay)
    # for replay in all_replay_list:
    #     parse_replay(replay)
    #     print('--------------------------------------')


__main__()
