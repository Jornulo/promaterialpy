from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="promaterialpy",
    version="0.1.0",
    author="Jorge Rolando Aarón Núñez López",
    author_email="jorgearon1905@gmail.com",
    description=(
        "A curated collection of mechanical, structural, and materials engineering datasets "
        "for mechanical-electrical design, computational modeling, and research. "
        "Includes standard commercial specifications, international design codes (ANSI, DIN, ISO, GOST), "
        "heat treatment metadata, pure element stiffness profiles, and fiber-reinforced composite "
        "manufacturing parameters from physics-inspired simulation and industrial databases."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jornulo/promaterialpy",
    project_urls={
        "Bug Tracker": "https://github.com/Jornulo/promaterialpy/issues",
        "Documentation": "https://github.com/Jornulo/promaterialpy",
        "Source Code": "https://github.com/Jornulo/promaterialpy",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "promaterialpy": [
            "data/*.csv",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        
        # Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Topics
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        
        # Python Versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        
        # OS
        "Operating System :: OS Independent",
        
        # Language
        "Natural Language :: English",
    ],
    keywords=(
        "materials, engineering, mechanical, electrical, structural, materials science, "
        "datasets, youngs modulus, elastic parameters, poisson ratio, yield strength, "
        "tensile strength, hardness, steel, alloy, composite materials, manufacturing, "
        "simulation, standard standards, ansi, din, iso, data science, research"
    ),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    license="MIT",
    zip_safe=False,
)