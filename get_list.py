import pandas as pd
import numpy as np

if __name__ == "__main__":
    pop_list =np.load("Pop.npy")
    print("pop",pop_list.shape[0])
    pop_list =np.load("Folk.npy")
    print("Folk.npy",pop_list.shape[0])
    pop_list =np.load("Hip-Hop.npy")
    print("Hip-Hop.npy",pop_list.shape[0])
    pop_list =np.load("Instrumental.npy")
    print("Instrumental.npy",pop_list.shape[0])
    pop_list =np.load("International.npy")
    print("International.npy",pop_list.shape[0])
    pop_list =np.load("Jazz.npy")
    print("Jazz.npy",pop_list.shape[0])
    pop_list =np.load("Rock.npy")
    print("Rock.npy",pop_list.shape[0])
    pop_list =np.load("Jazz.npy")
    print(".")

