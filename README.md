# `mms-data-pipeline`

## Set Up

We use a combination of conda, poetry and pip to manage our environment as per <https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry/>

### Installation steps

1. Install `miniforge` and `poetry`

```bash
brew install miniforge
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install Python

```bash
conda env update --file environment.yml
```

3. Generate pyright config

```bash
./scripts/gen_pyright_config.sh
```

4. Update pyright config to include custom typings

## Package structure (generated through ChatGPT prompt)

```shell
your_package_name/
│
├── __init__.py
├── pipeline/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── steps/
│   │   ├── __init__.py
│   │   ├── step1.py
│   │   ├── step2.py
│   │   └── ...
│   └── utils/
│       ├── __init__.py
│       ├── data.py
│       ├── logging.py
│       └── ...
└── tests/
    ├── __init__.py
    ├── test_pipeline.py
    ├── test_step1.py
    ├── test_step2.py
    └── ...
```

Here's what each of the files and directories do:

    `bnirs_pipeline/`: This is the main directory for the package.

    `__init__.py`: This file tells Python that the directory should be treated as a package.

    `pipeline/`: This is a directory that will contain the code for your data pipeline.

    `__init__.py`: This file tells Python that the pipeline/ directory should be treated as a package.

    `pipeline.py`: This is the main file for your pipeline package. It should define a Pipeline class that coordinates the execution of the pipeline steps.

    `steps/`: This is a directory that will contain the code for the individual steps of your pipeline.

    `__init__.py`: This file tells Python that the steps/ directory should be treated as a package.

    `step1.py`, `step2.py`, etc.: These are files that define the individual steps of your pipeline. Each step should define a class that implements a run method.

    `utils/`: This is a directory that will contain utility code for your pipeline.

    `__init__.py`: This file tells Python that the utils/ directory should be treated as a package.

    `data.py`, `logging.py`, etc.: These are files that contain utility functions for your pipeline.

    `tests/`: This is a directory that will contain the tests for your pipeline.

    `__init__.py`: This file tells Python that the tests/ directory should be treated as a package.

    `test_pipeline.py`, `test_step1.py`, `test_step2.py`, etc.: These are files that define tests for your pipeline and its steps.
