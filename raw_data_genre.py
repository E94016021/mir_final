import pandas as pd
import numpy as np


def genre2top(input_id):
    top = pd.read_csv('fma_metadata/genres.csv')
    g_id = top.genre_id
    top_id = top.top_level
    for work in range(len(g_id)):
        if input_id == g_id[work]:
            return top_id[work]
        else:
            return [-1]


if __name__ == '__main__':
    tracks = pd.read_csv('fma_metadata/raw_tracks.csv')
    tracks.shape
    kk = tracks.track_id
    id_list = [-1]
    genre_list = ['start']
    no_genre = 0
    try:

        for track_id in range(tracks.shape[0]):
            # if track_id % 10 == 0:
            #     print(".", end='')
            # genre_list = tracks.track_genres[track_id].split('\'')
            # track_id = 106140
            try:

                test = tracks.track_genres[track_id]
                if type(test) is float:
                    print("track_id:%d" % track_id, "no genre")
                    no_genre += 1
                    continue

                # print(".")

                genre_id = int(tracks.track_genres[track_id].split('\'')[3])
                genre_title = tracks.track_genres[track_id].split('\'')[7]
                # print("g_id = %4d" % genre_id, " : ", genre_title)
                new = 0
                for id_num in range(len(id_list)):
                    if genre_id == id_list[id_num]:
                        new = 1
                    else:
                        continue
                if new == 0:
                    id_list.append(genre_id)
                    genre_list.append(genre_title)
            except Exception as e:
                print("id:%d" % track_id, "inner ERROR :", e)
        print("*")
        print(id_list)
        print(genre_list)

        pair = list(zip(id_list, genre_list))
        pair.sort(key=lambda x: x[0], )
        res = pair[1:]
        np.save("res.npy", res)
        np.save("pair.npy", pair)
        print(pair)

        print("count of no genre's file", no_genre)

    except Exception as e:
        print("outer ERROR", e)

    print(".")
