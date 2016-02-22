# HIV-Pred® [![Apache License](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/iamprabhat/HIV-Pred/blob/master/LICENSE)
**HIV-Pred®:** HIV (Human Immunodeficiency Virus) Resistance Phenotypes Prediction.

## About:
The **H**uman **I**mmunodeficiency **V**irus (HIV) is a lentivirus (a subgroup of retrovirus) that causes HIV infection and over time acquired immunodeficiency syndrome (AIDS). AIDS is a condition in humans in which progressive failure of the immune system allows life-threatening opportunistic infections and cancers to thrive. Without treatment, average survival time after infection with HIV is estimated to be 9 to 11 years, depending on the HIV subtype. Infection with HIV occurs by the transfer of blood, semen, vaginal fluid, pre-ejaculate, or breast milk. Within these bodily fluids, HIV is present as both free virus particles and virus within infected immune cells.

**HIV-Pred®, is a Machine Learning Model to predict HIV Resistance Phenotypes.**

### Mechanism:
HIV infects vital cells in the human immune system such as helper T cells (specifically CD4<sup>+</sup> T cells), macrophages, and dendritic cells. HIV infection leads to low levels of CD4<sup>+</sup> T cells through a number of mechanisms, including pyroptosis of abortively infected T cells, apoptosis of uninfected bystander cells, direct viral killing of infected cells, and killing of infected CD4<sup>+</sup> T cells by CD8 cytotoxic lymphocytes that recognize infected cells. When CD4<sup>+</sup> T cell numbers decline below a critical level, cell-mediated immunity is lost, and the body becomes progressively more susceptible to opportunistic infections.

### Project Overview:
- Machine Learning Algorithmic models implementation in R and Python to predict HIV resistance phenotypes.
- Python implementation for Molecular Weight and Isoelectronic Point Calculations.
- Building of Protein Data Frame (for storing data tables) using [Python](https://www.python.org/) – [Pandas](http://pandas.pydata.org/).
- Molecular Modeling of HIV Protease, using [RasMol](http://www.openrasmol.org/), [PyMol](https://www.pymol.org/) and [Discovery Studio Viewer](http://accelrys.com/).
- Structure Similarity by using – [PDBeFold](http://www.ebi.ac.uk/msd-srv/ssm/cgi-bin/ssmserver):
  - pairwise comparison and 3D alignment of protein structures,
  - multiple comparison and 3D alignment of protein structures,
  - examination of a protein structure for similarity with the whole PDB archive or SCOP archive, and
  - best C⍺-alignment of compared structures.
- Protein Structure Database Searching by [DaliLite](http://ekhidna.biocenter.helsinki.fi/dali_server/) v3.0.
