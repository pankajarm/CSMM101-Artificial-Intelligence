import sys
import resource
import time
import output
from bfs import BFS
from dfs import DFS
from state import State
from output import Output

# start with main function that you want to build
def main():
    # python driver.py bfs 0,8,7,6,5,4,3,2,1
    arguments = sys.argv
    search_type = arguments[1]
    # create a list of initial states from arguments[2]
    initial_state_list = [ int(x) for x in arguments[2].split(',') ]
    # now use this list to create initial_state object from State class
    initial_state = State(initial_state_list)
    # let's use time var to time execution
    start_time = time.time()
    # create output Object from Output class
    output = Output()

    if search_type == 'bfs':
        output = BFS(initial_state)
    elif search_type == 'dfs':
        output = DFS(initial_state)
    # elif search_type == 'ast':
    #     output = solve_ast(initial_state)
    else:
        print('Invalid search_type: {}'.format(search_type))

    # Let's add max ram uage and running time to output object
    output.max_ram_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    output.running_time = time.time() - start_time
    f = open('output.txt', 'w')
    f.write(str(output))
    f.close()

if __name__ == '__main__':
    main()
