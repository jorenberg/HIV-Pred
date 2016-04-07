#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = 'Prabhat Kumar, prabhat.genome@gmail.com'

class ProteinDataFrame(object):
    """Doc string for Protein Data Frame."""
    def __init__(self, handle):
        super(ProteinDataFrame, self).__init__()
        self.handle = handle
        self.protein_df = self.parse_pdb()
        self.alpha_carbons = self.extract_alpha_carbons()
