# trying-out-pytest
Stuff for learning about pytest for CSCI 5802, software testing, at the University of Minnesota


# Setup instructions
1. Clone the repository using `git clone`
2. Create a python virtual environment, run this command in the cloned `trying-out-pytest` directory: `python -m venv myenv`
3. Activate the virtual environment, run this in your terminal: `.\myenv\Scripts\activate`
    - You should see something similar to: `(myenv) PS C:\trying-out-pytest>` with the (myenv) prepending the path
4. Install pytest in your environment: `pip install pytest` in the terminal.
5. To use pytest's coverage metrics, install a plugin: run `pip install pytest-cov` in the terminal.

Setup is complete! If you want to deactivate the environment type `deactivate` in your shell.


# Usage
Various tests are located in the `tests/` directory.

1. To run all tests, run `pytest tests/` in a terminal.
    - Here's how you can run a certain file: `pytest tests/test_calculator.py`
    - And to run a certain test in a test file: `pytest tests/test_calculator.py::test_add`
2. To run pytest coverage, run `pytest tests/ --cov`