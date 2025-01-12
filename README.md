# RAG Application

This project demonstrates the implementation of a **Retrieval-Augmented Generation (RAG)** application using **LangChain** and **Python**. The app is designed to fetch either user leetcode profile details or user programming language statistics on leetcode based on user queries. It supports standalone execution and a Streamlit-based frontend for an interactive user experience.
This application could work with local llm or hugging face open source model. Check common/llm.py file for more info.

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
- Hugging Face API Token

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
     HUGGINGFACEHUB_API_TOKEN=<your-api-key>
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
Leetcode_Profile_Generator/
├── common/                   # Common utilities shared across the app
│   ├── logger.py             # Logging utilities
│   └── llm.py                # LLM-related logic
├── third_parties/            # Code or integrations from third-party libraries
│   ├── __init__.py           # Module initializer
│   └── leetcode.py           # LeetCode API integration
├── tools/                    # Tools and scripts specific to app functionality
│   └── leetcode.py           # LeetCode-related Tool
├── .env                      # Environment variables (excluded from version control)
├── app.py                    # Main application file for Streamlit
├── config.toml               # Configuration file for the app
├── main.py                   # Entry point of the app
├── Pipfile                   # Pipenv dependency file

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
  "Get Profile Details": "Get the profile details of username letsmailabhishekmarathe"
  ```
  **Output**:
   ### Summary
   The user has attempted a total of 237 questions on LeetCode, with a success rate of 96.63% across all difficulties. They have solved 92.95% of Easy problems, 87.53% of Medium problems, and 40.58% of Hard problems.

   ### Skills and Success Rates
   The user is quite skilled at solving Easy problems, with a success rate of 92.95%. They are also doing well in Medium problems, with a success rate of 87.53%. However, their success rate in Hard problems is relatively low, at 40.58%.

   ### Programming Level and Recommendations
   Based on the data provided, the user's programming level can be rated as a 6 out of 10. They are doing well in Easy and Medium problems, but their success rate in Hard problems is quite low. To improve, they should focus on practicing more Hard problems and seeking out resources to help them better understand the underlying concepts and algorithms. Additionally, they may benefit from reviewing their solutions to Easy and Medium problems to identify any potential areas for improvement or optimization.
   
- **Programming Stats**:
  ```
  "Get Programing Language Stats": "Get the Programing Language Stats of username letsmailabhishekmarathe"
  ```
  **Output**:

   ### Summary
   This user has solved a total of 208 problems on LeetCode. They have used three different programming languages: Python, JavaScript, and TypeScript. Python and TypeScript have each been used to solve one problem, while JavaScript is their most frequently used language, with a total of 194 problems solved.

   ### Programming Languages Used
   - Python: 1 problem
   - JavaScript: 194 problems
   - TypeScript: 53 problems

   ### Favourite Programming Language
   Based on the data provided, the user's favourite programming language on LeetCode is JavaScript, as they have used it to solve the majority of their problems (approximately 93.7% of their total problem solutions).


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

