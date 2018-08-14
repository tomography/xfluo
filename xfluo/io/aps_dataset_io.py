#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (c) 2018, UChicago Argonne, LLC. All rights reserved.

Copyright 2016. UChicago Argonne, LLC. This software was produced
under U.S. Government contract DE-AC02-06CH11357 for Argonne National
Laboratory (ANL), which is operated by UChicago Argonne, LLC for the
U.S. Department of Energy. The U.S. Government has rights to use,
reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR
UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR
ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is
modified to produce derivative works, such modified software should
be clearly marked, so as not to confuse it with the version available
from ANL.

Additionally, redistribution and use in source and binary forms, with
or without modification, are permitted provided that the following
conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the
      distribution.

    * Neither the name of UChicago Argonne, LLC, Argonne National
      Laboratory, ANL, the U.S. Government, nor the names of its
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago
Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''


import os
import sys
import json
import argparse
import collections

import h5py
import tomopy
import tomopy.util.dtype as dtype
import dxchange

import numpy as np

def restricted_float(x):

    x = float(x)
    if x < 0.0 or x >= 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x,))
    return x

def find_index(a_list, element):
    try:
        return a_list.tolist().index(element)
    except ValueError:
        return None

def read_elements(h5fname):
    return(dxchange.read_hdf5(h5fname, "MAPS/channel_names"))

def read_projection(fname, element, theta_index):

    projections = dxchange.read_hdf5(fname, "MAPS/XRF_roi")
    theta = dxchange.read_hdf5(fname, "MAPS/extra_pvs_as_csv")[theta_index].split(",")[1]
    elements = read_elements(fname)

    return theta, projections[find_index(elements, element)]

def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="Directory containing multiple datasets or file name of a single dataset: /data/ or /data/sample.h5")
    parser.add_argument("--start", nargs='?', type=float, default=0.0, help="Angle first projection (default 0.0)")
    parser.add_argument("--end", nargs='?', type=float, default=180.0, help="Angle last projection (default 180.0)")
    parser.add_argument("--element", nargs='?', type=str, default="Si", help="Select the element to recontruct (default Si)")

    args = parser.parse_args()

    # Set path to the micro-CT data to reconstruct.
    fname = args.fname
    angle_start = float(args.start)
    angle_end = float(args.end)
    element = args.element

    if os.path.isfile(fname):    

        elements = read_elements(fname)
        for i, e in enumerate(elements):
            print ('%d:  %s' % (i, e))
        
        proj, theta = read_projection(fname, element, 657)
        print ("theta:", theta)
        print (proj.shape)

    elif os.path.isdir(fname):
        # Add a trailing slash if missing
        top = os.path.join(fname, '')

        h5_file_list = list(filter(lambda x: x.endswith(('.h5', '.hdf')), os.listdir(top)))

        for i, fname in enumerate(h5_file_list):
            theta, proj = read_projection(top+fname, element, 657)
            print(i, theta, fname)

    else:
        print("Directory or File Name does not exist: ", fname)

if __name__ == "__main__":
    main(sys.argv[1:])

