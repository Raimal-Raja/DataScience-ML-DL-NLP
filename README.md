# DataScience-ML-DL-NLP

Learning archive of Python, statistics, machine learning, deep learning, NLP, deployment, and project exercises.

## Setup and repository reference

### Project structure

- [10_Data_Analysis_with_Python](10_Data_Analysis_with_Python)
- [11_SqlLite](11_SqlLite)
- [12_logging_in_python](12_logging_in_python)
- [13_multi-threading and multi-processing](13_multi-threading%20and%20multi-processing)
- [14_Memory Allocation  and Memory Management](14_Memory%20Allocation%20%20and%20Memory%20Management)
- [15_Flask](15_Flask)
- [16_streamlit_app](16_streamlit_app)
- [17_statistics](17_statistics)
- [18_Probability](18_Probability)
- [19_Machine Learning](19_Machine%20Learning)
- [1_1.1 Basic_Python](1_1.1%20Basic_Python)
- [1_1.2 Array](1_1.2%20Array)
- [20_docker](20_docker)
- [22_End-to-End Projects](22_End-to-End%20Projects)
- [2_Control Flow](2_Control%20Flow)
- [3_inbuilt_in Python Data Structures](3_inbuilt_in%20Python%20Data%20Structures)
- [4_Functions in python](4_Functions%20in%20python)
- [5_Import_Modules&Packages](5_Import_Modules%26Packages)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/DataScience-ML-DL-NLP.git
cd DataScience-ML-DL-NLP
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Open the relevant .ipynb notebook in Jupyter or a compatible notebook environment. Inspect its dependency and data-loading cells before running; there is no single shared application entry point.

### Configuration and limitations

Treat chapter folders and end-to-end projects as independent environments. Inspect dataset paths and dependency requirements per example. Notebook execution and full training pipelines were not run in this audit.

### Validation

Recorded checks from the previous maintenance review (2026-10-08): 44 existing Python files passed syntax checks; changed files and new regression tests were checked separately. Syntax checks do not establish full runtime correctness. External APIs, live scraping, GUI interaction, notebook training and production deployment were not comprehensively exercised.

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.
