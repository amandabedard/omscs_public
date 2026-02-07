import copy
# We will take the initial state and a transition tuple to build the new state
# and make sure it is not invalid
def test(initial_state:dict, transition_list:list[tuple]) -> list[dict]:
    # We will take the list of generated states and check them with the test function against the rules
    # we know. They are:
    # 1. Gollum nor Frodo can be alone with the Ring
    filtered_list = []
    return filtered_list

def _apply(initial_state:dict, transition_list:list[tuple]):
    # We will apply the transition to the state
    transformed_states = []
    for transition in transition_list:
        new_state = copy.deepcopy(initial_state)
        # Flipping the state for 0 
        new_state[transition[0]] = not new_state[transition[0]]
        if transition[1]:
            # If it's not sam in the boat alone
            new_state[transition[1]] = not new_state[transition[1]]
        transformed_states.append(new_state)

    return transformed_states

def _is_valid(state: dict) -> bool:
    # Is this a valid state? We will go through conditions to determine
    valid = True

    # Writing out the conditions so i don't get confused
    frodo_with_ring = state["frodo"] == state["ring"]
    frodo_with_sam = state["frodo"] == state["sam"]
    gollum_with_ring = state["gollum"] == state["ring"]
    gollum_with_sam = state["gollum"] == state["sam"]
    frodo_with_gollum = state["gollum"] == state["frodo"]

    # check if frodo or gollum is alone with the ring
    if frodo_with_ring and not frodo_with_gollum and not frodo_with_sam:
        valid = False
    if gollum_with_ring and not frodo_with_gollum and not gollum_with_sam:
        valid = False

    return valid

if __name__ == "__main__":
    test()