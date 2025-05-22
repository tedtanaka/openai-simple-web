# openai-simple-web
A very simple web app that is a front end to OpenAI.

Followed the tutorial from here: https://www.geeksforgeeks.org/develop-an-llm-application-using-openai/

To run in Windows CMD shell:

* python -m venv venv
* venv\Scripts\activate.bat
* pip install -r requirements.txt
* streamlit run openai_web.py (Ctrl-C doesn't always work)

To run in a Codespace (Linux):

* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* streamlit run openai_web.py