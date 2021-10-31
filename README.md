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
5. Скачать и поместить в `datasets` тренированные веса `coco`. Директория, в конечном итоге, должна выглядеть так:
```
datasets/
|-test/
|-train/
| mask_rcnn_coco.h5
| train-all.csv
```
6. Установить `venv` для jupyter notebook.
```bash
pip install ipykernel
python -m ipykernel install --name=venv
```
7. Запустить jupyter notebook 
```bash
jupyter notebook
```

Для подготовки датасета - запустить `garbage.ipynb`, а для запуска обучения - `training.ipynb`


## Для работы с CUDA ускорением
Страница с подробными инструкциями от самой [tensorflow тут](https://www.tensorflow.org/install/gpu?hl=ur), которые актуальны для последней версии. Новые версии при установке `pip install tensorflow` автоматически ставят и библиотеку для GPU, однако для версий 1.15 и старше библиотеки поставляются отдельно.
```bash
pip install tensorflow==1.15      # CPU
pip install tensorflow-gpu==1.15  # GPU
```

### Порядок установки
1. Скачать [драйвера](https://www.nvidia.com/drivers) для GPU Nvidia
2. Скачать [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
3. Установить библиотеку [cuDNN](https://developer.nvidia.com/cudnn)

Добавить пути установки CUDA®, CUPTI, и cuDNN в переменную глобального окружения %PATH%. Например, если CUDA® Toolkit установлен в `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0` и cuDNN в `C:\tools\cuda`, надо обновить пути %PATH% до таких:
```
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin;%PATH%
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\extras\CUPTI\lib64;%PATH%
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\include;%PATH%
SET PATH=C:\tools\cuda\bin;%PATH%
```

### Проверка, что CUDA встала нормально
`nvcc -v`

### Проверка, что TF видит GPU
```pyton
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```

Ну и на всякий случай [видос от индуса](https://www.youtube.com/watch?v=2TcnIzJ1RQs)
