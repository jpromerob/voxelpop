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
    parser.add_argument('-nc','--nb-cam', type=int, help="Number of cameras", default=3)
    parser.add_argument('-w', '--width', type=int, help="# pixels on x dimension", default=1)
    parser.add_argument('-x', '--x', type=int, help="x", default=0) 
    parser.add_argument('-y', '--y', type=int, help="y", default=0)
    parser.add_argument('-z', '--z', type=int, help="z", default=0) 
    parser.add_argument('-d', '--ip', type= str, help="IP address", default="172.16.223.2")
    parser.add_argument('-p', '--port', type=int, help="port", default=3333)  
    parser.add_argument('-t', '--sleep', type=float, help="sleep", default=0.01)    

    return parser.parse_args()
   

if __name__ == '__main__':


    args = parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    NO_TIMESTAMP = 0x80000000
    # print(np_spikes.shape)

    x = args.x
    y = args.y
    z = args.z
    w = args.width

    while True:
        if x < w and y < w and z < w:
            data = b""      
            for cam_id in range(args.nb_cam):
                offset = cam_id*(args.width**2) 
                if cam_id == 0: # fron view
                    rel_x = x 
                    rel_y = y
                if cam_id == 1: # top view
                    rel_x = w-x-1 
                    rel_y = z
                if cam_id == 2: # lateral view (left --> right)
                    rel_x = w-z-1 
                    rel_y = y
                neuron_id = (rel_y*args.width) + rel_x + offset

                print(f"Cam #{cam_id+1} sending ({rel_x},{rel_y}), i.e. n_id: {neuron_id}")
                packed = NO_TIMESTAMP + neuron_id            
                data += pack("<I", packed)
            sock.sendto(data, (args.ip, args.port))
            time.sleep(args.sleep)
        else:
            pass