from setuptools import find_packages, setup

setup(
    name="job_runner",
    packages=find_packages(exclude=["job_runner_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
