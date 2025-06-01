# Educagen Course Generator

An interactive web app that uses Google’s Gemini Large Language Model API to generate fully developed courses from a simple topic prompt. The app produces a complete outline and a structuredd list of modules, each of which can be expanded for detailed, educational content to learn complex topics entirely in one place.

Check out the [demo]()!

![Educagen Home Page Image](/images/homePage.png)

![Educagen Demo Image](/images/example.png)

---

## Features

- **Course Topic Input:** Enter any topic to generate a tailored course of 6 to 10 modules.
- **Comprehensive Course Content:** Generate modules with deep explanations, examples, analogies, key concepts, diagrams, summaries, questions with answers, and additional resources.
- **Module Expansion:** Select which modules to expand via checkboxes and view their full content.
- **Clean, User-Friendly UI:** Easy navigation through course content with expandable modules.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API access and API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tmattkim/educagen.git
   cd educagen
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Google Gemini API key as an environment variable:

   ```bash
   export API_KEY="your_google_gemini_api_key"
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```
---

## Additional Information

- The app uses Gemini 2.0 Flash
