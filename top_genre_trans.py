import pandas as pd


def genre_id2top_id(input_id):
    top = pd.read_csv('fma_metadata/genres.csv')
    g_id = top.genre_id
    top_id = top.top_level
    check = -1
    for work in range(len(g_id)):
        if input_id == g_id[work]:
            check = top_id[work]

    return check


def genre_id2genre_title(input_id):
    top = pd.read_csv('fma_metadata/genres.csv')
    # target_id = top.values[0][0]
    # target_title = top.values[0][3]
    check = str(-1)
    for work in range(len(top.genre_id)):
        if input_id == top.values[work][0]:
            check = top.values[work][3]
    return check


if __name__ == "__main__":
    tracks = pd.read_csv('fma_metadata/raw_tracks.csv')
    genre_table = pd.read_csv('fma_metadata/genres.csv')
    # g_id = genre_table.genre_id
    # top_id = genre_table.top_level
    track_id = 30
    # for track_id in range(tracks.shape[0]):

    genre_id = int(tracks.track_genres[track_id].split('\'')[3])
    genre_id_top = genre_id2top_id(genre_id)
    genre_title = genre_id2genre_title(genre_id)
    genre_title_top = genre_id2genre_title(genre_id_top)

    print(".")
