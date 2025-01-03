#
#  This file is part of Bioconvert software
#
#  Copyright (c) 2017 - Bioconvert Development Team
#
#  Distributed under the terms of the 3-clause BSD license.
#  The full license is in the LICENSE file, distributed with this software.
#
#  website: https://github.com/biokit/bioconvert
#  documentation: http://bioconvert.readthedocs.io
#
##############################################################################
"""Convert :term:`BED` format to :term:`WIGGLE` format"""
import colorlog

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

_log = colorlog.getLogger(__name__)

__all__ = ["BED2WIGGLE"]


class BED2WIGGLE(ConvBase):
    """Convert sorted :term:`BED` file into :term:`WIGGLE` file

    Methods available are based on wiggletools [WIGGLETOOLS]_.

    """

    _default_method = "wiggletools"

    def __init__(self, infile, outfile):
        """
        :param str infile: The path to the input BED file. **It must be sorted**.
        :param str outfile: The path to the output file
        """
        super(BED2WIGGLE, self).__init__(infile, outfile)

    @requires("wiggletools")
    def _method_wiggletools(self, *args, **kwargs):
        """Convert BED to WIGGLE using wiggletools

        `wiggletools documentation <https://github.com/Ensembl/WiggleTools>`_"""
        cmd = "wiggletools {} > {}".format(self.infile, self.outfile)
        self.execute(cmd)
