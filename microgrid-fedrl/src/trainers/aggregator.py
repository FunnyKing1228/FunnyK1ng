def fed_avg(states):
    """Federated averaging of model states."""
    result = {}
    for k in states[0]:
        result[k] = sum(s[k] for s in states) / len(states)
    return result
