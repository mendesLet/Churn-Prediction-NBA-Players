import requests
import pandas as pd

alltit = ["GM", "WGM", "IM", "WIM", "FM", "WFM", "NM", "WNM", "CM", "WCM"]
for tit in alltit:
    url1 = f"https://api.chess.com/pub/titled/{tit}"
    paisplayer = requests.get(url1)
    paisplayer = paisplayer.json()

    if "players" in paisplayer:
        players_data = paisplayer["players"]
        df = pd.DataFrame(players_data)

        csv_file = f"chess_players_{tit}.csv"
        df.to_csv(csv_file, index=False)
