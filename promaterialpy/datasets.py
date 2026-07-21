"""
Datasets registry for promaterialpy.
"""
DATASETS = {
    "commercial_regulations": {
        "Filename": "commercial_regulations.csv",
        "Original name": "Data.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "Description": "It contains detailed specifications, heat treatments, and standards (ANSI, DIN, ISO, GOST)."
    },

    "commercial_properties": {
        "Filename": "commercial_properties.csv",
        "Original name": "material.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/purushottamnawale/materials",
        "License": "MIT",
        "Description": "It contains the fundamental elastic properties (including Poisson's ratio and density) for direct mechanical calculations."
    },

    "pure_metals": {
        "Filename": "pure_metals.csv",
        "Original name": "youngs_modulus.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/kanchana1990/youngs-modulus-of-metals?select=youngs_modulus.csv",
        "License": "Open Data Commons Attribution License (ODC-By) v1.0",
        "Description": "A scientific reference dataset containing Young's modulus (in GPa) for 50 pure metals from the periodic table, identified by name and chemical symbol. It serves as a baseline for elemental comparison and is useful for pure physics simulations requiring an assessment of the elements' intrinsic stiffness range—spanning from 1.7 GPa for cesium to 447 GPa for ruthenium—prior to alloying."
    },

    "composite_material_strength": {
        "Filename": "composite_material_strength.csv",
        "Original name": "composite_material_strength.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/meruvakodandasuraj/composite-material-tensile-strength-dataset",
        "License": "CC0: Public Domain",
        "Description": "A materials-physics-inspired regression dataset that models the mechanical behavior of fiber-reinforced composites (glass, carbon, aramid, basalt) with resin matrices. It includes critical manufacturing variables such as fiber volume fraction, curing temperature, and void content (defects). It is ideal for implementing predictive or optimization functions, simulating how manufacturing parameters affect ultimate tensile strength (in MPa) without the need for actual destructive testing."
    },

    "steel_fatigue": {
        "Filename": "steel_fatigue.csv",
        "Original name": "Steel Fatigue Strength Prediction",
        "Source": "Kaggle / National Institute for Materials Science (NIMS)",
        "URL": "https://www.kaggle.com/datasets/chaozhuang/steel-fatigue-strength-prediction",
        "License": "Apache 2.0",
        "Description": "Experimental dataset tracking steel chemical composition (%C, %Si, %Mn, %Ni, %Cr), heat treatment conditions (normalizing, hardening, tempering temperatures), and mechanical outcomes to predict rotating bending fatigue strength (10^7 cycles)."
    },

    "concrete_strength": {
        "Filename": "concrete_strength.csv",
        "Original name": "Concrete Data",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/zain280/concrete-data",
        "License": "Apache 2.0",
        "Description": "A classic civil engineering dataset containing concrete mixture compositions (cement, water, fly ash, slag, superplasticizer) and specimen age to predict compressive strength (in MPa)."
    },

    "glass_classification": {
        "Filename": "glass_classification.csv",
        "Original name": "Glass Dataset",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/hiteshyadavx/glass-dataset",
        "License": "CC0: Public Domain",
        "Description": "An enhanced materials science dataset containing chemical composition oxide ratios (RI, Na, Mg, Al, Si, K) and engineered interaction features to classify distinct types of engineered glass."
    },
    
    "crystal_properties": {
        "Filename": "crystal_properties.csv",
        "Original name": "Crystal Thermal Properties Dataset",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ziya07/crystal-thermal-properties-dataset",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive thermodynamic and physical dataset containing over 1,000 crystal structures, lattice parameters, and symmetry features to predict thermal conductivity, specific heat, entropy, and dielectric functions."
    },

    "predictive_maintenance": {
        "Filename": "predictive_maintenance.csv",
        "Original name": "Machine Predictive Maintenance Classification",
        "Source": "Kaggle / UCI Machine Learning",
        "URL": "https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification",
        "License": "CC0: Public Domain",
        "Description": "An industrial engineering dataset reflecting real-world predictive maintenance metrics (rotational speed, torque, tool wear, thermal dynamics) to classify machine failure states and failure modes."
    },

    "mineral_hardness": {
        "Filename": "mineral_hardness.csv",
        "Original name": "Mineral_Dataset_Supplementary_Info.csv",
        "Source": "Kaggle / Vanderbilt University",
        "URL": "https://www.kaggle.com/datasets/jocelyndumlao/prediction-of-mohs-hardness-with-machine-learning",
        "License": "CC0: Public Domain",
        "Description": "A compositional dataset featuring 622 naturally occurring minerals with 11 atomic descriptors (electronegativity, valence electrons, atomic radii) to predict experimental Mohs hardness."
    },

    "crystal_hardness": {
        "Filename": "crystal_hardness.csv",
        "Original name": "Artificial_Crystals_Dataset.csv",
        "Source": "Kaggle / Vanderbilt University",
        "URL": "https://www.kaggle.com/datasets/jocelyndumlao/prediction-of-mohs-hardness-with-machine-learning",
        "License": "CC0: Public Domain",
        "Description": "An independent validation dataset containing 51 synthetic single crystal structures and atomic properties to benchmark predictive models for Mohs hardness."
    },

    "fdm_3d_printing": {
        "Filename": "fdm_3d_printing.csv",
        "Original name": "FDM_Dataset.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ziya07/fdm-3d-printed-composite-material-prediction-data",
        "License": "CC0: Public Domain",
        "Description": "A manufacturing and mechanical testing dataset for Fused Deposition Modeling (FDM) 3D printing. It tracks process parameters (layer height, infill density, patterns, speeds, and temperatures) along with destructive testing load rates to predict the mechanical behavior, quality, and dynamic strength of composite and pure polymer components."
    },

    "3d_printer_plastics": {
        "Filename": "3d_printer_plastics.csv",
        "Original name": "3D_Printer_Plastics.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/sourceduty/3d-printer-plastics-2024",
        "License": "CC0: Public Domain",
        "Description": "A materials selection dataset containing physical, thermal, and qualitative mechanical properties for the top 25 types of 3D printing filaments. It covers melting points, flexibility, tensile strength levels, and industrial applications ranging from general prototyping to biocompatible medical implants."
    },

    "nasa_battery_degradation": {
        "Filename": "nasa_battery_degradation.csv",
        "Original name": "battery_cycle_level_dataset_CLEAN_FINAL.csv",
        "Source": "Kaggle / NASA Ames PCoE",
        "URL": "https://www.kaggle.com/datasets/yashxss/nasa-battery-cycle-level-dataset",
        "License": "Apache 2.0",
        "Description": "A gold-standard experimental battery aging dataset from the NASA Ames Prognostics Center of Excellence. It contains consolidated, cycle-level laboratory testing telemetry for Lithium-ion cells, tracking voltage, operating temperature, and capacity fade to model State of Health (SoH) and Remaining Useful Life (RUL)."
    },

    "industrial_iot_faults": {
        "Filename": "industrial_iot_faults.csv",
        "Original name": "industrial_fault_detection_data_1000.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ziya07/industrial-iot-fault-detection-dataset",
        "License": "CC0: Public Domain",
        "Description": "An industrial IoT telemetry dataset capturing real-time machine health metrics. It logs vibration velocity, casing temperature, and hydraulic/pneumatic pressure across automated systems, providing target labels for diagnosing bearing failures and mechanical overheating anomalies."
    },

    "conveyor_faults": {
        "Filename": "conveyor_faults.csv",
        "Original name": "conveyor_fault_dataset.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ziya07/operational-conveyor-fault-dataset",
        "License": "CC0: Public Domain",
        "Description": "An electromechanical fault dataset from an industrial conveyor belt system. It captures the direct relationship between mechanical stress variables (speed, load, vibration) and electrical response (motor current draw) across six distinct failure modes like belt slippage and pulley faults."
    },

    "aerospace_structural_design": {
        "Filename": "aerospace_structural_design.csv",
        "Original name": "aerospace_structural_design_dataset.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ziya07/aerospace-structural-design-dataset",
        "License": "CC0: Public Domain",
        "Description": "A comprehensive structural engineering dataset for aerospace vehicle optimization. It maps physical material properties (such as Young's modulus and Poisson's ratio) and multi-scale aircraft geometric parameters against high-altitude environmental stress variables to evaluate structural integrity and vibration damping."
    },

    "turbine_efficiency": {
        "Filename": "turbine_efficiency.csv",
        "Original name": "Data.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/ishank2005/wind-turbines-data-csv",
        "License": "MIT",
        "Description": "A thermodynamic power plant dataset from a Combined Cycle Power Plant (CCPP). It models the relationship between environmental ambient variables (temperature, pressure, humidity) and turbine vacuum states to predict the net hourly electrical energy output of the generation system."
    },

    "solar_generation": {
        "Filename": "solar_generation.csv",
        "Original name": "solar_plant_generation_dataset.csv",
        "Source": "Kaggle",
        "URL": "https://www.kaggle.com/datasets/juanschafle/solarplant-power-generation-monitoring-2023-2025",
        "License": "MIT",
        "Description": "An operational and environmental time-series dataset from a solar photovoltaic (PV) power plant. It logs hourly atmospheric conditions, panel surface temperatures, and irradiance measurements to track plant performance and support power output forecasting."
    },

    "building_energy": {
        "Filename": "building_energy.csv",
        "Original name": "energy_efficiency_data.csv",
        "Source": "Kaggle / UCI Machine Learning",
        "URL": "ttps://www.kaggle.com/datasets/ujjwalchowdhury/energy-efficiency-data-set",
        "License": "CC0: Public Domain",
        "Description": "A thermodynamic simulation dataset tracking the heating and cooling load requirements of 12 distinct building geometries. It evaluates how structural parameters, dimensions, and glazing properties dictate energy consumption."
    },
}

__all__ = ["DATASETS"]