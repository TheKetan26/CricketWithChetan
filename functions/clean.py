from ..models import Matches


def cleanUnwantedMatches():
    print('Starting cleaning!')

    types = ['CCH', 'CEC', 'CPL', 'HND', 'FRB', 'CTC', 'ILT', 'IPO', 'IPT', 'LPL', 'MSL', 'NTB', 'PSL', 'RHF', 'RLC', 'SAT', 'SFT', 'SMA', 'SSH', 'SSM', 'WBB', 'WCL', 'WSL', 'WTC']
    matches = []

    for type in types:
        match = Matches.objects.filter(type=type)
        matches.append(match)

    size, n = len(matches), 1

    for match in matches:
        match.delete()
        print(n, '/', size)
        n += 1

    print('Completed without any error!')
    return 'Completed!'

