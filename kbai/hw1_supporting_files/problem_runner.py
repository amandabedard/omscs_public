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

    
def run(state=START_STATE):
    previous_states = []
    response = []
    # Using a stack instead of recursion for my dfs
    stack = [(state, 1)]
    while stack:
        current_state, turn = stack.pop()
        transitions = generate(current_state)
        states = test(current_state, transitions, previous_states)
        previous_states.extend(states)
        response.append((turn, states))
        # We got our goal
        if END_STATE in states or states == []:
            return response
        for new_state in states:
            stack.append((new_state, turn + 1))
    return response

if __name__ == "__main__":
    res = run()
    print(f"Got res: {res}")
