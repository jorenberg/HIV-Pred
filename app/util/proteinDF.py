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
    
    def parse_pdb(self):
        """
        Parses the PDB file as a pandas DataFrame object.
        -------------------------------------------------
        Backbone chain atoms are ignored for the calculation of interacting residues.
        """
        atomic_data = []
        with open(self.pdb_handle, 'r') as f:
            for line in f.readlines():
                data = dict()
                if line[0:4] == 'ATOM':
                    # Retrieving the atomic data.
                    data['Record name'] = line[0:5].strip(' ')
                    data['serial_number'] = int(line[6:11].strip(' '))
                    data['atom'] = line[12:15].strip(' ')
                    data['resi_name'] = line[17:20]
                    data['chain_id'] = line[21]
                    data['resi_num'] = int(line[23:26])
                    data['x'] = float(line[30:37])
                    data['y'] = float(line[38:45])
                    data['z'] = float(line[46:53])
                    atomic_data.append(data)
        atomic_df = pd.DataFrame(atomic_data)
        
        return atomic_d
