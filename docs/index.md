# promaterialpy Documentation

## Welcome

The `promaterialpy` package provides a curated collection of mechanical, structural, and materials engineering datasets for data analysis, statistical modeling, and machine learning research in Python. It includes datasets related to **standard commercial specifications, international design codes (ANSI, DIN, ISO, GOST), heat treatment metadata, pure element stiffness profiles, and fiber-reinforced composite manufacturing parameters**.

The package contains data optimized for mechanical-electrical design, allowing users to analyze fundamental elastic properties, evaluate chemical element baselines prior to alloying, and simulate physics-inspired behavior of fiber-reinforced composites (glass, carbon, aramid, and basalt) under different manufacturing conditions such as curing temperatures and void content defects without needing destructive physical testing.

### Philosophy

The author's vision is to create **specialized dataset packages** focused on specific themes and topics. Instead of searching through multiple generic data repositories to find relevant datasets, users can go directly to a thematic package where all datasets are carefully curated around a particular engineering subject.

In the case of `promaterialpy`, every dataset is **exclusively focused on mechanical, structural, and materials science research**, making it the go-to resource for engineers, researchers, data scientists, metallurgists, and students working in the fields of mechanical engineering, electrical design, manufacturing automation, and advanced materials optimization.


## Getting Started

### Installation

#### From PyPI (Recommended)

The easiest way to install `promaterialpy` is directly from PyPI:
```bash
pip install promaterialpy
```

#### From GitHub (Latest Development Version)

To get the latest development version with the newest features and bug fixes:
```bash
pip install git+https://github.com/Jorbulo/promaterialpy
```

### Quick Start Tutorial

#### 1. Import the Package
```python
import promaterialpy as pmp
```

#### 2. List Available Datasets

See all datasets included in the package:
```python
# Get list of all datasets
datasets = pmp.list_datasets()
print(datasets)
```

#### 3. Load a Dataset

Load any dataset as a pandas DataFrame:
```python
# Load commercial_properties
df = pmp.load_dataset('commercial_properties')

# Display first rows
print(df.head())

# Check dataset dimensions
print(f"Shape: {df.shape}")
```

#### 4. Describe a dataset

```python

# Describe a dataset
print(pmp.describe("commercial_properties"))

```

### Basic Concepts

#### Dataset Naming Convention

All dataset names in `promaterialpy` follow a consistent naming pattern:

- Lowercase with underscores: `commercial_properties`
- Descriptive names that reflect content


#### Some Datasets available at `promaterialpy`

Every dataset is **exclusively focused on legal, criminal justice, and political topics for
data analysis, statistical modeling, and machine learning**:

- **commercial_regulations**: Contains detailed specifications, heat treatments, and international standards (ANSI, DIN, ISO, GOST) for standard design materials.
- **commercial_properties**: Includes fundamental elastic properties (such as Young's modulus, shear modulus, Poisson's ratio, and density) optimized for direct mechanical calculations.
- **pure_metals**: A scientific reference dataset recording the Young's modulus (in GPa) for 50 pure metals from the periodic table, providing an elemental baseline of stiffness.
- **composite_material_strength**: A physics-inspired regression dataset modeling the ultimate tensile strength (in MPa) of fiber-reinforced composites (glass, carbon, aramid, basalt) based on manufacturing parameters.

> **Disclaimer:** The datasets included in `promaterialpy` are provided strictly for educational, research, and informational purposes. For safety-critical engineering, formal structural certifications, or certified manufacturing specifications, always consult a licensed and qualified Professional Engineer.


#### Data Licenses

All datasets are sourced from open industrial databases and public research repositories,
maintaining their original open-source licenses:

- **MIT License** for the commercial specifications and structural properties datasets.

- **Open Data Commons Attribution License (ODC-By) v1.0** for the pure metals stiffness profile dataset.

- **CC0: Public Domain** for the fiber-reinforced composites manufacturing dataset.

- The `promaterialpy` package itself is licensed under the MIT License.