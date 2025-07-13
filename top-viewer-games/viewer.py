from __future__ import annotations

from gpt_fusion.twitch import TwitchClient


def main() -> None:
    client = TwitchClient()
    games = client.get_top_games()
    streams = client.get_top_streams()
    print("Top Games:")
    for game in games:
        print(f"{game['name']} - {game['id']}")
    print("\nTop Streams:")
    for stream in streams:
        print(
            f"{stream['user_name']} playing {stream['game_name']} "
            f"with {stream['viewer_count']} viewers"
        )


if __name__ == "__main__":
    main()
