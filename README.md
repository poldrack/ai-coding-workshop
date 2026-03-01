### AI Coding Workshop

#### Setup 

This is for Mac/Linux; Windows users should consult the [Microsoft guide for Python development environments on Windows](https://learn.microsoft.com/en-us/windows/dev-environment/python?tabs=winget) for more info.

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Clone this repository: `git clone https://github.com/poldrack/ai-coding-workshop`
- Synchronize the packages: `uv sync`
- Activate the virtual environment: `source .venv/bin/activate`
- Confirm that the testing environment works: `pytest test_cohensd.py`
    - Should show that 1 test passed.