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

# DFS was not the move. Using loops instead.
def run(state=START_STATE):
    previous_states = [state]
    response = []
    frontier = [state]
    turn = 1
    while frontier:
        print(f"Working on turn {turn}")
        next_frontier = []
        found = False
        for current_state in frontier:
            transitions = generate(current_state)
            states = test(current_state, transitions, previous_states)
            if END_STATE in states:
                found = True
            previous_states.extend(states)
            next_frontier.extend(states)
        response.append((turn, next_frontier))
        if found or not next_frontier:
            return response
        frontier = next_frontier
        turn += 1
    return response

if __name__ == "__main__":
    res = run()
    print(f"Got res: {res}")
