# Language Lesson Generation Agent

A CrewAI-powered agent that generates comprehensive language lessons using Google's Gemini AI.

## Features

- Generates structured language lessons tailored to proficiency levels
- Supports multiple African languages (focus on Yoruba)
- Creates culturally appropriate content
- Includes vocabulary, grammar, dialogues, and practice exercises

## Prerequisites

```bash
pip install google-generativeai crewai crewai-tools python-dotenv
```

## Setup

1. Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

2. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

```python
from lesson_agent import LessonGenerationAgent

# Initialize the agent
agent = LessonGenerationAgent(gemini_api_key="your_api_key")

# Define lesson parameters
lesson_params = {
    "target_language": "Yoruba",
    "primary_language": "English",
    "proficiency_level": "Beginner",
    "lesson_focus": "Greetings and introductions",
    "learning_goals": "Be able to greet someone and introduce yourself",
    "cultural_context": "Yoruba culture in Nigeria",
    "age_group": "adult"
}

# Generate lesson
lesson = agent.generate_lesson(lesson_params)
```

## Run

```bash
python lesson_agent.py
```

## Output Structure

The agent returns a structured lesson with:

- Metadata (language, proficiency level, etc.)
- Introduction and explanations
- Vocabulary with pronunciations
- Grammar rules and examples
- Cultural notes
- Practice exercises
- Summary and review points

## Files

- `lesson_agent.py` - Main agent implementation
- `json_lesson_demo.py` - Demo lesson parameters
- `requirements.txt` - Python dependencies
