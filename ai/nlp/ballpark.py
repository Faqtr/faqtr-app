import re


def get_acceptable_margin(n1, n2):
    n1, n2 = float(n1), float(n2)
    n1, n2 = min(n1, n2), max(n1, n2)

    if n1 >= n2 * 0.8 and n1 <= n2 * 1.2:
        return True

    return False


def get_most_relevant_data(claim, snip):
    # Get the first number from the claim
    claim_nos = [float(s) for s in re.findall(r'\b\d+\b', claim)]
    #acceptable_statements = []
    #for snip in data_snips:
    snip_nos = [float(s) for s in re.findall(r'\b\d+\b', snip)]
    snip_nos = sorted(snip_nos, reverse=True)
    claim_nos = sorted(claim_nos, reverse=True)
        # Add them to a list with the difference of nos as the key
    a = 0
    i = 0
    for nos in claim_nos:
        if i < len(snip_nos) and get_acceptable_margin(nos, snip_nos[i]):
            #acceptable_statements.append(snip)
            a += 1
        i += 1
    return float( a / len(claim_nos))

    #return acceptable_statements
