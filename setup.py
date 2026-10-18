from setuptools import find_packages, setup

setup(
    name="coa-rl-paper-code",
    version="1.0.0",
    description="Single-instance CoA-RL and comparison methods for MRTA",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "coa_rl_mrta": ["models/*.pt", "models/*.pth"],
        "coa_rl_mrta.baselines.rca_rl": ["SOURCE.md", "THIRD_PARTY_LICENSE"],
    },
    license_files=["LICENSE"],
    python_requires=">=3.7",
    install_requires=["numpy>=1.21", "scipy>=1.7", "torch>=1.10"],
    license="Apache-2.0",
)
