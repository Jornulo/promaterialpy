"""
Basic usage example for promaterialpy

Run:
    python basic_usage.py
"""

import promaterialpy as pmp

print("=== promaterialpy: Basic Usage Example ===\n")

# List all available datasets
print("Available datasets in promaterialpy:")
print(pmp.list_datasets())

# Describe a dataset
print("\nDataset description for 'pure_metals':")
print(pmp.describe("pure_metals"))

# Load a dataset
print("\nLoading 'pure_metals' dataset...")
metals_df = pmp.load_dataset("pure_metals")

# Show basic information
print("\nFirst 5 rows of pure_metals:")
print(metals_df.head())

print("\nDataset shape:")
print(metals_df.shape)

print("\nColumn names:")
print(list(metals_df.columns))

# Load another dataset (Structural engineering example)
print("\nLoading 'concrete_strength' dataset...")
concrete_df = pmp.load_dataset("concrete_strength")

print("\nFirst 5 rows of concrete_strength:")
print(concrete_df.head())

print("\nDone.")