import json

import numpy as np
from keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.models import load_model

model_category = None

# tokenizer считаем из файла, ранее было сохранен при обучении
with open('./static/tokenizer.json') as f:
    data = json.load(f)

    tokenizer = tokenizer_from_json(data)

# наименование классов из файла
with open('./static/classes.txt', encoding="utf-8") as f:
    data = f.read()
    class_list = data.split("\n")


def get_category(message: str) -> str:
    """
    Предсказание категории по тексту
    :param message: текст
    :return: категория сообщения
    """
    global model_category
    if model_category is None:
        model_category = load_model('./static/model_text_bow_dense.h5')
    message_as_list = [message]

    data_matrix = tokenizer.texts_to_matrix(message_as_list)

    predict = model_category.predict(data_matrix)

    category = np.argmax(predict, axis=1)

    return class_list[category[0]]
