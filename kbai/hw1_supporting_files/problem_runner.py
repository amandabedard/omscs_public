from generate import generate
from test import test

START_STATE = {
    "frodo": False,
    "ring": False,
    "sam": False,
    "gollum": False
}
END_STATE = {
    "frodo": True,
    "ring": True,
    "sam": True,
    "gollum": True
}

    
# Doing depth runs vs breadth since i already worked out that the paths
# to the solution are the same lenght
def run(state=START_STATE, previous_states=[], turn=1, response=[]):
    transitions = generate(state)
    states = test(state, transitions, previous_states)
    previous_states.append(states)
    response.append((turn, states))

    # Break out of recursion
    if END_STATE in states or states == []:
        return response
    else:
        for new_state in states:
            run(new_state, previous_states, turn+1, response)

if __name__ == "__main__":
    res = run()
    print(f"Got res: {res}")
