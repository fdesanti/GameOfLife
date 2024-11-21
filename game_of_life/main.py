"""Script to play the Game of Life"""

import random
import argparse
import numpy as np
from game_of_life import GameofLife

def main():
    pars = argparse.ArgumentParser()
    pars.add_argument("--N", type=int, default=10, help="Size of the grid NxM. (Default: 10)")
    pars.add_argument("--M", default=None, help="Size of the grid NxM. If None then M=N. (Default: None)")
    pars.add_argument("--boundary", type=str, default="wall", help="Boundary condition. (Default: wall)")
    pars.add_argument("--seed", default=None, help="Random seed for reproducibility. (Default: None)")
    
    args = pars.parse_args()

    if args.seed:
        seed = int(args.seed)
        random.seed(seed)
        np.random.seed(seed)
    
    N        = args.N
    M        = int(args.M) if args.M is not None else args.M
    boundary = args.boundary

    #setup the game instance and play
    Game = GameofLife(N=N, M=M, boundary=boundary)
    Game.play()


if __name__=='__main__':
    main()