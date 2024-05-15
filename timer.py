import timeit as ti

#Gives the minimum time of execution of the generate_patterns function

def timer_generate_patterns():
    setup_code = "from Hopfield import generate_patterns"
    stmt_code = "generate_patterns(50,100)"
    time = ti.repeat(setup = setup_code, stmt = stmt_code, repeat = 5, number = 10000)#attention temps pour n iteration
    print ("generate_patterns() minimum time of execution: ", min(time))

def timer_perturb_pattern():
    setup_code = "from Hopfield import perturb_pattern"
    stmt_code = "perturb_pattern(np.zeros(100),50)"
    time = ti.repeat(setup = setup_code, stmt = stmt_code, repeat = 5, number = 10000)
    print ("perturb_pattern minimum time of execution: ", min(time))

def timer_pattern_match():
    setup_code = "from Hopfield import pattern_match"
    stmt_code = "pattern_match(np.zeros(100,100),np.ones(100)"
    time = ti.repeat(setup=setup_code, stmt=stmt_code, repeat=5, number=10000)
    print ("pattern_match minimum time of execution: ", min(time))

def timer_hebbian_weights():
    setup_code = "from Hopfield import hebbian_weights"
    stmt_code = "hebbian_weights(np.zeros(100,100))"
    time = ti.repeat(setup=setup_code, stmt=stmt_code, repeat=5, number=10000)
    print ("hebbian_weights minimum time of execution:", min(time))

def timer_storkey_weights():
    setup_code = "from Hopfield import storkey_weights"
    stmt_code = "storkey_weights(np.zeros(100,100))"
    time = ti.repeat(setup=setup_code, stmt=stmt_code, repeat=5, number=10000)
    print ("storkey_weights minimum time of execution:" , mint (time))
