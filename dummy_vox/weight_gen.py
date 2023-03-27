import numpy as np
import math
import pdb
import argparse
import time



def get_ratio(min_src, max_src, min_dst, max_dst):

    if min_dst < max_src:
        ratio = (max_src-min_dst) / (max_src-min_src)
    else:
        ratio = 0
    return ratio

def get_2D_space_idx(width, height, nb_cam):

    pix = np.ones((width*nb_cam, height), dtype='int')

    idx = 0
    for i in range(width*nb_cam):
        for j in range(height):
                pix[i,j] = idx 
                idx += 1

    return pix

def from_3D_to_2D(coor_3D, vox):

    coor_2D = []


    return coord_2D


def get_3D_space_idx(vox_l):

    vox = np.ones((vox_l, vox_l, vox_l), dtype='int')

    idx = 0
    for i in range(vox_l):
        for j in range(vox_l):
            for k in range(vox_l):
                vox[i,j,k] = idx 
                idx += 1

    return vox

''' 
This function creates a list of weights 
It ONLY works for width = height = vox_l
'''
def create_conn_list(nb_cam, width, height, vox_l, weight, delay):

    conn_list = []

    pix = get_2D_space_idx(width, height, nb_cam)
    # print(pix)
    vox = get_3D_space_idx(vox_l)
    # pdb.set_trace()

    for cam_id in range(nb_cam):

        pix_layer = pix[cam_id*width:(cam_id+1)*width,:]
        
        # print(f"\n\nFor cam #{1+cam_id}")
        # print(pix_layer)

        for layer in range(vox_l):
            if cam_id == 0:
                vox_layer = vox[layer, :, :]
            if cam_id == 1:
                vox_layer = np.fliplr(vox[:, layer, :])
            if cam_id == 2:
                vox_layer = np.fliplr(np.flipud(np.rot90(vox[:, :, layer])))
            # print(f"\nLayer {layer}:")
            # print(vox_layer)

            for i in range(vox_l):
                for j in range(vox_l):
                    conn_list.append((pix_layer[i,j], vox_layer[i,j], weight, delay))

    return conn_list

