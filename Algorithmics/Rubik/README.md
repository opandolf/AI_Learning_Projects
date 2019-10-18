# Rubik

Rubik is a school project made with Jean Baptiste Austry (https://github.com/jb255)  
To store the cube and simulate rotations, positions and orientations of corners and edges are represented by array of 8 and 12 respectively. Those 4 lists are shifted in when a face is rotated.

# Usage

usage: rubik.py [-h] [-t] [-g] [-d] [file [file ...]]

positional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file  
  
optional arguments:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help       show this help message and exit  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-t, --timer      print total execution time  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-g, --generator  use integred generator  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-d, --detail     detail solution for humain comprehension  
