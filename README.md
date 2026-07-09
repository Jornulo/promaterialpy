# promaterialpy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The `promaterialpy` package provides a curated collection of mechanical, structural, and materials engineering datasets for mechanical-electrical design, computational modeling, and research. Includes standard commercial specifications, international design codes (ANSI, DIN, ISO, GOST), heat treatment metadata, pure element stiffness profiles, and fiber-reinforced composite manufacturing parameters from physics-inspired simulation and industrial databases.

## Installation
You can install the `promaterialpy` package from PyPI:
```bash
pip install promaterialpy
```

## Usage
```python

import promaterialpy as pmp

# List all available datasets
datasets = pmp.list_datasets()
print(datasets)

# Load a specific dataset
df = pmp.load_dataset('commercial_properties')
print(df.head())

# Describe dataset
df_01 = pmp.describe('compounds')
print(df_01)

```

## 📊 Some Available Datasets

| Dataset | Description | 
|---------|-------------|
| `commercial_normas` | Contains detailed specifications, heat treatments, and international standards (ANSI, DIN, ISO, GOST) for standard design materials.| 
| `commercial_properties` | Includes fundamental elastic properties (such as Young's modulus $E$, shear modulus $G$, Poisson's ratio, and density) optimized for direct mechanical calculations.| 
| `pure_metals` | A scientific reference dataset recording the Young's modulus (in GPa) for 50 pure metals from the periodic table, providing an elemental baseline of stiffness.| 
| `compounds` | A physics-inspired regression dataset modeling the ultimate tensile strength (in MPa) of fiber-reinforced composites (glass, carbon, aramid, basalt) based on manufacturing parameters.|

> Run `promaterialpy.list_datasets()` or `pmp.list_datasets()` (using `pmp` as alias) to see the full list of available datasets.

## Disclaimer

The datasets included in `promaterialpy` are provided strictly for educational, research, and informational purposes. All datasets originate from open-source industrial databases and public research repositories, retaining their original licenses and attributions.

The author of `promaterialpy` makes no warranties, express or implied, regarding the accuracy, completeness, or suitability of any dataset for a particular structural, mechanical, or engineering purpose. Users are solely responsible for ensuring that their simulations, engineering designs, and use of these datasets comply with applicable industry codes, safety standards, and local regulations.

Any findings, calculations, structural failure analyses, or engineering decisions derived from the use of these datasets are the sole responsibility of the user. The author shall not be held liable for any direct, indirect, incidental, or consequential damages (including, but not limited to, mechanical component failures, structural hazards, or property damage) arising from the use or misuse of the datasets included in this library.

For safety-critical engineering, formal structural certifications, or certified manufacturing specifications, always consult a licensed and qualified Professional Engineer.


## License

The `promaterialpy` library is released under the **MIT License**, which allows free use, modification, distribution, and private use, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software. See the [LICENSE](LICENSE) file for details.