import subprocess
from cStringIO import StringIO
from Bio import SeqIO


def getSequence(title, db='nt'):
    """
    @param title: A C{str} sequence title from a BLAST hit. Of the form
        'gi|63148399|gb|DQ011818.1| Description...'.
    @param db: the C{str} name of the BLAST database to search.
    """
    titleId = title.split(' ', 1)[0]
    fasta = subprocess.check_output(
        ['blastdbcmd', '-entry', titleId, '-db', db])
    return SeqIO.read(StringIO(fasta), 'fasta')