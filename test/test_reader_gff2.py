from bioconvert import bioconvert_data
from bioconvert.readers.gff2 import Gff2

import pytest


expected_values = [{'seqid': 'chr1', 'source': 'processed_transcript', 'type': 'exon', 'start': 11869, 'stop': 12227, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000456328', 'exon_number': '1', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-002', 'exon_id': 'ENSE00002234944'}}
, {'seqid': 'chr1', 'source': 'processed_transcript', 'type': 'exon', 'start': 12613, 'stop': 12721, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000456328', 'exon_number': '2', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-002', 'exon_id': 'ENSE00003582793'}}
, {'seqid': 'chr1', 'source': 'processed_transcript', 'type': 'exon', 'start': 13221, 'stop': 14409, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000456328', 'exon_number': '3', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-002', 'exon_id': 'ENSE00002312635'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 11872, 'stop': 12227, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000515242', 'exon_number': '1', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-201', 'exon_id': 'ENSE00002234632'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12613, 'stop': 12721, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000515242', 'exon_number': '2', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-201', 'exon_id': 'ENSE00003608237'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 13225, 'stop': 14412, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000515242', 'exon_number': '3', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-201', 'exon_id': 'ENSE00002306041'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 11874, 'stop': 12227, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000518655', 'exon_number': '1', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-202', 'exon_id': 'ENSE00002269724'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12595, 'stop': 12721, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000518655', 'exon_number': '2', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-202', 'exon_id': 'ENSE00002270865'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 13403, 'stop': 13655, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000518655', 'exon_number': '3', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-202', 'exon_id': 'ENSE00002216795'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 13661, 'stop': 14409, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000518655', 'exon_number': '4', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-202', 'exon_id': 'ENSE00002303382'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12010, 'stop': 12057, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '1', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001948541'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12179, 'stop': 12227, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '2', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001671638'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12613, 'stop': 12697, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '3', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001758273'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 12975, 'stop': 13052, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '4', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001799933'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 13221, 'stop': 13374, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '5', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001746346'}}
, {'seqid': 'chr1', 'source': 'transcribed_unprocessed_pseudogene', 'type': 'exon', 'start': 13453, 'stop': 13670, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000223972', 'transcript_id': 'ENST00000450305', 'exon_number': '6', 'gene_name': 'DDX11L1', 'gene_biotype': 'pseudogene', 'transcript_name': 'DDX11L1-001', 'exon_id': 'ENSE00001863096'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 29321, 'stop': 29370, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '1', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001718035'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 24738, 'stop': 24891, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '2', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00003624050'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 18268, 'stop': 18379, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '3', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001642865'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17915, 'stop': 18061, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '4', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00003638984'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17602, 'stop': 17742, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '5', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001699689'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17233, 'stop': 17364, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '6', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001656010'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16854, 'stop': 17055, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '7', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001760358'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16607, 'stop': 16765, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '8', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00003618297'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15904, 'stop': 15947, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '9', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001375216'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15796, 'stop': 15901, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '10', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00001388009'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14970, 'stop': 15038, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '11', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00003497546'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14363, 'stop': 14829, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000438504', 'exon_number': '12', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-202', 'exon_id': 'ENSE00003511598'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 24734, 'stop': 24886, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '1', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00002254515'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 18268, 'stop': 18369, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '2', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00002303227'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17915, 'stop': 18061, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '3', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00003638984'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17606, 'stop': 17742, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '4', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00003629019'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17498, 'stop': 17504, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '5', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00002285713'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17233, 'stop': 17364, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '6', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00001656010'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16854, 'stop': 17055, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '7', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00001760358'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14970, 'stop': 15038, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '8', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00003497546'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14363, 'stop': 14829, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000541675', 'exon_number': '9', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-204', 'exon_id': 'ENSE00003511598'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 29321, 'stop': 29370, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '1', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00001718035'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 24738, 'stop': 24891, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '2', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003603734'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17915, 'stop': 18061, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '3', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003513603'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17606, 'stop': 17742, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '4', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003565315'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17233, 'stop': 17368, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '5', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003685767'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16858, 'stop': 17055, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '6', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003553898'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16607, 'stop': 16765, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '7', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003621279'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15796, 'stop': 15947, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '8', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00002030414'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14970, 'stop': 15038, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '9', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003591210'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14363, 'stop': 14829, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000423562', 'exon_number': '10', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-201', 'exon_id': 'ENSE00003693168'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 29534, 'stop': 29570, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '1', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00001890219'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 24738, 'stop': 24891, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '2', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003507205'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 18268, 'stop': 18366, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '3', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003477500'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17915, 'stop': 18061, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '4', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003565697'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17606, 'stop': 17742, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '5', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003475637'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17233, 'stop': 17368, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '6', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003502542'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16858, 'stop': 17055, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '7', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003553898'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16607, 'stop': 16765, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '8', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00003621279'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15796, 'stop': 15947, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '9', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00002030414'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15005, 'stop': 15038, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '10', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00001935574'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14404, 'stop': 14501, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000488147', 'exon_number': '11', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-001', 'exon_id': 'ENSE00001843071'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 29534, 'stop': 29806, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '1', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00001378845'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 24737, 'stop': 24891, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '2', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00002317443'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 18268, 'stop': 18366, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '3', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00003682243'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17915, 'stop': 18061, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '4', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00003638984'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17602, 'stop': 17742, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '5', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00001699689'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 17233, 'stop': 17364, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '6', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00001656010'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16858, 'stop': 17055, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '7', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00003632482'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16748, 'stop': 16765, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '8', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00002275850'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 16607, 'stop': 16745, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '9', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00002241734'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15904, 'stop': 15947, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '10', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00001375216'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15796, 'stop': 15901, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '11', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00001388009'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 15000, 'stop': 15038, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '12', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00002215305'}}
, {'seqid': 'chr1', 'source': 'unprocessed_pseudogene', 'type': 'exon', 'start': 14411, 'stop': 14502, 'strand': '-', 'attributes': {'gene_id': 'ENSG00000227232', 'transcript_id': 'ENST00000538476', 'exon_number': '13', 'gene_name': 'WASH7P', 'gene_biotype': 'pseudogene', 'transcript_name': 'WASH7P-203', 'exon_id': 'ENSE00002295553'}}
, {'seqid': 'chr1', 'source': 'lincRNA', 'type': 'exon', 'start': 29554, 'stop': 30039, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000473358', 'exon_number': '1', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-001', 'exon_id': 'ENSE00001947070'}}
, {'seqid': 'chr1', 'source': 'lincRNA', 'type': 'exon', 'start': 30564, 'stop': 30667, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000473358', 'exon_number': '2', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-001', 'exon_id': 'ENSE00001922571'}}
, {'seqid': 'chr1', 'source': 'lincRNA', 'type': 'exon', 'start': 30976, 'stop': 31097, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000473358', 'exon_number': '3', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-001', 'exon_id': 'ENSE00001827679'}}
, {'seqid': 'chr1', 'source': 'lincRNA', 'type': 'exon', 'start': 30267, 'stop': 30667, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000469289', 'exon_number': '1', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-002', 'exon_id': 'ENSE00001841699'}}
, {'seqid': 'chr1', 'source': 'lincRNA', 'type': 'exon', 'start': 30976, 'stop': 31109, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000469289', 'exon_number': '2', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-002', 'exon_id': 'ENSE00001890064'}}
, {'seqid': 'chr1', 'source': 'miRNA', 'type': 'exon', 'start': 30366, 'stop': 30503, 'strand': '+', 'attributes': {'gene_id': 'ENSG00000243485', 'transcript_id': 'ENST00000607096', 'exon_number': '1', 'gene_name': 'MIR1302-11', 'gene_biotype': 'lincRNA', 'transcript_name': 'MIR1302-11-201', 'exon_id': 'ENSE00003695741'}}]


def test_load():
    infile = bioconvert_data("GFF2/gff2_example.gff")
    reader_gff2 = Gff2(infile)

    for expected_value, file_value in zip(expected_values, reader_gff2.read()):
        assert expected_value == file_value

