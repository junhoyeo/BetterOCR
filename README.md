<p align="center">
  <a href="https://github.com/junhoyeo">
    <img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/logo.png" width="256px" />
  </a>
</p>
<h1 align="center">BetterOCR</h1>

<p align="center">
<a href="https://pypi.org/project/betterocr"><img alt="PyPI" src="https://img.shields.io/pypi/v/betterocr.svg?style=for-the-badge&labelColor=162246" /></a>
<a href="https://github.com/junhoyeo/betterocr/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&labelColor=162246" /></a>
<p>

> 🔍 Better text detection by combining multiple OCR engines with 🧠 LLM.

OCR _still_ sucks! ... Especially when you're from the _other side_ of the world (and face a significant lack of training data in your language) — or just not thrilled with noisy results.

**BetterOCR** combines results from multiple OCR engines with an LLM to correct & reconstruct the output.

### 🔍 OCR Engines
Currently supports [EasyOCR](https://github.com/JaidedAI/EasyOCR) (JaidedAI), [Tesseract](https://github.com/tesseract-ocr/tesseract) (Google), and [Pororo](https://github.com/kakaobrain/pororo) (KakaoBrain).

- For Pororo, we're using the code from https://github.com/black7375/korean_ocr_using_pororo <br />
  (Pre-processing ➡️ _Text detection_ with EasyOCR ➡️ _Text recognition_ with Pororo).
- Pororo is used only if the language options (`lang`) specified include either 🇺🇸 English (`en`) or 🇰🇷 Korean (`ko`). Also additional dependencies listed in <a href="https://github.com/junhoyeo/BetterOCR/blob/main/pyproject.toml#L22"><code>[tool.poetry.group.pororo.dependencies]</code></a> should be available. (If not, it'll automatically be excluded from enabled engines.)

### 🧠 LLM
Supports [Chat models](https://github.com/openai/openai-python#chat-completions) from OpenAI.

### 📒 Custom Context
Allows users to provide an optional context to use specific keywords such as proper nouns and product names. This assists in spelling correction and noise identification, ensuring accuracy even with rare or unconventional words.

### 🛢️ Resources

- Head over to [💯 Examples](#-Examples) to view performace by languages (🇺🇸, 🇰🇷, 🇮🇳).
- Coming Soon: ~~box detection~~ 🧪✅, improved interface 🚧, async support, and more. Contributions are welcomed.

> **Warning**<br/>
> This package is under rapid development 🛠

<a href="https://github.com/junhoyeo">
  <img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/arch.jpg?v=2" width="100%" />
</a>

> Architecture

## 🚀 Usage (WIP)

```bash
pip install betterocr
# pip3 install betterocr
```

```py
import betterocr

# text detection
text = betterocr.detect_text(
    "demo.png",
    ["ko", "en"], # language codes (from EasyOCR)
    context="", # (optional) context
    tesseract={
      # Tesseract options here
      "config": "--tessdata-dir ./tessdata"
    },
    openai={
      # OpenAI options here

      # `os.environ["OPENAI_API_KEY"]` is used by default
      "API_KEY": "sk-xxxxxxx",

      # rest are used to pass params to `client.chat.completions.create`
      # `{"model": "gpt-4"}` by default
      "model": "gpt-3.5-turbo",
    },
)
print(text)
```

### 📦 Box Detection

| Original | Detected |
|:---:|:---:|
| <img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/demo-1.png" width="500px" /> | <img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/boxes-0.png" width="500px" /> |

Example Script: https://github.com/junhoyeo/BetterOCR/blob/main/examples/detect_boxes.py (Uses OpenCV and Matplotlib to draw rectangles)

```py
import betterocr

image_path = ".github/images/demo-1.png"
items = betterocr.detect_boxes(
    image_path,
    ["ko", "en"],
    context="퍼멘테이션 펩타인 아이케어 크림",  # product name
    tesseract={
        "config": "--psm 6 --tessdata-dir ./tessdata -c tessedit_create_boxfile=1"
    },
)
print(items)
```

<details>
  <summary>View Output</summary>

```py
[
  {'text': 'JUST FOR YOU', 'box': [[543, 87], [1013, 87], [1013, 151], [543, 151]]},
  {'text': '이런 분들께 추천드리는 퍼멘테이션 펩타인 아이케어 크림', 'box': [[240, 171], [1309, 171], [1309, 224], [240, 224]]},
  {'text': '매일매일 진해지는 다크서클을 개선하고 싶다면', 'box': [[123, 345], [1166, 345], [1166, 396], [123, 396]]},
  {'text': '축축 처지는 피부를 탄력 있게 바꾸고 싶다면', 'box': [[125, 409], [1242, 409], [1242, 470], [125, 470]]},
  {'text': '나날이 늘어가는 눈가 주름을 완화하고 싶다면', 'box': [[123, 479], [1112, 479], [1112, 553], [123, 553]]},
  {'text': 'FERMENATION', 'box': [[1216, 578], [1326, 578], [1326, 588], [1216, 588]]},
  {'text': '민감성 피부에도 사용할 수 있는 아이크림을 찾는다면', 'box': [[134, 534], [1071, 534], [1071, 618], [134, 618]]},
  {'text': '얇고 예민한 눈가 주변 피부를 관리하고 싶다면', 'box': [[173, 634], [1098, 634], [1098, 690], [173, 690]]}
]
```

</details>

## 💯 Examples

> **Note**<br/>
> Results may vary due to inherent variability and potential future updates to OCR engines or the OpenAI API.

### Example 1 (English with Noise)

<img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/demo-0.webp" width="500px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `CHAINSAWMANChapter 109:The Easy Way to Stop Bullying~BV-THTSUKIFUUIMUTU ETT` |
| Tesseract | `A\ ira \| LT ge a TE ay NS\nye SE F Pa Ce YI AIG 44\nopr See aC\n; a) Ny 7S =u \|\n_ F2 SENN\n\ ZR\n3 ~ 1 A \ Ws —— “s 7 “A\n=) 24 4 = rt fl /1\n£72 7 a NS dA Chapter 109:77/ ¢ 4\nZz % = ~ oes os \| \STheEasf Way.to Stop Bullying:\n© Wa) ROT\n\n` |
| Pororo | `CHAINSAWNAN\nChapter 109\nThe Easy Way.to Stop Bullying.\nCBY=TATSUKI FUJIMDTO` |
| LLM | 🤖 GPT-3.5 |
| **Result** | **`CHAINSAW MAN\n\nChapter 109: The Easy Way to Stop Bullying\n\nBY: TATSUKI FUJIMOTO`** |

### Example 2 (Korean+English)

<img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/demo-1.png" width="500px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `JUST FOR YOU이런 분들께 추천드리는 퍼멘테이선 팬타인 아이켜어 크림매일매일 진해지논 다크서클올 개선하고 싶다면축축 처지논 피부름 탄력 잇게 바꾸고 싶다면나날이 늘어가는 눈가 주름올 완화하고 싶다면FERMENATION민감성 피부에도 사용할 수잇는 아이크림올 찾는다면얇고 예민한 눈가 주변 피부름 관리하고 싶다면`                                                                              |
| Tesseract | `9051 508 \ㅇ4\n이런 분들께 추천드리는 퍼멘테이션 타인 아이케어 크림\n.매일매일 진해지는 다크서클을 개선하고 싶다면        "도\nㆍ축축 처지는 피부를 탄력 있게 바꾸고 싶다면         7\nㆍ나날이 늘어가는 눈가 주름을 완화하고 싶다면        /\n-민감성 피부에도 사용할 수 있는 아이크림을 찾는다면    (프\nㆍ않고 예민한 눈가 주변 피부를 관리하고 싶다면                         밸\n\n` |
| Pororo | `JUST FOR YOU\n이런 분들께 추천드리는 퍼맨테이션 펩타인 아이케어 크림\n매일매일 진해지는 다크서클을 개선하고 싶다면\n촉촉 처지는 피부를 탄력 있게 바꾸고 싶다면\n나날이 늘어가는 눈가 주름을 완화하고 싶다면\nFERMENTATIOM\n민감성 피부에도 사용할 수 있는 아이크림을 찾는다면\n얇고 예민한 눈가 주변 피부를 관리하고 싶다면` |
| LLM | 🤖 GPT-3.5 |
| **Result** | **`JUST FOR YOU\n이런 분들께 추천드리는 퍼멘테이션 펩타인 아이케어 크림\n매일매일 진해지는 다크서클을 개선하고 싶다면\n축축 처지는 피부를 탄력 있게 바꾸고 싶다면\n나날이 늘어가는 눈가 주름을 완화하고 싶다면\nFERMENTATION\n민감성 피부에도 사용할 수 있는 아이크림을 찾는다면\n얇고 예민한 눈가 주변 피부를 관리하고 싶다면`** |

### Example 3 (Korean with custom `context`)

<img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/demo-2.png" width="400px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `바이오함보#세로모공존존세럼6글로우픽 설문단 100인이꼼꼼하게 평가햇어요"#누적 판매액 40억#제품만족도 1009` |
| Tesseract | `바이오힐보\n#세로모공폰폰세럼\n“글로 으피 석무다 1 00인이\n꼼꼼하게평가했어요”\n\n` |
| Pororo | `바이오힐보\n#세로모공쫀쫀세럼\n'.\n'글로우픽 설문단 100인이\n꼼꼼하게 평가했어요'"\n#누적 판매액 40억\n# 제품 만족도 100%` |
| Context | `[바이오힐보] 세로모공쫀쫀세럼으로 콜라겐 타이트닝! (6S)` |
| LLM | 🤖 GPT-4 |
| **Result** | **`바이오힐보\n#세로모공쫀쫀세럼\n글로우픽 설문단 100인이 꼼꼼하게 평가했어요\n#누적 판매액 40억\n#제품 만족도 100%`** |

#### 🧠 LLM Reasoning (*Old)

Based on the given OCR results and the context, here is the combined and corrected result:

```
{
  "data": "바이오힐보\n#세로모공쫀쫀세럼\n글로우픽 설문단 100인이 꼼꼼하게 평가했어요\n#누적 판매액 40억\n#제품만족도 100%"
}
```

- `바이오힐보` is the correct brand name, taken from [1] and the context.
- `#세로모공쫀쫀세럼` seems to be the product name and is derived from the context.
- `글로우픽 설문단 100인이 꼼꼼하게 평가했어요` is extracted and corrected from both OCR results.
- `#누적 판매액 40억` is taken from [0].
- `#제품만족도 100%` is corrected from [0].

### Example 4 (Hindi)

<img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/demo-3.webp" width="500px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `` `७नवभारतटाइम्सतोक्यो ओलिंपिक के लिए भारतीय दलका थीम सॉन्ग लॉन्च कर दिया गयाबुधवार को इस सॉन्ग को किया गया लॉन्चसिंगर मोहित चौहान ने दी है आवाज7लखेल मंत्री किरण रिजिजू ने ट्विटर पर शेयरकिया थीम सॉन्ग का वीडियो0ब४0 २०२०गीत का नाम- '्लक्ष्य तेरा सामने है' , खेलमंत्री ने ५७ सेकंड का वीडियो किया शेयर `` |
| Tesseract | `'8ा.\nनवभोरत टैइम्स\n\nतोक्यो ओलिंपिक के लिंए भारतीय दल\n\nका थीम सॉन्ग लॉन्च कर दिया गया\n\nबुधवार को हस सॉन्ग को किया गया लॉन्च\nसिंगर मोहित चौहान ने दी है आवाज\n\nखेल मंत्री किरण रिजिजू ने द्विटर पर शेयर\nकिया थीम सॉन्ग का वीडियो\n\nपृ 0 (९ है 0 2 0 2 0 गीत का नाम- 'लक्ष्य तेरा सामने है', खेल\n\n(2 (9९) मंत्री ने 57 सेकंड का वीडियो किया शेयर\n\n` |
| LLM | 🤖 GPT-4 |
| **Result** | **`नवभारत टाइम्स\nतोक्यो ओलिंपिक के लिए भारतीय दल का थीम सॉन्ग लॉन्च कर दिया गया\nबुधवार को इस सॉन्ग को किया गया लॉन्च\nसिंगर मोहित चौहान ने दी है आवाज\n\nखेल मंत्री किरण रिजिजू ने ट्विटर पर शेयर किया थीम सॉन्ग का वीडियो\n2020 गीत का नाम- 'लक्ष्य तेरा सामने है', खेल मंत्री ने 57 सेकंड का वीडियो किया शेयर`** |

## License (Starmie!)

<p align="center">
  <strong>MIT © <a href="https://github.com/junhoyeo">Junho Yeo</a></strong>
</p>

<p align="center">
  <a href="https://github.com/junhoyeo">
    <img src="https://github.com/junhoyeo/BetterOCR/raw/main/.github/images/starmie.jpg" width="256px" />
  </a>
</p>

If you find this project interesting, **please consider giving it a star(⭐)** and following me on [GitHub](https://github.com/junhoyeo). I code 24/7 and ship mind-breaking things on a regular basis, so your support definitely won't be in vain!
