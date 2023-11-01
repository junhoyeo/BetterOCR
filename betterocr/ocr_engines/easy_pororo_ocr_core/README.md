<h2 align="center">
Korean OCR using pororo
</h2>

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.7.13-blue.svg"/>
  <img src="https://img.shields.io/badge/torch-v1.13.1-blue.svg"/>
  <img src="https://img.shields.io/badge/torchvision-v0.14.1-blue.svg"/>
  <img src="https://img.shields.io/badge/opencv_python-v4.7.0.68-blue.svg"/>
</div>

This is a Korean OCR Python code using the Pororo library.

<div align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FboAZK8%2FbtrYeYCWzKj%2Ft3Lhe05Bqm1iQNkOo4x9Lk%2Fimg.png" width="70%">
</div>

## Requirements

You can packages install with [pipenv](https://pipenv.pypa.io/en/latest/):

```sh
pipenv install
```

Then, you can run Python through the following commands:
```sh
pipenv run python main.py

# Or using virtual env
pipenv shell
python main.py
```

## PORORO: Platform Of neuRal mOdels for natuRal language prOcessing

[pororo](https://github.com/kakaobrain/pororo) is a library developed by KakaoBrain for performing natural language processing and speech-related tasks. 

This repository is configured to only include the OCR functionality from the pororo library. If you wish to use other pororo features such as natural language processing, please install pororo through `pip install pororo`.

## Usage

```python
from pororo import Pororo

ocr = PororoOcr()
image_path = input("Enter image path: ")
text = ocr.run_ocr(image_path, debug=True)
print('Result :', text)
```

Output:

```sh
['메이크업존 MAKEUP ZONE', '드레스 피팅룸 DRESS FITTING ROOM', '포토존 PHOTO ZONE']
```

------



<div align="center">
<img src="https://user-images.githubusercontent.com/69428232/216900012-40572b3e-fc16-4bb0-a119-d61eaf680213.png" width="70%">
</div>

```sh
["Life is ot a spectator sport. If you're going to spend your whole life in the grandstand just watching what goes on, in my apinion you're wasting your life.",
 "인생은 구경거리가 아니다. 무슨 일이 일어나는지 보기만 하는 것은 인생을 낭비하고 있는 것이다.",
 'Jackie Robinson']
```
