import copy

example_initial = {
    "frodo": False,
    "ring": False,
    "sam": False,
    "gollum": False
}
example_transitions =  [('sam',), ('sam', 'ring'), ('sam', 'frodo'), ('sam', 'gollum')]
previous_states = []
# We will take the initial state and a transition tuple to build the new state
# and make sure it is not invalid
def test(initial_state:dict, transition_list:list[tuple], previous_states: list[dict]) -> list[dict]:
    # We will take the list of generated states and check them with the test function against the rules
    # we know. They are:
    # 1. Gollum nor Frodo can be alone with the Ring
    all_states = _apply(initial_state, transition_list)
    filtered_list = [valid_state for valid_state in all_states if _is_valid(valid_state)]
    print(f"Found valid states: {filtered_list}")
    return filtered_list

def _apply(initial_state:dict, transition_list:list[tuple]):
    # We will apply the transition to the state
    transformed_states = []
    for transition in transition_list:
        new_state = copy.deepcopy(initial_state)
        # Flipping the state for 0 
        new_state[transition[0]] = not new_state[transition[0]]
        if len(transition) > 1 and transition[1]:
            # If it's not sam in the boat alone
            new_state[transition[1]] = not new_state[transition[1]]
        transformed_states.append(new_state)

    return transformed_states

def _is_valid(state: dict, previous_states: list[dict]) -> bool:
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
    if state in previous_states:
        # This moves us further away from our goal since it has been traversed before.
        valid = False

    return valid

if __name__ == "__main__":
    test(example_initial, example_transitions, previous_states)