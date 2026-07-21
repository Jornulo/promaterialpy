# promaterialpy – Examples

This page provides practical examples of using `promaterialpy` for materials data analysis, mechanical calculations, and exploration.

## Basic Examples

### Example 1: Loading and Exploring Mechanical Properties

Learn how to load a dataset containing structural parameters and perform a basic exploratory data analysis (EDA) before setting up a simulation.

```python
import promaterialpy as pmp

# Load fundamental elastic properties optimized for direct mechanical calculations
material_data = pmp.load_dataset("commercial_properties")

# Display first few rows (e.g., Young's Modulus, Poisson's ratio, Density)
print(material_data.head())

# Check dataset shape (number of materials vs. properties tracked)
print(f"\nDataset shape: {material_data.shape}")

# View property column names
print(f"\nColumns: {list(material_data.columns)}")

# Get summary statistics (mean stiffness, minimum yield strength, etc.)
print("\nSummary statistics:")
print(material_data.describe_dataset())

# Check for missing values in specification fields
print("\nMissing values:")
print(material_data.isnull().sum())

```

### Example 2: Analyzing Fiber-Reinforced Composite Manufacturing Parameters

Load the physics-inspired regression dataset to evaluate how ultimate tensile strength (MPa) behaves across different composite matrices (glass, carbon, aramid, basalt).

```python

import promaterialpy as pmp

# Load the composite_material_strength manufacturing parameters dataset
composites_df = pmp.load_dataset("composite_material_strength")

# Quick preview of manufacturing factors and tensile outputs
print(composites_df.head())
print(f"\nDataset shape: {composites_df.shape}")
print(f"\nTracked variables: {list(composites_df.columns)}")

```

### Example 3: Correlating Photovoltaic Efficiency and Thermal De-rating

Load the solar generation dataset to analyze how solar irradiance and thermal stressors (ambient vs. panel surface temperature) impact the net power generation output.

```python

import promaterialpy as pmp

# Load the clean hourly solar power generation time-series
solar_df = pmp.load_dataset("solar_generation")

# Preview the environmental and power columns
print(solar_df.head())

# Filter data to analyze high-irradiance peaks (greater than 800 W/m²)
peak_solar = solar_df[solar_df['solar_irradiance_wm2'] > 800]

# Calculate the thermal delta (Panel Temperature minus Ambient Temperature)
peak_solar['thermal_delta'] = peak_solar['panel_temperature_c'] - peak_solar['ambient_temperature_c']

# Display relevant vectors for cooling and efficiency analysis
print("\nPeak solar operational states:")
print(peak_solar[['solar_irradiance_wm2', 'thermal_delta', 'power_generation_kw']].head())

```