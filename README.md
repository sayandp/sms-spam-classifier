# SMS Spam Classifier

A compact SMS spam detection app using TF-IDF + Naive Bayes and a Streamlit front-end.

Live demo: https://share.streamlit.io/sayandp/sms-spam-classifier/main/app.py

## What this repo contains

- `spam.csv` — original SMS spam dataset
- `sms_classi.py` — training script (preprocess, train, evaluate, save `nb_model.pkl` and `tfidf.pkl`)
- `app.py` — Streamlit app that loads the saved model and vectorizer for predictions
- `nb_model.pkl`, `tfidf.pkl` — serialized model & vectorizer (included for quick demo)
- `requirements.txt` — pinned dependencies

## Quick start (local)

1. Clone the repository:

```powershell
git clone https://github.com/sayandp/sms-spam-classifier.git
cd sms-spam-classifier
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the Streamlit app:

```powershell
streamlit run app.py
```

Open http://localhost:8501 when the server starts.

## Training / Retraining

To retrain the model on `spam.csv` (and overwrite the pickles):

```powershell
python sms_classi.py
```

After training the script will save `nb_model.pkl` and `tfidf.pkl` in the project folder.

## NLTK stopwords note (deployment)

The app includes a small compatibility step to ensure NLTK stopwords are available in environments that do not have NLTK data preinstalled (Streamlit Cloud, etc.). The code downloads stopwords into a local `nltk_data/` folder at runtime if needed.

This folder is intentionally not committed — ensure `nltk_data/` is present in `.gitignore`.

## Deployment (Streamlit Cloud)

1. Push this project to GitHub (already done): https://github.com/sayandp/sms-spam-classifier
2. Sign in to https://share.streamlit.io with your GitHub account
3. Click **New app** → select the `sayandp/sms-spam-classifier` repo → branch `main` → file `app.py` → **Deploy**

## Files of interest

- `app.py` — main web app
- `sms_classi.py` — training pipeline
- `requirements.txt` — runtime dependencies

## Contributing

Contributions welcome: open issues or submit PRs. For code/style consistency, please run tests and keep changes small.

## License

MIT License

## Contact

Repo: https://github.com/sayandp/sms-spam-classifier
Live app: https://share.streamlit.io/sayandp/sms-spam-classifier/main/app.py
