import pandas as pd

if __name__ == '__main__':
    tracks = pd.read_csv('fma_metadata/raw_tracks.csv')
    tracks.shape
    kk = tracks.track_id
    id_list = [-1]
    genre_list = ['start']
    try:

        for track_id in range(tracks.shape[0]):
            if track_id % 10 == 0:
                print(".", end='')
            # genre_list = tracks.track_genres[track_id].split('\'')
            try:
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
                print("inner ERROR :", e)
        print("*")
        print(id_list)
        print(genre_list)

    except Exception as e:
        print("outer ERROR", e)

    print(".")
