import pandas as pd
import numpy as np


def genre_id2top_id(input_id, top):
    g_id = top.genre_id
    top_id = top.top_level
    check = -1
    for work in range(len(g_id)):
        if input_id == g_id[work]:
            check = top_id[work]
    return check


def genre_id2genre_title(input_id, top):
    # target_id = top.values[0][0]
    # target_title = top.values[0][3]
    check = str(-1)
    for work in range(len(top.genre_id)):
        if input_id == top.values[work][0]:
            check = top.values[work][3]
    return check


if __name__ == '__main__':
    tracks = pd.read_csv('fma_metadata/raw_tracks.csv')
    genres = pd.read_csv('fma_metadata/genres.csv')

    target_id_list = [15, 38, 17, 21, 1235, 2, 4, 10, 12]
    try:

        for target_genre_id in target_id_list:
            try:
                target_genre_id_top = genre_id2top_id(target_genre_id, genres)

                print("~\n~\n~ ~ deal with\n~\n~", genre_id2genre_title(target_genre_id_top, genres))

                target_genre_tracks = []
                no_genre_cnt = 0
                try:

                    for track_id in range(tracks.shape[0]):
                        try:
                            # test if without genre
                            test = tracks.track_genres[track_id]
                            if type(test) is float:
                                print("track_id:%d" % track_id, "no genre")
                                no_genre_cnt += 1
                                continue

                            genre_id = int(tracks.track_genres[track_id].split('\'')[3])
                            genre_id_top = genre_id2top_id(genre_id, genres)

                            if genre_id_top == target_genre_id_top:
                                print(genre_id2genre_title(genre_id, genres), end=' -> ')
                                print(genre_id2genre_title(genre_id_top, genres))
                                target_genre_tracks.append(track_id)

                        except Exception as e:
                            print("id:%d" % track_id, "inner ERROR :", e)
                    print("*")
                    print(target_genre_tracks)
                    string = genre_id2genre_title(target_genre_id_top, genres) + ".npy"
                    np.save(string, target_genre_tracks)

                    print("count of no genre's file", no_genre_cnt)

                except Exception as e:
                    print("outer ERROR", e)
            except Exception:
                print("a", Exception)
    except Exception:
        print("genre_id ERROR :", Exception)
