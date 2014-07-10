# Finite State Machine simulator for Regexp
# Plug-in the mappings defining the FSM and the accepting state

edges = {}
accepting = []

def fsmsim(string, current, edges, accepting):
	if string[0] == "":
		return current in accepting
	else:
		letter = string[0]
		if (current, letter) in edges:
			destination = edges([current, edges])
			remaining_string = string[1:]
			fsmsim(remaining_string, destination, accepting, edges)
		else:
			return False




