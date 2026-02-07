# We will take the initial state and a transition object to build the new state
# and make sure it is not invalid
def test(initial_state, transition_list:list[dict]):
    # We will take the list of generated states and check them with the test function against the rules
    # we know. They are:
    # 1. Gollum nor Frodo can be alone with the Ring
    filtered_list = []
    return filtered_list