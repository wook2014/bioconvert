###########################################################################
# Bioconvert is a project to facilitate the interconversion               #
# of life science data from one format to another.                        #
#                                                                         #
# Authors: see CONTRIBUTORS.rst                                           #
# Copyright © 2018  Institut Pasteur, Paris and CNRS.                     #
# See the COPYRIGHT file for details                                      #
#                                                                         #
# bioconvert is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# bioconvert is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with this program (COPYING file).                                 #
# If not, see <http://www.gnu.org/licenses/>.                             #
###########################################################################
"""Converts :term:`STOCKHOLM` to :term:`PHYLIP` format."""
import colorlog
from Bio import SeqIO

from bioconvert import ConvBase
from bioconvert.core.decorators import compressor, requires

_log = colorlog.getLogger(__name__)


__all__ = ["STOCKHOLM2PHYLIP"]


class STOCKHOLM2PHYLIP(ConvBase):
    """
    Converts a sequence alignment from :term:`STOCKHOLM` format to :term:`PHYLIP` interleaved format

    Methods available are based on squizz [SQUIZZ]_, and
    biopython [BIOPYTHON]_.

    """

    #: Default value
    _default_method = "biopython"

    def __init__(self, infile, outfile=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input :term:`STOCKHOLM` file.
        :param str outfile: (optional) output :term:`FASTA` file
        """
        super(STOCKHOLM2PHYLIP, self).__init__(infile, outfile)

    @requires(python_library="biopython")
    @compressor
    def _method_biopython(self, *args, **kwargs):
        """Convert :term:`STOCKHOLM` interleaved file in :term:`PHYLIP` format using biopython.

        `Bio.SeqIO Documentation <https://biopython.org/docs/1.76/api/Bio.SeqIO.html>`_"""
        sequences = list(SeqIO.parse(self.infile, "stockholm"))
        count = SeqIO.write(sequences, self.outfile, "phylip")
        _log.info("Converted %d records to phylip" % count)

    @requires("squizz")
    @compressor
    def _method_squizz(self, *args, **kwargs):
        """Convert :term:`STOCKHOLM` interleaved file in :term:`PHYLIP` interleaved format using squizz tool."""
        cmd = "squizz -c PHYLIPI {infile} > {outfile}".format(infile=self.infile, outfile=self.outfile)
        self.execute(cmd)
