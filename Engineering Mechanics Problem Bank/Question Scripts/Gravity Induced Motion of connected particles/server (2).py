import random
import pandas as pd
import math
import problem_bank_helpers as pbh

def imports(data):
    import random
    import pandas as pd
    import math
    import problem_bank_helpers as pbh
    
def generate(data):
    data2 = pbh.create_data2()
    
    # define bounds of the variables
    h = pbh.roundp(random.uniform(3,5), sigfigs=2)
    l = pbh.roundp(random.uniform((2*h +2),4 * h), sigfigs=2)
    m1 = pbh.roundp(random.uniform(3,6), sigfigs=2)
    m2 = pbh.roundp(random.uniform(2,7), sigfigs=2)
    u = pbh.roundp(random.uniform(0.2,0.9), sigfigs=2)
    theta = pbh.roundp(random.uniform(5, math.degrees(math.atan(u))-1), sigfigs=2)
    
    
    
    # store the variables in the dictionary "params"
    data2["params"]["h"] = h
    data2["params"]["l"] = l
    data2["params"]["m1"] = m1
    data2["params"]["theta"] = theta
    data2["params"]["m2"] = m2
    data2["params"]["u"] = u
    
    
    ## Part 1
    
    # define correct answers
    
    g = 9.81
    theta_r = math.radians(theta)
    u_l_i = m1 * g * h
    u_b_i = m2 * g * (2 * h + (l-h)*math.sin(theta_r))
    w_f = -1 * u * m2 * g * h * math.cos(theta_r)
    u_b_f = m2 * g * (2* h + math.sin(theta_r) * (l-(2*h)))
    z1 = 2 * (u_l_i + u_b_i + w_f - u_b_f)
    z2 = m1 + m2
    v = math.sqrt(z1 / z2)
    
    
    data2["correct_answers"]["part1_ans"] = v
    
    ## Part 2
    
    # define possible answers
    
    
    data2["correct_answers"]["part2_ans"] = v
    ## Part 3
    
    # define possible answers
    
    z3 = (m1 * g) + (m2 * g * math.sin(theta_r)) - (math.cos(theta_r) * u * m2 * g)
    a = z3 / z2
    t = m1 * a + m1 * g
    data2["correct_answers"]["part3_ans"] = t
    
    ## Part 4
    
    # define possible answers
    
    f_r = t * (math.sqrt(2*(1-math.sin(theta_r))))
    data2["correct_answers"]["part4_ans"] = f_r
    
    ## Part 5
    
    # define possible answers
    
    b = math.asin((t * math.cos(theta_r)) / f_r)
    a = (math.pi / 2) - b
    a_d = math.degrees(a)
    data2["correct_answers"]["part5_ans"] = a_d
    
    ## Part 6
    
    # define possible answers
    
    min = 3
    
    data2["correct_answers"]["part6_ans"] = min
    
    
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
