import glob
import os
import sc2reader
from dotenv import load_dotenv
import datetime


def get_all_replays(replay_dir):
    glob_path = os.path.join(f"{replay_dir}", "*.SC2Replay")
    list_of_replays = glob.glob(glob_path)
    return list_of_replays


def get_most_recent_replay(list_of_replays=None, replay_path=None):
    if list_of_replays is None:
        list_of_replays = get_all_replays(replay_path)
    latest_file = max(list_of_replays, key=os.path.getctime)
    return latest_file


def convert_event_second_to_real_time(seconds):
    real_seconds = seconds / 1.4
    timestamp = ":".join(str(datetime.timedelta(seconds=real_seconds)).split(":")[1:3])
    if "." in timestamp:
        timestamp = timestamp.split(".")[0]
    return timestamp


def parse_replay(path_to_replay, target_player=None):
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
        actual_time = convert_event_second_to_real_time(event.second)
        if type(event) == sc2reader.events.tracker.PlayerStatsEvent:
            if target_player is not None:
                if target_player not in str(event.player):
                    continue
            oversupply_percent = ((event.food_made / event.food_used) * 100) - 100
            print(f"{actual_time} | Supply: {event.food_used} / {event.food_made} ({str(oversupply_percent)[:3]}% oversupplied) ")
        # else:
        #     print(f"type - {type(event)} | {event}")


def __main__():
    # Load environment variables from .env file
    load_dotenv()
    sc2_replay_path = os.getenv('sc2_replay_path')
    # reviewing_player = os.getenv('player')
    reviewing_player = None

    all_replay_list = get_all_replays(sc2_replay_path)
    active_replay = get_most_recent_replay(all_replay_list)

    parse_replay(active_replay, reviewing_player)
    # for replay in all_replay_list:
    #     parse_replay(replay)
    #     print('--------------------------------------')


__main__()
