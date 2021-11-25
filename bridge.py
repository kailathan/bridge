def compute_I_local(b,h):
    return (b*h**3/12)
def compute_I_global(I_list, areas, ys, y_bar):
    i_global = 0
    for i in range(len(I_list)):
        d_y = abs(ys[i] - y_bar)
        i_global += I_list[i] + areas[i]*d_y**2
    return i_global
def compute_y_local(h, to_bottom):
    return (h/2)+to_bottom
def compute_y_bar(areas, ys):
    y_bar = 0
    sum_areas = 0
    '''takes in a dictionary of areas and their corresponding y values (lists have to be the same size)'''
    for i in range(len(areas)):
        y_bar += areas[i]*ys[i]
        sum_areas += areas[i]
    print(y_bar)
    print(sum_areas)
    return y_bar/sum_areas
def compute_Q(areas, ys, y_bar):
    q = 0
    for i in range(len(areas)):
        d_y = abs(ys[i]-y_bar)
        q += areas[i]*d_y
    return q

if __name__ == "__main__":
    #where main function will be
    #user defines heights, bases, distance from bottom of each area
    heights = [1.27, 1.27, 1.27, 72.2, 72.2, 1.27]
    bases = [100, 10, 10, 1.27, 1.27, 80]
    d_bottom = [73.73, 72.46, 72.46, 1.27, 1.27, 0]
    areas = []
    ys = []
    i_list = []
    #populating lists
    for i in range(len(heights)):
        ys.append(compute_y_local(heights[i],d_bottom[i]))
        areas.append(heights[i]*bases[i])
        i_list.append(compute_I_local(bases[i], heights[i]))
    print("ilist", i_list)
    y_bar = compute_y_bar(areas,ys)
    i_global = compute_I_global(i_list, areas, ys, y_bar)
    q = compute_Q([51.3,51.3,101.6], [20.2, 20.2, 0.635], y_bar)

    mat_properties = {
    "dimensions": [813,1016,1.27],
    "tensile strength": 30,
    "compressive strength": 6,
    "shear strength": 4,
    "young's modulus": 4000
    "poisson's ratio": 0.2,
    "shear strength glue": 2
    }







