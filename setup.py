import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

with open("VERSION", "r") as v:
    version = v.read()

setuptools.setup(
    name="Synthetic Root Generator",
    version=version,
    author="James Bristow",
    author_email="james.bristow@plantandfood.co.nz",
    description="Synthetic root generator for apple tree modelling.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PlantandFoodResearch/synthetic-root-generator",
    packages=['synthetic_root_generator'],
    python_requires='>=3.9',
)