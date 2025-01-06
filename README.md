# RAG Application

This project demonstrates the implementation of a **Retrieval-Augmented Generation (RAG)** application using **LangChain** and **Python**. The app is designed to fetch either user leetcode profile details or user programming language statistics on leetcode based on user queries. It supports standalone execution and a Streamlit-based frontend for an interactive user experience.

---

## Features

1. **Zero-Shot ReAct Prompt**:
   - Uses the Zero-Shot ReAct (Reasoning + Acting) paradigm to decide which tool to invoke based on the user's query.
   - Dynamically fetches relevant information from predefined tools.

2. **Toolset**:
   - `fetch_leetcode_profile_info_tool`: Retrieves user profile information.
   - `fetch_leetcode_language_info_tool`: Fetches programming language statistics for a user.

3. **Standalone Execution**:
   - Run the application as a command-line Python script.

4. **Streamlit Integration**:
   - A Streamlit-based interface for enhanced usability.

---

## Installation

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)
- Streamlit

### Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Environment**:
   - Ensure any necessary API keys (if required) are added to a `.env` file in the root directory.
   - Example `.env` file:
     ```env
     API_KEY=<your-api-key>
     ```

---

## Usage

### Standalone Script
To run the app as a standalone script:
```bash
python main.py
```
- The script will prompt for user input and execute the required functionality.

### Streamlit Application
To run the Streamlit frontend:
```bash
streamlit run app.py
```
- Open the URL displayed in your terminal (e.g., `http://localhost:8501`) to access the web interface.

---

## Project Structure

```
├── main.py                # Standalone script for the application
├── app.py                 # Streamlit-based interface
├── tools.py               # Contains tool functions for profile details and stats
├── prompts.py             # Contains prompts for the LLM
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .env                   # Environment variables (optional)
```

---

## How It Works

1. **User Input**:
   - The user provides a query, such as:
     - "Get the profile details for user123."
     - "Fetch programming stats for user123."

2. **Zero-Shot ReAct Agent**:
   - The agent determines which tool to use based on the input query.

3. **Tool Execution**:
   - The selected tool fetches the required data and returns it to the user.

4. **Streamlit Integration**:
   - Displays the tool selection process and the final output interactively.

---

## Example Queries

- **Profile Details**:
  ```
  Get the profile details for user123.
  ```
  **Output**:
  ```
  Profile details for user123: [Name: John Doe, Role: Software Developer]
  ```

- **Programming Stats**:
  ```
  Fetch programming stats for user456.
  ```
  **Output**:
  ```
  Stats for user456: [Solved: 75 problems, Rank: Top 5%]
  ```

---

## Future Enhancements

- Add support for more tools and APIs.
- Implement user authentication for personalized responses.
- Optimize LLM interactions for faster processing.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments

- [LangChain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

