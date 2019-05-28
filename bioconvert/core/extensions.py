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
"""List of formats and associated extensions"""
from easydev import AttrDict

# Formats can be of type
# - sequence
# - alignment
# - binary
# - compression
# - database
# - variant

extensions = {
    'abi': ["abi", "ab1"],                      # sequence
    'bam': ["bam"],                             # alignment
    'bcf': ["bcf"],                             # variant
    'bed': ["bed"],                             # database
    'bedgraph': ["bedgraph"],                   # database
    'bigwig': ["bigwig", "bw"],                 # database
    'bigbed': ['bb', "bigbed"],
    'bz2': ['bz2'],                             # compression
    'bplink': ['bplink'],
    'cdao': ["cdao"],                           # phylo
    'cram': ["cram"],                           # alignment
    'clustal': ["clustal", "aln", "clw"],       # phylo
    'csv': ["csv"],                             # database
    'dsrc': ['dsrc'],                           # compression
    'embl': ['embl'],                           # annotation/sequence
    'fasta': ["fasta", "fa", "fst"],            # sequence
    'fastq': ["fastq", "fq"],                   # sequence
    'genbank': ['genbank', 'gbk', "gb"],        # annotation/sequence
    'gfa': ['gfa'],                             # assembly
    'gff2': ['gff'],
    'gff3': ['gff3'],                           # annotation
    'gz': ['gz'],
    'json': ['json'],                           # database
    'maf': ["maf"],     # !! this is MIRA format, not mutation alignment format
    'newick': ["newick", "nw", "nhx", "nwk"],   # phylo
    'nexus': ["nexus", "nx", "nex", "nxs"],     # phylo
    'ods': ['ods'],                             # database
    'paf': ['paf'],                             # assembly
    'phylip': ['phy', 'ph', 'phylip'],          # phylo
    'phyloxml': ['phyloxml', 'xml'],            # phylo
    'plink': ['plink'],
    'qual': ['qual'],                           # seauence
    'sam': ["sam"],                             # alignement
    'scf': ["scf"],                             # alignement
    'sra': ["sra"],                             # sra format
    'stockholm': ['sto', 'sth', 'stk', 'stockholm'], # alignment
    'twobit': ['2bit'],                         # sequence
    'tsv': ["tsv"],                             # database
    'vcf': ['vcf'],                             # variant
    'wiggle': ['wig'],
    'wig': ['wig'],
    'xls': ['xls'],                             # database
    'xlsx': ['xlsx'],                           # database
    'xmfa': ['xmfa'],
    'yaml': ['yaml', 'YAML']                    # database


}

extensions = AttrDict(**extensions)
