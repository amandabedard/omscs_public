# Creating code to generate one state at a time

# Our state object. We can use this to test the generator
example = {
    "frodo": False,
    "ring": False,
    "sam": False,
    "gollum": False
} # False is left, True is right.

# The initial state generator. We are focused on only generating valid transition states, not
# checking the results. That's for test.py
def generate(initial_state:dict) -> tuple:
    # Sam can always go by himself
    transition_states = [("sam",)]
    # The rules:
    # 1. Sam must always flip sides (he steers the boat)
    # 2. Frodo and Gollum cannot be on the boat with the ring
    # (so the ring will be treated as its own entity)
    # 3. Frodo and Gollum cannot drive the boat

    # Sam is the key piece in this decision
    sam_state = initial_state["sam"]

    # Basically, any valid transition is sam + another entity, or
    # sam on his own depending on the initial state.
    if sam_state == initial_state["ring"]:
        # Sam can take the ring
        transition_states.append(("sam", "ring"))
    if sam_state == initial_state["frodo"]:
        # Sam can take frodo
        transition_states.append(("sam", "frodo"))
    if sam_state == initial_state["gollum"]:
        # Sam can take gollum
        transition_states.append(("sam", "gollum"))
    
    
    print(f"Discovered the following transition states: {transition_states}")
    return transition_states