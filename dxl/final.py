import dxl 
a=dxl.get_available_ports()
print(a)
b={1: 512, 2:900, 3:512}
d= dxl.dxl(a[0], 1000000)
print(d.scan(4))
d.set_goal_position(b)
print("done")
