import cProfile as cpo
import pstats as ps
from main import main

cpo.run("main()", "restats")
p = ps.Stats('restats')
p.sort_stats('cumulative').print_stats(30)
