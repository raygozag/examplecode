import sys


length=int(sys.argv[1])

con=342976341834.91656


basew=650*1.67e-24
plw=(basew*length*con)/1e-6
print(str(plw)+" ug(s)")
