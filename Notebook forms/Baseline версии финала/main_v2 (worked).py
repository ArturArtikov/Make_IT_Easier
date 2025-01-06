# Импортируем основные данные для классификатора CatBoost
from catboost import CatBoostClassifier, Pool, cv
# Импортируем дополнительную модель
from sklearn.ensemble import HistGradientBoostingClassifier
# Импортируем модуль для работы с данными
import pandas as pd
# Импортируем модуль для работы с системой
import os

# Функция для обучения на 1 наборе данных
def fitting(path):
    try:
        # Получим список файлов по выданному пути к папке
        current_data = os.listdir(path)
    # В случае ошибки отловим ее и прервем выполнение цикла
    except Exception:
        return "Не папка"
    # В случае отсутствия ошибки - сохраним данные
    else:
        current_data = os.listdir(path)
    # Выделим тренировочный датасет
    train_data = [data for data in current_data if data.endswith('train.csv')][0]
    # Выделим тестовый датасет
    test_data = [data for data in current_data if data.endswith('test.csv')][0]
    # Откроем тренировочные данные
    train_data = pd.read_csv(path + f'/{train_data}')
    # Откроем тестовые данные
    test_data = pd.read_csv(path + f'/{test_data}')
    # Инициалищируем модель
    classificator = HistGradientBoostingClassifier(random_state=42, 
                                                   max_depth=5, 
                                                   min_samples_leaf=4)
    # # Выделим тренировочную часть данных
    X = train_data.drop('target', axis=1)
    # # Выделим тестовую часть данных
    y = train_data['target']
    # Обучим модель на тренировочных данных
    classificator.fit(X, y)
    # Создадим предсказание на тестовых данных
    model_pred = classificator.predict_proba(test_data)[:, 1]
    # Объединим предсказание с метками
    test_data['target'] = model_pred
    # Отсортируем предсказание
    prediction = test_data[['id', 'target']].sort_values(by='id', ascending=True)
    # Вернем предсказание, как результат работы модели
    return prediction


# Функция смотрит на рабочее окружение и на папки с данными
def model():
    # Пропишем путь к файлам данных
    data = 'data'
    # Запишем список датасетов в папке:
    folders = os.listdir(data)
    # Создадим цикл для прохождения по каждому файлу и генерации предсказания
    for fold in folders:
        # Запишем новый путь к данным
        data_path = data + f'/{fold}'
        # Вызовем функцию, передав в нее путь к папке для обучения
        prediction = fitting(path=data_path)
        # Сохраним полученное предсказание
        if type(prediction) is not str:
            # Сохраняем предсказание
            prediction.to_csv(f"predictions/{fold}.csv", index=False)
            print("Предсказание создано!")
        else:
            print("Невозможно создать предсказание!")

# Обозначаем действия при запуске кода
if __name__ == "__main__":
    # Запускаем модель
    model()