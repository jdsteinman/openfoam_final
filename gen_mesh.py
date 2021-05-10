import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from datetime import date

# Parameters #############################################
r = 1.0
R = 2.0
H = 4.0
res = 1.0

##########################################################

file_name = "blockMeshDict" 
f = open(file_name, "w+")
np.set_printoptions(precision=8)

## Comments
f.write("// Mesh generated on {}\n\n".format(date.today()))
f.write("// r  (inner)  = {}\n".format(r))
f.write("// R  (outer) = {}\n".format(R))
f.write("// H  (height) = {}\n".format(H))
f.write("// res = {}\n".format(res))

# Header
f.write("FoamFile\n")
f.write("{\n")
f.write("    version  2.0;\n")
f.write("    format   ascii;\n")
f.write("    class    dictionary;\n")
f.write("    object   blockMeshDict;\n")
f.write("}\n\n")

f.write("convertToMeters {};\n\n".format(1.0))

# Vertices
vert = np.array([
    [r, 0, -H/2],                       # 0
    [r*sqrt(2)/2, r*sqrt(2)/2, -H/2],   # 1
    [0, r, -H/2],                       # 2
    [-r*sqrt(2)/2, r*sqrt(2)/2, -H/2],  # 3
    [-r, 0, -H/2],                      # 4
    [-r*sqrt(2)/2, -r*sqrt(2)/2, -H/2], # 5
    [0, -r, -H/2],                      # 6
    [r*sqrt(2)/2, -r*sqrt(2)/2, -H/2],  # 7

    [R, 0, -H/2],                       # 8
    [R*sqrt(2)/2, R*sqrt(2)/2, -H/2],   # 9
    [0, R, -H/2],                       # 10
    [-R*sqrt(2)/2, R*sqrt(2)/2, -H/2],  # 11
    [-R, 0, -H/2],                      # 12
    [-R*sqrt(2)/2, -R*sqrt(2)/2, -H/2], # 13
    [0, -R, -H/2],                      # 14
    [R*sqrt(2)/2, -R*sqrt(2)/2, -H/2],  # 15

    [r, 0, H/2],                       # 16
    [r*sqrt(2)/2, r*sqrt(2)/2, H/2],   # 17
    [0, r, H/2],                       # 18
    [-r*sqrt(2)/2, r*sqrt(2)/2, H/2],  # 19
    [-r, 0, H/2],                      # 20
    [-r*sqrt(2)/2, -r*sqrt(2)/2, H/2], # 21
    [0, -r, H/2],                      # 22
    [r*sqrt(2)/2, -r*sqrt(2)/2, H/2],  # 23

    [R, 0, H/2],                       # 24
    [R*sqrt(2)/2, R*sqrt(2)/2, H/2],   # 25
    [0, R, H/2],                       # 26
    [-R*sqrt(2)/2, R*sqrt(2)/2, H/2],  # 27
    [-R, 0, H/2],                      # 28
    [-R*sqrt(2)/2, -R*sqrt(2)/2, H/2], # 29
    [0, -R, H/2],                      # 30
    [R*sqrt(2)/2, -R*sqrt(2)/2, H/2],  # 31
])

# Write Vertices
f.write("vertices\n")
f.write("(\n")
for i, row in enumerate(vert):
    f.write("    ( ")
    f.write("  ".join(map("{: .10e}".format, row)))
    # f.write(")\n")
    f.write(") // {0} \n".format(i))
f.write(");\n\n")


# Blocks
blocks = np.array([
    [0, 8, 9, 1, 16, 24, 25, 17],
    [1, 9, 10, 2, 17, 25, 26, 18],
    [2, 10, 11, 3, 18, 26, 27, 19],
    [3, 11, 12, 4, 19, 27, 28, 20],
    [4, 12, 13, 5, 20, 28, 29, 21],
    [5, 13, 14, 6, 21, 29, 30, 22],
    [6, 14, 15, 7, 22, 30, 31, 23],
    [7, 15, 8, 0, 23, 31, 24, 16]
])

ncells = np.array([
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20],
    [20, 20, 20]
]) 
ncells[:,0:2] = np.around(ncells[:,0:2] * res)
ncells = ncells.astype(int)

grading = np.array([
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0],
])

# Write Blocks
f.write("blocks\n")
f.write("(\n")
for i, (block, n, grad) in enumerate(zip(blocks, ncells, grading)):
    # Connectivity
    f.write("    // block {}\n".format(i))
    f.write("    hex (")
    f.write(" ".join(map(str, block)))
    f.write(") ")

    # Number of Cells
    f.write("(")
    f.write(" ".join(map(str, n)))
    f.write(") ")

    # Grading
    f.write(" simpleGrading ")
    f.write("(")
    f.write(" ".join(map(str, grad)))
    f.write(")\n\n")

f.write(");\n\n")

# Edges
edges = np.array([
    [0, 1],
    [8, 9],
    [16, 17],
    [24, 25],

    [1, 2], 
    [9, 10],
    [17, 18],
    [25, 26],

    [2, 3],
    [10, 11],
    [18, 19],
    [26, 27],

    [3, 4],
    [11, 12],
    [19, 20],
    [27, 28],

    [4, 5],
    [12, 13],
    [20, 21],
    [28, 29],

    [5, 6],
    [13, 14],
    [21, 22],
    [29, 30],

    [6, 7],
    [14, 15],
    [22, 23],
    [30, 31],

    [7, 0],
    [15, 8],
    [23, 16],
    [31, 24]
])

# Extra points
epoints = np.array([
    [r*sqrt(3)/2, r/2, -H/2],
    [R*sqrt(3)/2, R/2, -H/2],
    [r*sqrt(3)/2, r/2, H/2],
    [R*sqrt(3)/2, R/2, H/2],

    [r/2, r*sqrt(3)/2, -H/2],
    [R/2, R*sqrt(3)/2, -H/2],
    [r/2, r*sqrt(3)/2, H/2],
    [R/2, R*sqrt(3)/2, H/2],

    [-r/2, r*sqrt(3)/2, -H/2],
    [-R/2, R*sqrt(3)/2, -H/2],
    [-r/2, r*sqrt(3)/2, H/2],
    [-R/2, R*sqrt(3)/2, H/2],

    [-r*sqrt(3)/2, r/2, -H/2],
    [-R*sqrt(3)/2, R/2, -H/2],
    [-r*sqrt(3)/2, r/2, H/2],
    [-R*sqrt(3)/2, R/2, H/2],

    [-r*sqrt(3)/2, -r/2, -H/2],
    [-R*sqrt(3)/2, -R/2, -H/2],
    [-r*sqrt(3)/2, -r/2, H/2],
    [-R*sqrt(3)/2, -R/2, H/2],

    [-r/2, -r*sqrt(3)/2, -H/2],
    [-R/2, -R*sqrt(3)/2, -H/2],
    [-r/2, -r*sqrt(3)/2, H/2],
    [-R/2, -R*sqrt(3)/2, H/2],

    [r/2, -r*sqrt(3)/2, -H/2],
    [R/2, -R*sqrt(3)/2, -H/2],
    [r/2, -r*sqrt(3)/2, H/2],
    [R/2, -R*sqrt(3)/2, H/2],

    [r*sqrt(3)/2, -r/2, -H/2],
    [R*sqrt(3)/2, -R/2, -H/2],
    [r*sqrt(3)/2, -r/2, H/2],
    [R*sqrt(3)/2, -R/2, H/2]
])


# Write Edges
f.write("edges\n")
f.write("(\n")
for i, (edge, point) in enumerate(zip(edges, epoints)):

    f.write("    arc ")
    f.write(" ".join(map(str, edge)))

    f.write(" (")
    f.write("  ".join(map("{:.10e}".format, point)))
    f.write(")\n")

f.write(");\n\n")

# Boundaries
inner = np.array([
    [0, 16, 17, 1],
    [1, 17, 18, 2],
    [2, 18, 19, 3],
    [3, 19, 20, 4],
    [4, 20, 21, 5],
    [5, 21, 22, 6],
    [6, 22, 23, 7],
    [7, 23, 16, 0]
])

outer = np.array([
    [8, 24, 25, 9],
    [9, 25, 26, 10],
    [10, 26, 27, 11],
    [11, 27, 28, 12],
    [12, 28, 29, 13],
    [13, 29, 30, 14],
    [14, 30, 31, 15],
    [15, 31, 24, 8]
])

bottom = np.array([
    [0, 8, 9, 1],
    [1, 9, 10, 2],
    [2, 10, 11, 3],
    [3, 11, 12, 4],
    [4, 12, 13, 5],
    [5, 13, 14, 6],
    [6, 14, 15, 7],
    [7, 15, 8, 0]
])

top = np.array([
    [16, 24, 25, 17],
    [17, 25, 26, 18],
    [18, 26, 27, 19],
    [19, 27, 28, 20],
    [20, 28, 29, 21],
    [21, 29, 30, 22],
    [22, 30, 31, 23],
    [23, 31, 24, 16]
])

boundaries=[inner, outer, top, bottom]
bnames = ["inner_wall","outer_wall","bottom","top"]
btypes = ["wall", "wall", "patch", "patch"]

# Write Boundaries
f.write("boundary\n")
f.write("(\n")
for i, (name, arr, btype) in enumerate(zip(bnames, boundaries, btypes)):
    f.write("    {}\n".format(name))
    f.write("    {\n")
    f.write("        type {};\n".format(btype))
    f.write("        faces\n")
    f.write("        (\n")

    for row in arr:
        f.write("            (")
        f.write(" ".join(map(str, row)))
        f.write(")\n")

    f.write("        );\n")
    f.write("    }\n\n")

f.write(");")
f.close()

# plots
fig, ax = plt.subplots(1,1)
ax.set_title('Mesh Vertices')

# Edit the font, font size, and axes widthmpl.rcParams['font.family'] = 'Avenir'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2

# Vertices
ax.scatter(vert[:,0], vert[:,1], c='k')
ax.scatter(epoints[:,0], epoints[:,1], c='r')    

plt.show()
