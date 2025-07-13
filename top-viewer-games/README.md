# Top Viewer Games

This mini project displays the current top channels and games on Twitch.
It uses the public Twitch API and requires your own client credentials.

## Setup

1. Create a Twitch application at <https://dev.twitch.tv/console/apps>.
2. Note the *Client ID* and *Client Secret*.
3. Set the environment variables before running:

```bash
export TWITCH_CLIENT_ID=<your client id>
export TWITCH_CLIENT_SECRET=<your client secret>
```

Run the viewer script from the project root:

```bash
python top-viewer-games/viewer.py
```

The script prints the most viewed games and live channels.
