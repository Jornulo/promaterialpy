"""
Datasets registry for promaterialpy.
"""
DATASETS = {
    "commercial_regulations": {
        "filename": "promaterial_commercial_regulations.csv",
        "Original name": "Data.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "description": "It contains detailed specifications, heat treatments, and standards (ANSI, DIN, ISO, GOST)."
    },

    "commercial_properties": {
        "filename": "promaterial_commercial_properties.csv",
        "Original name": "material.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "description": "It contains the fundamental elastic properties (including Poisson's ratio and density) for direct mechanical calculations."
    },

    "pure_metals": {
        "filename": "promaterial_pure_metals.csv",
        "Original name": "youngs_modulus.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/kanchana1990/youngs-modulus-of-metals?select=youngs_modulus.csv",
        "License": "Open Data Commons Attribution License (ODC-By) v1.0",
        "description": "A scientific reference dataset containing Young's modulus (in GPa) for 50 pure metals from the periodic table, identified by name and chemical symbol. It serves as a baseline for elemental comparison and is useful for pure physics simulations requiring an assessment of the elements' intrinsic stiffness range—spanning from 1.7 GPa for cesium to 447 GPa for ruthenium—prior to alloying."
    },

    "compounds": {
        "filename": "promaterial_compounds.csv",
        "Original name": "composite_material_strength.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/meruvakodandasuraj/composite-material-tensile-strength-dataset",
        "License": "CC0: Public Domain",
        "description": "A materials-physics-inspired regression dataset that models the mechanical behavior of fiber-reinforced composites (glass, carbon, aramid, basalt) with resin matrices. It includes critical manufacturing variables such as fiber volume fraction, curing temperature, and void content (defects). It is ideal for implementing predictive or optimization functions, simulating how manufacturing parameters affect ultimate tensile strength (in MPa) without the need for actual destructive testing."
    }
}

__all__ = ["DATASETS"]