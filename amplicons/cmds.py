import os


# TODO: Break this file up

def get_primer_pairs():
    with open('amplicon_len_pairs.txt', 'r') as f:
        lines = f.read().split('\n')

    chunks = []
    for i in range(0, len(lines), 4):
        chunk = lines[i:i+4]
        chunks.append(chunk)

    chunks = chunks[1:]

    primer_dir = 'primers'

    if not os.path.exists(primer_dir):
        os.makedirs(primer_dir)

    c = 0
    for chunk in chunks:
        c += 1
        with open('{}/primers_{}.txt'.format(primer_dir, c), 'w') as f:
            f.write('{}\n{}'.format(chunk[0], chunk[1]))
    return c, chunks


def chunks_to_primer_names(chunks):
    primers = set()
    for chunk in chunks:
        p1 = chunk[0].split('\t')[0]
        p2 = chunk[1].split('\t')[0]
        primers.add(p1)
        primers.add(p2)
    return list(primers)


def no_comments(lines):
    return list(filter(lambda l: not l.startswith('#'), lines))


def primer_scores(chunks):
    primers = chunks_to_primer_names(chunks)
    p_scores = {}
    for p in primers:
        with open('{}_sequences_hits.txt'.format(p), 'r') as f:
            lines = no_comments(f.read().split('\n'))
        scores = [float(line.split(',')[-2]) for line in lines]
        p_scores[p] = sum(scores)/len(scores)
    return p_scores


def generate_primers(reference_name, alignment_name):
    from primerprospector.generate_primers_denovo import search_sequences
    # -i aligned.fasta -p 0.95 -a sars-cov-2.fasta -o 95-primers.txt
    search_sequences(
        input_fasta_filepath = alignment_name,
        sequence_length = 5,
        exclude_fasta_filepath = None,
        verbose = False,
        percent_match = 1,
        full_primer_length = 20,
        output_f = '95-primers.txt',
        specificity_threshold = 0.01,
        log_filepath = None,
        standard_index_file = reference_name,
        search_range = None
    )


def make_primer_hits():
    # -i 95-primers.txt -a 200:400
    from primerprospector.sort_denovo_primers import analyze_primers as sort_primers
    sort_primers(
        hits_file='95-primers.txt',
        output_dir='.',
        verbose=False,
        variable_pos_freq=0.2,
        sort_method='S',
        known_primers_filepath=None,
        primer_name='',
        match_len=10,
        cmp_truncate_len=10,
        amplicon_len='200:400'
    )


def amplicon_hits(primers_fp, seqs_fp='sequences.fasta'):
    # -f sequences.fasta -P min_deg_primers.txt
    from primerprospector.analyze_primers import analyze_primers
    analyze_primers(
        fasta_fps=seqs_fp,
        verbose=False,
        output_dir='.',
        primers_filepath=primers_fp,
        primer_name=None,
        primer_sequence=None,
        tp_len=5,
        last_base_mm=3,
        tp_mm=1,
        non_tp_mm=0.4,
        tp_gap=3,
        non_tp_gap=1
    )


def find(reference_name, sequences_name, alignment_name):
    print('Generating primers...')
    generate_primers(reference_name, alignment_name)
    print('Done!')
    print('Generating amplicon primer pairs...')
    make_primer_hits()
    n, chunks = get_primer_pairs()
    print('Done!')
    print('Finding amplicon hits...')
    for i in range(n):
        print('Getting hits for pair {}/{}'.format(i+1, n))
        amplicon_hits('primers/primers_{}.txt'.format(i+1), sequences_name)
    print('Done!')
