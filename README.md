# SMS Spam Classifier

A machine learning application that classifies SMS messages as spam or legitimate (ham) using a Naive Bayes classifier with TF-IDF vectorization.

## Features

- **Text Preprocessing**: Removes special characters, converts to lowercase, applies stemming, and removes stopwords
- **TF-IDF Vectorization**: Converts cleaned text into numerical features (max 3000 features)
- **Naive Bayes Classification**: Fast and efficient probabilistic classifier
- **Streamlit Web Interface**: Easy-to-use interactive web application
- **Real-time Predictions**: Instantly classify any SMS message

## Project Structure

```
sms-spam-classifier/
├── spam.csv                    # Dataset with SMS messages and labels
├── sms_classi.py              # Training script
├── app.py                     # Streamlit web application
├── nb_model.pkl               # Trained Naive Bayes model
├── tfidf.pkl                  # TF-IDF vectorizer
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

Run the training script to retrain the model on the dataset:
```bash
python sms_classi.py
```

This will:
- Load and preprocess the SMS dataset
- Train a Naive Bayes classifier
- Display model performance metrics
- Save the model and vectorizer for deployment

### Running the Web App

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` where you can:
- Enter an SMS message
- Get instant classification (Spam or Ham)
- View prediction results

## Dataset

The project uses the **SMS Spam Collection Dataset** which contains:
- **5,574 SMS messages**
- **2 classes**: Ham (legitimate) and Spam
- **Features**: Message text

### Data Labels
- **Ham (0)**: Legitimate SMS messages
- **Spam (1)**: Spam/unwanted SMS messages

## Model Performance

The Naive Bayes classifier achieves high accuracy on the SMS dataset with:
- Fast training time
- Good generalization
- Efficient prediction
- Interpretable results

## Technical Stack

- **Python 3.14**
- **pandas**: Data manipulation
- **scikit-learn**: Machine learning
- **nltk**: Natural language processing
- **streamlit**: Web application framework
- **pickle**: Model serialization

## Requirements

See `requirements.txt` for the complete list of dependencies.

## Deployment

### Streamlit Cloud

Deploy your app on Streamlit Cloud:

1. Push this repository to GitHub
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and connect your GitHub repository
4. Select this repository and specify `app.py` as the main file
5. Deploy!

## How It Works

1. **Text Cleaning**: 
   - Remove special characters
   - Convert to lowercase
   - Remove stopwords
   - Apply Porter Stemming

2. **Vectorization**: Convert cleaned text to TF-IDF vectors

3. **Classification**: Use Naive Bayes to predict spam probability

4. **Result**: Display classification result to user

## Future Improvements

- Add more classifiers (SVM, Random Forest, etc.)
- Implement model comparison
- Add confidence scores
- Support multiple languages
- Implement active learning
- Add chat history/logging

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created as a machine learning classification project.

## Acknowledgments

- Dataset: SMS Spam Collection Dataset
- Framework: Streamlit
- Libraries: scikit-learn, NLTK, pandas
