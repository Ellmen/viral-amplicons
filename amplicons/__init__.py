from .cmds import find
from .least_degenerate import least_degenerate


class Amplicons(object):
    """Find amplicons for viral metagenomics"""

    def __str__(self):
        return "Find amplicons for viral metagenomics"

    def find(self, reference_name, sequences_name, alignment_name):
        find(reference_name, sequences_name, alignment_name)

    def ld(self):
        least_degenerate()
