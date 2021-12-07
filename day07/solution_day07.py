import numpy as np

def load_data(infile):
    data = np.loadtxt(infile, delimiter=',')
    return data

def calc_fuel_consumption(data):
    a = np.median(data)
    res = np.sum(np.abs(data-a))
    return res

def calc_a(data):
    a1 = data.mean()
    delta = np.sum(np.sign(a1-data))
    a = a1 - delta/(2*len(data))
    aint = np.round(a)
    return a, aint

def calc_fuel_consumption_2(data, a):
    r = np.abs(data-a)
    res = 0.5*r*(r+1)
    return np.sum(res)

def calc_fuel_consumption_brute_force(data):
    res = []
    for a in range(0, 1955):
        r = np.abs(data-a)
        res.append((a, np.sum(0.5*r*(r+1))))
        rr = np.asarray(res)
    return rr[:,1].min()
        
def fun(a, data):
    r = np.abs(data-a)
    res = 0.5*r*(r+1)
    return np.sum(res)
    

if __name__ == '__main__':
    infile = 'input.txt'
    d = load_data(infile)
    # This one is trivial, it's just the summed absolute distances to the median
    print('The first solution is:', calc_fuel_consumption(d))

    # This one is a little tricky. The distances have the closed expression
    # n*(n+1)/2 where n is the absolute distance between the point and the
    # minimum: n_i = |x_i - a|.
    # we can find the minimum by differentiatigng, but we need to take care of
    # the sgn(a-x_i) term that we pick up. As long as that's smaller than one,
    # we can get the minimum by just adding it. Here we deal with integers,
    # therefore, we need to round at the end. 
    a = calc_a(d)
    print(calc_a(d))
    print('The second solution is:', calc_fuel_consumption_2(d,a[1]))
    # Just to check the result
    # print(calc_fuel_consumption_brute_force(d))
