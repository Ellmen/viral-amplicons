from .cmds import find, get_amplicons
from .least_degenerate import least_degenerate


class Amplicons(object):
    """Find amplicons for viral metagenomics"""

    def __str__(self):
        return "Find amplicons for viral metagenomics"

    def find(self, reference_name, sequences_name, alignment_name):
        find(reference_name, sequences_name, alignment_name)

    def ld(self):
        least_degenerate()

    def get_amplicons(self, sequences_name, p1, p2):
        get_amplicons(sequences_name, p1, p2)
