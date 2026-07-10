"""
Datasets registry for promaterialpy.
"""
DATASETS = {
    "commercial_regulations": {
        "filename": "commercial_regulations.csv",
        "Original name": "Data.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "description": "It contains detailed specifications, heat treatments, and standards (ANSI, DIN, ISO, GOST)."
    },

    "commercial_properties": {
        "filename": "commercial_properties.csv",
        "Original name": "material.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "description": "It contains the fundamental elastic properties (including Poisson's ratio and density) for direct mechanical calculations."
    },

    "pure_metals": {
        "filename": "pure_metals.csv",
        "Original name": "youngs_modulus.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/kanchana1990/youngs-modulus-of-metals?select=youngs_modulus.csv",
        "License": "Open Data Commons Attribution License (ODC-By) v1.0",
        "description": "A scientific reference dataset containing Young's modulus (in GPa) for 50 pure metals from the periodic table, identified by name and chemical symbol. It serves as a baseline for elemental comparison and is useful for pure physics simulations requiring an assessment of the elements' intrinsic stiffness range—spanning from 1.7 GPa for cesium to 447 GPa for ruthenium—prior to alloying."
    },

    "composite_material_strength": {
        "filename": "composite_material_strength.csv",
        "Original name": "composite_material_strength.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/meruvakodandasuraj/composite-material-tensile-strength-dataset",
        "License": "CC0: Public Domain",
        "description": "A materials-physics-inspired regression dataset that models the mechanical behavior of fiber-reinforced composites (glass, carbon, aramid, basalt) with resin matrices. It includes critical manufacturing variables such as fiber volume fraction, curing temperature, and void content (defects). It is ideal for implementing predictive or optimization functions, simulating how manufacturing parameters affect ultimate tensile strength (in MPa) without the need for actual destructive testing."
    },

    "steel_fatigue": {
        "Filename": "steel_fatigue.csv",
        "Original name": "Steel Fatigue Strength Prediction",
        "Source Repository": "Kaggle / National Institute for Materials Science (NIMS)",
        "License": "Apache 2.0",
        "Description": "Experimental dataset tracking steel chemical composition (%C, %Si, %Mn, %Ni, %Cr), heat treatment conditions (normalizing, hardening, tempering temperatures), and mechanical outcomes to predict rotating bending fatigue strength (10^7 cycles)."
    },

    "concrete_strength": {
        "Filename": "concrete_strength.csv",
        "Original name": "Concrete Data",
        "Source Repository": "Kaggle",
        "License": "Apache 2.0",
        "Description": "A classic civil engineering dataset containing concrete mixture compositions (cement, water, fly ash, slag, superplasticizer) and specimen age to predict compressive strength (in MPa)."
    },

    "glass_classification": {
        "Filename": "glass_classification.csv",
        "Original name": "Glass Dataset",
        "Source Repository": "Kaggle",
        "License": "CC0: Public Domain",
        "Description": "An enhanced materials science dataset containing chemical composition oxide ratios (RI, Na, Mg, Al, Si, K) and engineered interaction features to classify distinct types of engineered glass."
    },
    
    "crystal_properties": {
        "Filename": "crystal_properties.csv",
        "Original name": "Crystal Thermal Properties Dataset",
        "Source Repository": "Kaggle",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive thermodynamic and physical dataset containing over 1,000 crystal structures, lattice parameters, and symmetry features to predict thermal conductivity, specific heat, entropy, and dielectric functions."
    },

    "predictive_maintenance": {
        "Filename": "predictive_maintenance.csv",
        "Original name": "Machine Predictive Maintenance Classification",
        "Source Repository": "Kaggle / UCI Machine Learning Repository",
        "License": "CC0: Public Domain",
        "Description": "An industrial engineering dataset reflecting real-world predictive maintenance metrics (rotational speed, torque, tool wear, thermal dynamics) to classify machine failure states and failure modes."
    },

    "mineral_hardness": {
        "Filename": "mineral_hardness.csv",
        "Original name": "Mineral_Dataset_Supplementary_Info.csv",
        "Source Repository": "Kaggle / Vanderbilt University",
        "License": "CC0: Public Domain",
        "Description": "A compositional dataset featuring 622 naturally occurring minerals with 11 atomic descriptors (electronegativity, valence electrons, atomic radii) to predict experimental Mohs hardness."
    },
    "crystal_hardness": {
        "Filename": "crystal_hardness.csv",
        "Original name": "Artificial_Crystals_Dataset.csv",
        "Source Repository": "Kaggle / Vanderbilt University",
        "License": "CC0: Public Domain",
        "Description": "An independent validation dataset containing 51 synthetic single crystal structures and atomic properties to benchmark predictive models for Mohs hardness."
    },
}

__all__ = ["DATASETS"]