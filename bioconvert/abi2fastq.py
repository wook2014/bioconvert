##############################################################################
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
##############################################################################
"""Convert :term:`ABI` format to :term:`FASTQ` format"""
from bioconvert import ConvBase, requires

__all__ = ["ABI2FASTQ"]


class ABI2FASTQ(ConvBase):
    """Convert :term:`ABI` file to :term:`FASTQ` file

    :term:`ABI` files are created by ABI sequencing machine and includes
    PHRED quality scores for base calls. This allows the creation
    of :term:`FastQ` files.

    Method implemented is based on BioPython [BIOPYTHON]_.
    """

    #: Default value
    _default_method = "biopython"

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input ABI file
        :param str outfile: output FASTQ filename

        """
        super(ABI2FASTQ, self).__init__(infile, outfile, *args, **kargs)

    @requires(python_library="biopython")
    def _method_biopython(self, *args, **kwargs):
        """For this method we use the biopython package Bio.SeqIO.

        `Bio.SeqIO Documentation <https://biopython.org/docs/1.76/api/Bio.SeqIO.html>`_"""
        from Bio import SeqIO

        records = SeqIO.parse(self.infile, "abi")
        SeqIO.write(records, self.outfile, "fastq")
