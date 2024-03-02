import ezdxf
import sys
from ezdxf.addons.drawing.matplotlib import qsave

if len(sys.argv[0]) == 1:
    print("Please supply dxf file as argument")
    sys.exit(1)

try:
    print(f"Checking DXF file {sys.argv[1]}...")
    dxf = ezdxf.readfile(sys.argv[1])
    valid = False
    msp = dxf.modelspace()
    for e in msp:
        if e.dxftype() == 'LINE':
            valid = True
            print(e.dxf.start[0], e.dxf.start[1], e.dxf.end[0], e.dxf.end[1])
    if valid:
        print(f"DXF file {sys.argv[1]} is valid")
    else:
        print(f"DXF file {sys.argv[1]} is not valid")
    qsave(msp, f'out.png')
except IOError:
    print("Cannot open dxf file, exiting...")
    sys.exit(1)
