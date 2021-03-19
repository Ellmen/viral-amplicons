def count_degenerate(seq):
    nts = ['A','C','G','T']
    count = 0
    for bp in seq:
        if bp not in nts:
            count += 1
    return count


def prod(lst):
    val = 1.0
    for n in lst:
        val *= n
    return val


def degeneracy(seq):
    ones = ['A','C','G','T']
    twos = ['R','Y','S','W','K','M']
    threes = ['B','D','H','V']
    deg = {}
    for nt in ones:
        deg[nt] = 1
    for nt in twos:
        deg[nt] = 2
    for nt in threes:
        deg[nt] = 3
    deg['N'] = 4
    return prod([deg[nt] for nt in seq])


def least_degenerate():
    with open('amplicon_len_pairs.txt', 'r') as f:
        lines = f.read().split('\n')

    chunks = []
    for i in range(0, len(lines), 4):
        chunk = lines[i:i+4]
        chunks.append(chunk)

    chunks = chunks[1:]

    # min_count = 41
    min_count = 4**20
    min_chunk = []

    print('Degeneracy of each primer pair:')

    for chunk in chunks:
        p1 = chunk[0].split('\t')
        p2 = chunk[1].split('\t')
        # c1 = count_degenerate(p1[1])
        # c2 = count_degenerate(p2[1])
        c1 = degeneracy(p1[1])
        c2 = degeneracy(p2[1])
        print(c1 + c2)
        if c1 + c2 < min_count:
            min_count = c1 + c2
            min_chunk = chunk
        # if c1 + c2 == 20:
        #     print('Found a fiver')

    print('Least degenerate primers ({}) degeneracy combined'.format(min_count))
    print('\n'.join(min_chunk))
