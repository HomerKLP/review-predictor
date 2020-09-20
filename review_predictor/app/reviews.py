# Vendor
from django.conf import settings
from os.path import join
from creme import compose, feature_extraction, naive_bayes, metrics
import pandas as pd
import pickle


def train_model():
    """Тренируем модель нейронки"""
    # Считываем датасет
    cols_to_use = ['text', 'rating']
    df = pd.read_csv(
        'reviews.csv',
        delimiter=',',
        index_col=False,
        usecols=cols_to_use
    )[cols_to_use]

    df = df.sample(frac=1)
    # Преобразуем датасет в лист кортежей
    df = df.to_records(index=False)
    # Создаем пайплайн
    metric = metrics.Accuracy()
    model = compose.Pipeline(
        ('tokenize', feature_extraction.BagOfWords(lowercase=False)),
        ('nb', naive_bayes.MultinomialNB(alpha=1))
    )
    # Тренируем модель построчно
    for sentence, label in df:
        pred = model.predict_one(sentence.lower())
        metric = metric.update(label, pred)
        model = model.fit_one(sentence.lower(), label)

    with open(join(settings.BASE_DIR, 'model.pkl'), 'wb') as exporting_model:
        pickle.dump(model, exporting_model)


def predict_rating(feedback: str) -> int:
    """Предсказать рейтинг отзыва"""
    with open(join(settings.BASE_DIR, 'model.pkl'), 'rb') as input_model:
        model = pickle.load(input_model)
        return model.predict_one(feedback.lower())
