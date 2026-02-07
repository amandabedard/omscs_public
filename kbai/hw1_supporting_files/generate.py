# Creating code to generate one state at a time

# Our state object. We can use this to test the generator
example = {
    "frodo": "LEFT",
    "ring": "LEFT",
    "sam": "LEFT",
    "gollum": "LEFT"
}

# The initial state generator. We are focused on only generating valid transition states, not
# checking the results. That's for test.py
def generate(initial_state:dict):
    transition_states = []
    # The rules:
    # 1. Sam must always flip sides (he steers the boat)
    # 2. Frodo and Gollum cannot be on the boat with the ring
    # (so the ring will be treated as its own entity)
    # 3. Frodo and Gollum cannot drive the boat

    # Sam is the key piece in this decision
    
    return transition_states