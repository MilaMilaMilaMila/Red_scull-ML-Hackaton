# Red_scull-ML-Hackaton
## Установка
1. Виртуальное окружение
```python
# Создать и активировать venv
python -m venv venv
source venv/bin/activate
```
2. Установить [форк библиотеки Mask RCNN](https://github.com/leekunhee/Mask_RCNN]). Нужно для поддержки TensorFlow >= 2.0.0
3. Установить `scikit-image 0.16.2`
```bash
pip uninstall scikit-image
pip install scikit-image==0.16.2
```
4. Создать директорию `datasets` - корень рабочей зоны. Туда же кинуть, всё, что кидается и распаковывается.
5. Установить `venv` для jupyter notebook.
```bash
pip install ipykernel
python -m ipykernel install --name=venv
```
6. Запустить jupyter notebook 
```bash
jupyter notebook
```

Для подготовки датасета - запустить `garbage.ipynb`, а для запуска обучения - `training.ipynb`