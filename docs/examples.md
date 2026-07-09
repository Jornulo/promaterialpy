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
print(material_data.describe())

# Check for missing values in specification fields
print("\nMissing values:")
print(material_data.isnull().sum())

```

### Example 2: Analyzing Fiber-Reinforced Composite Manufacturing Parameters

Load the physics-inspired regression dataset to evaluate how ultimate tensile strength ($MPa$) behaves across different composite matrices (glass, carbon, aramid, basalt).

```python

import promaterialpy as pmp

# Load the compounds manufacturing parameters dataset
composites_df = pmp.load_dataset("compounds")

# Quick preview of manufacturing factors and tensile outputs
print(composites_df.head())
print(f"\nDataset shape: {composites_df.shape}")
print(f"\nTracked variables: {list(composites_df.columns)}")

```

### Example 3: Cataloging Available Engineering Corpora

Quickly query and print all materials datasets currently registered within the ecosystem.

```python

import promaterialpy as pmp

# Retrieve and display the sorted list of engineering identifiers
datasets = pmp.list_datasets()
print("Available materials datasets:")
print(datasets)

```