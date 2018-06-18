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


def simple():
    # min = 2329 (Jazz)
    # genres = [15, 38, 17, 21, 1235, 2, 4, 10, 12]
    names = ["ex_chip.npy", "Experimental.npy", "Folk.npy", "Hip-Hop.npy", "Instrumental.npy", "International.npy",
             "Jazz.npy", "Pop.npy", "Rock.npy"]
    # out = ["Blues.npy", "Classical.npy", "Country.npy",
    #        "Electronic_fake.npy", "Soul-RnB.npy", "Spoken.npy", "old_time.npy", "Easy Listening.npy"]

    g = 0

    train_set_X = np.asarray([-1])
    train_set_Y = np.asarray([-1])
    v_set_X = np.asarray([-1])
    v_set_Y = np.asarray([-1])
    test_set_X = np.asarray([-1])
    test_set_Y = np.asarray([-1])

    for name in names:
        d = np.load(name)
        np.random.shuffle(d)
        l_shuffle = d[:1000]
        l_labels = np.asarray([g] * 1000, dtype=np.int32)

        train_v = int(0.6 * l_shuffle.size)
        v_test = int(0.8 * l_shuffle.size)

        train_set_X = np.hstack((train_set_X, l_shuffle[:train_v]))
        train_set_Y = np.hstack((train_set_Y, l_labels[:train_v]))
        v_set_X = np.hstack((v_set_X, l_shuffle[train_v:v_test]))
        v_set_Y = np.hstack((v_set_Y, l_labels[train_v:v_test]))
        test_set_X = np.hstack((test_set_X, l_shuffle[v_test:]))
        test_set_Y = np.hstack((test_set_Y, l_labels[v_test:]))

        g += 1

    np.save("train_set_sim1000_trackid.npy", train_set_X[1:])
    np.save("train_set_sim1000_genre_id.npy", train_set_Y[1:])
    np.save("v_set_sim1000_trackid.npy", v_set_X[1:])
    np.save("v_set_sim1000_genre_id.npy", v_set_Y[1:])
    np.save("test_set_sim1000_trackid.npy", test_set_X[1:])
    np.save("test_set_sim1000_genre_id.npy", test_set_Y[1:])

    print(".")


def medium():
    # min = 2329 (Jazz)
    # genres = [15, 38, 17, 21, 1235, 2, 4, 10, 12]
    names = ["ex_chip.npy", "Experimental.npy", "Folk.npy", "Hip-Hop.npy", "Instrumental.npy", "International.npy",
             "Jazz.npy", "Pop.npy", "Rock.npy"]
    out = ["Blues.npy", "Classical.npy", "Country.npy", "Soul-RnB.npy", "Spoken.npy"]
    # dun =["old_time.npy", "Easy Listening.npy"]
    # namess =names.extend(out)

    names.extend(out)

    g = 0

    train_set_X = np.asarray([-1])
    train_set_Y = np.asarray([-1])
    v_set_X = np.asarray([-1])
    v_set_Y = np.asarray([-1])
    test_set_X = np.asarray([-1])
    test_set_Y = np.asarray([-1])

    for name in names:
        d = np.load(name)
        np.random.shuffle(d)
        lenz = d.size
        if lenz > 1000:
            lenz = 1000
        l_shuffle = d[:lenz]
        l_labels = np.asarray([g] * lenz, dtype=np.int32)

        train_v = int(0.6 * l_shuffle.size)
        v_test = int(0.8 * l_shuffle.size)

        train_set_X = np.hstack((train_set_X, l_shuffle[:train_v]))
        train_set_Y = np.hstack((train_set_Y, l_labels[:train_v]))
        v_set_X = np.hstack((v_set_X, l_shuffle[train_v:v_test]))
        v_set_Y = np.hstack((v_set_Y, l_labels[train_v:v_test]))
        test_set_X = np.hstack((test_set_X, l_shuffle[v_test:]))
        test_set_Y = np.hstack((test_set_Y, l_labels[v_test:]))

        g += 1

    np.save("train_set_med_trackid.npy", train_set_X[1:])
    np.save("train_set_med_genre_id.npy", train_set_Y[1:])
    np.save("v_set_med_trackid.npy", v_set_X[1:])
    np.save("v_set_med_genre_id.npy", v_set_Y[1:])
    np.save("test_set_med_trackid.npy", test_set_X[1:])
    np.save("test_set_med_genre_id.npy", test_set_Y[1:])

    print(".")


def medium():
    # min = 2329 (Jazz)
    # genres = [15, 38, 17, 21, 1235, 2, 4, 10, 12]
    names = ["ex_chip.npy", "Experimental.npy", "Folk.npy", "Hip-Hop.npy", "Instrumental.npy", "International.npy",
             "Jazz.npy", "Pop.npy", "Rock.npy"]
    out = ["Blues.npy", "Classical.npy", "Country.npy", "Soul-RnB.npy", "Spoken.npy"]
    # dun =["old_time.npy", "Easy Listening.npy"]
    # namess =names.extend(out)

    names.extend(out)

    g = 0

    train_set_X = np.asarray([-1])
    train_set_Y = np.asarray([-1])
    v_set_X = np.asarray([-1])
    v_set_Y = np.asarray([-1])
    test_set_X = np.asarray([-1])
    test_set_Y = np.asarray([-1])

    for name in names:
        d = np.load(name)
        np.random.shuffle(d)
        lenz = d.size
        l_shuffle = d[:lenz]
        l_labels = np.asarray([g] * lenz, dtype=np.int32)

        train_v = int(0.6 * l_shuffle.size)
        v_test = int(0.8 * l_shuffle.size)

        train_set_X = np.hstack((train_set_X, l_shuffle[:train_v]))
        train_set_Y = np.hstack((train_set_Y, l_labels[:train_v]))
        v_set_X = np.hstack((v_set_X, l_shuffle[train_v:v_test]))
        v_set_Y = np.hstack((v_set_Y, l_labels[train_v:v_test]))
        test_set_X = np.hstack((test_set_X, l_shuffle[v_test:]))
        test_set_Y = np.hstack((test_set_Y, l_labels[v_test:]))

        g += 1

    np.save("train_set_hard_trackid.npy", train_set_X[1:])
    np.save("train_set_hard_genre_id.npy", train_set_Y[1:])
    np.save("v_set_hard_trackid.npy", v_set_X[1:])
    np.save("v_set_hard_genre_id.npy", v_set_Y[1:])
    np.save("test_set_hard_trackid.npy", test_set_X[1:])
    np.save("test_set_hard_genre_id.npy", test_set_Y[1:])

    print(".")


# simple()
medium()
# a = np.load("train_set_med_trackid.npy")
# b = np.load("train_set_med_genre_id.npy")
# c = np.load("v_set_med_trackid.npy")
# d = np.load("v_set_med_genre_id.npy")
# e = np.load("test_set_med_trackid.npy")
# f = np.load("test_set_med_genre_id.npy")

a = np.load("train_set_hard_trackid.npy")
b = np.load("train_set_hard_genre_id.npy")
c = np.load("v_set_hard_trackid.npy")
d = np.load("v_set_hard_genre_id.npy")
e = np.load("test_set_hard_trackid.npy")
f = np.load("test_set_hard_genre_id.npy")

print(".")
