import time
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def calc_pure_python(desired_width, max_iterations):
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    from guppy import hpy; hp = hpy()
    print ("heapy after creating y and x lists of floats")
    h = hp.heap()
    print (h)
	
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    print ("heapy after creating zs and cs using complex numbers")
    h = hp.heap()
    print (h)

    print ("Length of x:", len(x))
    print ("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_tine = time.time()
    secs = end_tine - start_time
    print (calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
	
    print ("heapy after calling calculate_z_serial_purepython")
    h = hp.heap()
    print (h)

    assert sum(output) == 33219980
    """
    print ("x_step",x_step)
    print ("y_step",y_step)
    print ("x:",x)
    print ("y", y)
    print ("ZS:",zs)
    print ("CS:",cs)
    """
def calculate_z_serial_purepython(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output
if __name__ == "__main__":
    calc_pure_python(desired_width = 1000, max_iterations = 300)
