import random
import math
import sympy as sp
import pandas as pd
import problem_bank_helpers as pbh

def imports(data):
    import random
    import math
    import sympy as sp
    import pandas as pd
    import problem_bank_helpers as pbh
    
def generate(data):
    data2 = pbh.create_data2()
    
    
    
    # define bounds of the variables
    m_load = random.randint(10,100)
    m_h = pbh.roundp(random.uniform(2, 4), sigfigs = 2)
    f_max = random.randint(1200,1500)
    
    
    
    # store the variables in the dictionary "params"
    data2["params"]["m_load"] = m_load
    data2["params"]["m_h"] = m_h
    data2["params"]["f_max"] = f_max
    
    
    
    
    
    ## Part 1
    
    # define correct answers
    
    g = 9.81
    t = (3 * m_h * g) / (2 * f_max)
    data2["correct_answers"]["part1_ans"] = t
    
    ## Part 2
    
    # define correct answers
    
    t_f = m_load * g
    data2["correct_answers"]["part2_ans"] = t_f
    
    ## Part 3
    
    # define correct answers
    
    a_max = (2 * f_max - m_h * g) / (m_h + m_load)
    
    data2["correct_answers"]["part3_ans"] = a_max
    
    ## Part 4
    
    # define correct answers
    
    v1 = (3 / 4) * f_max - (3 / 2) * m_h * g
    t2 = 3 - ((3 * m_h * g) / (2 * f_max))
    t1 = 3 / 2
    def v(t):
      z1 = -(f_max / 3) * t**2 + t * (2 * f_max - m_h *g)
      z2 = m_h + m_load
      v_t = z1 / z2
      return v_t
    v_b = v(t2)
    v_a = v(t1)
    v2 = v_b - v_a + v1
    data2["correct_answers"]["part4_ans"] = v2
    
    
    
    
    
    
    
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
