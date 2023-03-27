import numpy as np
import math
import pyNN.spiNNaker as p
import pdb
import socket
from struct import pack
import matplotlib.pyplot as plt
import argparse
import time


def parse_args():

    parser = argparse.ArgumentParser(description='SpiNNaker-SPIF Simulation')

    # SpiNNaker Simulation Parameters
    parser.add_argument('-w', '--width', type=int, help="# pixels on x dimension", default=1)  
    parser.add_argument('-c', '--cam', type=int, help="Cam ID # (0,1,2)", default=0) 
    parser.add_argument('-x', '--x', type=int, help="x", default=-1) 
    parser.add_argument('-y', '--y', type=int, help="y", default=-1) 
    parser.add_argument('-d', '--ip', type= str, help="IP address", default="172.16.223.2")
    parser.add_argument('-p', '--port', type=int, help="port", default=3333)  
    parser.add_argument('-z', '--sleep', type=float, help="sleep", default=0.01)    

    return parser.parse_args()
   

if __name__ == '__main__':


    args = parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    NO_TIMESTAMP = 0x80000000
    # print(np_spikes.shape)

    while True:
        if args.x >=0 and args.y >=0:
            data = b""      
            offset = args.cam*(args.width**2)      
            x = args.x
            y = args.y
            neuron_id = (y*args.width) + x + offset
            print(f"Sending ({x},{y}), i.e. n_id: {neuron_id}")
            packed = NO_TIMESTAMP + neuron_id            
            data += pack("<I", packed)
            sock.sendto(data, (args.ip, args.port))
            time.sleep(args.sleep)
        else:
            pass