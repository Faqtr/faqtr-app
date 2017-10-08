import re


def get_acceptable_margin(n1, n2):
    n1, n2 = float(n1), float(n2)
    n1, n2 = min(n1, n2), max(n1, n2)

    if n1 >= n2 * 0.8 and n1 <= n2 * 1.2:
        return True

    return False


def get_most_relevant_data(claim, data_snips):
    # Get the first number from the claim
    claim_nos = [int(s) for s in re.findall(r'\b\d+\b', claim)][0]

    acceptable_statements = []

    for snip in data_snips:
        snip_nos = [int(s) for s in re.findall(r'\b\d+\b', snip)]

        # Add them to a list with the difference of nos as the key
        for nos in snip_nos:
            if get_acceptable_margin(nos, claim_nos):
                acceptable_statements.append(snip)

    return acceptable_statements
