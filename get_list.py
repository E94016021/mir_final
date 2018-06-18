import pandas as pd
import numpy as np

if __name__ == "__main__":

    names = ["Blues.npy", "Classical.npy", "Country.npy", "Electronic.npy",
             "ex_chip.npy", "Experimental.npy", "Folk.npy", "Hip-Hop.npy",
             "Instrumental.npy", "International.npy", "Jazz.npy",
             "Pop.npy", "Rock.npy", "Soul-RnB.npy", "Spoken.npy", "old_time.npy", "Easy Listening.npy"]

    for name in names:
        elec_list = np.load(name)
        print(name.split(".npy")[0], "cnt =", elec_list.shape[0])

    print(".")
