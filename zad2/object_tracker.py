![image](https://user-images.githubusercontent.com/39220694/168040477-dc9e4f53-1e2c-4526-823d-3f4ba842cc7e.png)


opencv-python==4.1.1.26 <br>
lxml<br>
tqdm<br>
tensorflow==2.3.0<br>
absl-py<br>
easydict<br>
matplotlib<br>
pillow<br>
файл requirements.txt содержит все используемые библиотеки<br>

<p>нейросеть - попытка воссоздать человеческий мозг. 
состоит из 3 частей: </p>
1. Обучающаяся 
2. Тренировочная 
3. Тестовая

Математическая модель, а также её программное или аппаратное воплощение, построенная по принципу организации и функционирования биологических нейронных сетей - сетей нервных клеток живого организма. 

<p>нейросети бывают готовые и их можно обучать</p>
dataset - набор данных. для обучения нужно подготовить данные 
обучение - сбор данных, подготовка датасета
тренировка - обучение на основе датасета. обучение нейросети во время уравнения
тест - загрука нового изображения - наблюдаем, чему нейронная сеть научилась

<p>flags.DEFINE_string('video', './data/video/test.mp4', 'path to input video or set to 0 for webcam')
</p>

   аргументы командной строки передаются в def main(_argv): 
  video - название флага. все, что идет дальше - значения, которые может принимать флаг
  <p>python object_tracker.py --video ./data/video/test.mp4 --output ./outputs/demo.avi --model yolov4</p>
  <p>python object_tracker.py --video ./data/video/test.mp4 --output ./outputs/demo.avi --model yolov4</p>
  <p>python object_tracker.py 0 --output ./outputs/demo.avi --model yolov4</p>

после теста результатом тренировки становится веса(коэфы, параметры, которые можно передавать для дальнейшего обучения)

https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset&_ga=2.125677512.352426606.1652336646-1703930766.1640669646


Существует мнго разных типов данных для хранения большого количества данных
массивы хранят 1 тип данных
список хранит разные типы данных
множество не имеют дубликатов
в нашем случае будет использоваться <b>Множество</b> - \то структура данных, которые содержат неупорядченные элеменеты.

Элемент из множества нужно использовать цикл for m in name
чтобы добавить элемент множества используется функция add name.add("feb")

v = ((x1н, x2н), (x1к, x2к)) - вектор который представляет собой двумерный массив  v[0][1] обращение к элементу массив. - первая цифра номер скобки, вторая цифра номер элемента

Угол между осью Х и прямой = arctg k 
![image](https://user-images.githubusercontent.com/39220694/168235057-e0598e08-b0a9-458c-b0bf-ddfb7d2f3b33.png)
Проблема вертикального случая - мы не можем сравнить координаты по у
Для решения использовать матрицу поворота
