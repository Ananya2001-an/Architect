# Architect :sparkles:
Inspired by hackathon enthusiasts, Architect was created to help participants rapidly prototype and validate ideas. Using language models, this digital ally would 
generate designs, craft architectures, and analyze project feasibility. Its ultimate goal is to empower dreamers and innovators to turn their ideas into reality in the 
chaotic atmosphere of a hackathon.

![Screenshot 2023-07-23 150131](https://github.com/Ananya2001-an/Architect/assets/55504616/47f23d28-a646-4ac7-8679-fc66ac3a9a42)

## What it does
- Architect is a powerful AI tool that uses three distinct language models to help users develop their project ideas. The Frontend Design Language Model (FLLM) provides potential frontend features and design concepts, while the Backend Architecture Language Model (BLLM) suggests backend architectures and database solutions. The Feasibility Analysis Language Model (FALM) then evaluates the compatibility of the proposed technologies, user skills, and time constraints to ensure a successful project.

## Features
- **Frontend Design Language Model (FLLM)**: This LLM will generate ideas for the frontend or user interface of the project. It will take the user's initial project idea and their skills or target categories as input, then generate a list of potential frontend features, technologies, and design ideas suitable for the project.

- **Backend Architecture Language Model (BLLM)**: This LLM will focus on the backend architecture of the project. It will also take the user's initial project idea and their skills or target categories as input, then generate a list of potential backend architectures, database solutions, APIs, and other backend technologies that could be utilized in the project.

- **Feasibility Analysis Language Model (FALM)**: This LLM will evaluate the ideas produced by FLLM and BLLM. It will assess the feasibility of the project considering factors like the proposed technologies, time constraints of the hackathon, and the user's skills or target categories. If the project is deemed infeasible, FALM will provide feedback and rerun FLLM and BLLM with adjusted parameters.

## Challenges we ran into
- Accurate Feasibility Evaluation: Ensuring the FALM correctly assesses project feasibility based on technologies, skills, and time constraints is a critical challenge.
- Integration of Multiple LLMs: Managing the interaction and data flow between FLLM, BLLM, and FALM requires careful coordination to incorporate feedback effectively.
- User Experience: Designing an intuitive and user-friendly interface that provides constructive feedback for infeasible projects is a challenge.

## Accomplishments that we're proud of
We are proud of finishing the project on time which seemed like a tough task as we started working on it quite late due to other commitments and were also able to add most of the features that we envisioned during ideation. Moreover, we learned a lot about langchain, stramlit and libraries that we could incorporate into our project to meet our unique needs. We also learned how to maintain great communication among all teammates. Each of us felt like a great addition to the team. From the backend, frontend, research, we are proud of the great number of things we have built within 24 hours. And as always, working overnight was pretty fun! :)

## What we learned
- Integrating multiple language models in a pipeline to tackle distinct tasks efficiently.
- Designing a user-friendly interface that enhances the overall experience.
- Understanding the complexities of evaluating project feasibility using language models.

## What's next for Architect
We just really want this project to create a real positive impact on humanity. We are planning to integrate an "Inspirational Mode" that generates novel hackathon ideas based on trending technologies and popular themes and integration with educational resources. Overall, we hope that one day this project can be widely used by hackers globally to quickly prototype and validate ideas for hackathon projects as well as for small businesses & startups.

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
