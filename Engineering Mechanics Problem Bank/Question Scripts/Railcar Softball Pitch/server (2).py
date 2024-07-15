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
    v_r = random.randint(20,30)
    v_b_r = random.randint(15,40)
    theta = random.randint(10, 170)
    
    # store the variables in the dictionary "params"
    data2["params"]["v_r"] = v_r
    data2["params"]["v_b_r"] = v_b_r
    data2["params"]["theta"] = theta
    
    ## Part 1
    
    # define correct answers
    
    theta_r = math.radians(theta)
    
    z1 = (v_r**2) + (v_b_r**2) + (2 * v_r * v_b_r * math.cos(theta_r))
    v_b = math.sqrt(z1)
    data2["correct_answers"]["part1_ans"] = v_b
    
    ## Part 2
    
    # define correct answers
    
    z2 = v_b_r * math.sin(theta_r)
    z3 = (v_b_r * math.cos(theta_r)) + v_r
    a_r = math.atan(z2 / z3)
    if (a_r < 0):
        a_r_n = a_r + math.pi
    else:
        a_r_n = a_r
    a = math.degrees(a_r_n)
    data2["correct_answers"]["part2_ans"] = a
    
    # Update the data object with a new dict
    data.update(data2)
    
    # Start code added automatically by problem_bank_scripts

    # Convert backticks to code blocks/fences in answer choices.
    pbh.backticks_to_code_tags(data2)

    # Update data with data2
    data.update(data2)

    # End code added in by problem bank scripts

def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
