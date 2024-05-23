# Rule-Based Sentiment Analysis Web App (Flask)

This simple web application allows users to input text and receive an instant assessment of its sentiment (positive or negative). It utilizes a rule-based approach with NLTK's VADER lexicon to perform the sentiment analysis.

## Features

*   Real-time Sentiment Analysis: Provides immediate feedback on the sentiment of user-submitted text.
*   Rule-Based Approach: Uses a lexicon and predefined rules to classify sentiment, making the process transparent and interpretable.
*   VADER Lexicon: Leverages NLTK's Valence Aware Dictionary and sEntiment Reasoner (VADER) for sentiment scoring.
*   User-Friendly Interface: Built with Flask, offering a clean and intuitive web interface for user interaction.

## Installation and Setup

1.  Clone the Repository:
    ```bash
    git clone <repository-url>
    ```
2.  Install Dependencies:
    ```bash
    pip install Flask nltk
    ```
3.  Download VADER Lexicon:
    ```bash
    python
    import nltk
    nltk.download('vader_lexicon')
    ```
4.  Run the App:
    ```bash
    # Windows:
    set FLASK_APP=main.py
    flask run

    # macOS/Linux:
    export FLASK_APP=main.py
    flask run
    ```
5.  Access the App:
    Open a web browser and navigate to `` http://127.0.0.1:5000/ ``

## Usage

1.  Enter the text you want to analyze in the input field.
2.  Click the "Submit" button.
3.  The app will display the sentiment of the input text as either "Positive" or "Negative."

## Project Structure
```
your_project_folder/
├── main.py       (Flask app logic)
├── static/
│   └── style.css (Optional styling)
└── templates/
    └── index.html (HTML template)
```

## Technologies Used

*   Python
*   Flask (Web Framework)
*   NLTK (Natural Language Toolkit)
*   VADER Lexicon (Sentiment Analysis)
*   HTML & CSS (Frontend)

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License.