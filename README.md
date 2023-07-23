# Architect :sparkles:
The main goal of this project is to assist hackathon participants in quickly prototyping and validating their ideas for hackathon projects. This tool will use three separate language models (LLM chains) in a pipeline to handle different parts of the ideation process: frontend design, backend architecture, and feasibility analysis.

## Features
- **Frontend Design Language Model (FLLM)**: This LLM will generate ideas for the frontend or user interface of the project. It will take the user's initial project idea and their skills or target categories as input, then generate a list of potential frontend features, technologies, and design ideas suitable for the project.

- **Backend Architecture Language Model (BLLM)**: This LLM will focus on the backend architecture of the project. It will also take the user's initial project idea and their skills or target categories as input, then generate a list of potential backend architectures, database solutions, APIs, and other backend technologies that could be utilized in the project.

- **Feasibility Analysis Language Model (FALM)**: This LLM will evaluate the ideas produced by FLLM and BLLM. It will assess the feasibility of the project considering factors like the proposed technologies, time constraints of the hackathon, and the user's skills or target categories. If the project is deemed infeasible, FALM will provide feedback and rerun FLLM and BLLM with adjusted parameters.

## Installation
1. Fork and clone the repository.
2. Create a virtual environment by running command:
```bash
python3 -m venv venv
```
3. Activate the virtual environment by running command:
```bash
source venv/bin/activate
```
4. Install the required packages by running command:
```bash
pip install -r requirements.txt
```
5. Run the application by running command:
```bash
streamlit run src/main.py
```
