from dark.reads import AARead, DNARead, RNARead
from dark.fastq import FastqReads

from unittest import TestCase
from mock import patch
from mocking import mockOpen


class TestFastqReads(TestCase):
    """
    Tests for the L{dark.fastq.FastqReads} class.
    """

    def testEmpty(self):
        """
        An empty FASTQ file results in an empty iterator.
        """
        mockOpener = mockOpen()
        with patch('__builtin__.open', mockOpener, create=True):
            reads = FastqReads('filename.fastq')
            self.assertEqual([], list(reads))

    def testOneRead(self):
        """
        A FASTQ file with one read must be read properly.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq'))
            self.assertEqual([DNARead('id1', 'ACGT', '!!!!')], reads)

    def testTwoReads(self):
        """
        A FASTQ file with two reads must be read properly and its
        sequences must be returned in the correct order.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!',
                          '@id2', 'TGCA', '+', '????'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq'))
            self.assertEqual(2, len(reads))
            self.assertEqual([DNARead('id1', 'ACGT', '!!!!'),
                              DNARead('id2', 'TGCA', '????')], reads)

    def testTypeDefaultsToDNA(self):
        """
        A FASTQ file whose type is not specified must result in reads that
        are instances of DNARead.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq'))
            self.assertTrue(isinstance(reads[0], DNARead))

    def testTypeAA(self):
        """
        A FASTQ file whose read class is AARead must result in reads that
        are instances of AARead.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq', AARead))
            self.assertTrue(isinstance(reads[0], AARead))

    def testTypeDNA(self):
        """
        A FASTQ file whose read class is DNARead must result in reads that
        are instances of DNARead.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq', DNARead))
            self.assertTrue(isinstance(reads[0], DNARead))

    def testTypeRNA(self):
        """
        A FASTQ file whose read class is RNARead must result in reads that
        are instances of RNARead.
        """
        data = '\n'.join(['@id1', 'ACGT', '+', '!!!!'])
        mockOpener = mockOpen(read_data=data)
        with patch('__builtin__.open', mockOpener, create=True):
            reads = list(FastqReads('filename.fastq', RNARead))
            self.assertTrue(isinstance(reads[0], RNARead))