# Better OCR

<img src=".github/images/demo-0.webp" width="500px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `CHAINSAWMANChapter 109:The Easy Way to Stop Bullying~BV-THTSUKIFUUIMUTU ETT` |
| Tesseract | `A\ ira \| LT ge a TE ay NS\nye SE F Pa Ce YI AIG 44\nopr See aC\n; a) Ny 7S =u \|\n_ F2 SENN\n\ ZR\n3 ~ 1 A \ Ws —— “s 7 “A\n=) 24 4 = rt fl /1\n£72 7 a NS dA Chapter 109:77/ ¢ 4\nZz % = ~ oes os \| \STheEasf Way.to Stop Bullying:\n© Wa) ROT\n\n` |
| LLM | 🤖 GPT-3.5 |
| **Result** | **`CHAINSAWMAN\nChapter 109: The Easy Way to Stop Bullying`** |


<img src=".github/images/demo-1.png" width="500px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `JUST FOR YOU이런 분들께 추천드리는 퍼멘테이선 팬타인 아이켜어 크림매일매일 진해지논 다크서클올 개선하고 싶다면축축 처지논 피부름 탄력 잇게 바꾸고 싶다면나날이 늘어가는 눈가 주름올 완화하고 싶다면FERMENATION민감성 피부에도 사용할 수잇는 아이크림올 찾는다면얇고 예민한 눈가 주변 피부름 관리하고 싶다면`                                                                              |
| Tesseract | `9051 508 \ㅇ4\n이런 분들께 추천드리는 퍼멘테이션 타인 아이케어 크림\n.매일매일 진해지는 다크서클을 개선하고 싶다면        "도\nㆍ축축 처지는 피부를 탄력 있게 바꾸고 싶다면         7\nㆍ나날이 늘어가는 눈가 주름을 완화하고 싶다면        /\n-민감성 피부에도 사용할 수 있는 아이크림을 찾는다면    (프\nㆍ않고 예민한 눈가 주변 피부를 관리하고 싶다면                         밸\n\n` |
| LLM | 🤖 GPT-3.5 |
| **Result** | **`JUST FOR YOU 이런 분들께 추천드리는 퍼멘테이션 팬타인 아이케어 크림\n매일매일 진해지는 다크서클을 개선하고 싶다면\n축축 처지는 피부를 탄력 있게 바꾸고 싶다면\n나날이 늘어가는 눈가 주름을 완화하고 싶다면\n민감성 피부에도 사용할 수 있는 아이크림을 찾는다면\n얇고 예민한 눈가 주변 피부를 관리하고 싶다면`** |

<img src=".github/images/demo-2.png" width="400px" />

| Source | Text |
| ------ | ---- |
| EasyOCR | `바이오함보#세로모공존존세럼6글로우픽 설문단 100인이꼼꼼하게 평가햇어요"#누적 판매액 40억#제품만족도 1009` |
| Tesseract | `바이오힐보\n#세로모공폰폰세럼\n“글로 으피 석무다 1 00인이\n꼼꼼하게평가했어요”\n\n` |
| Context | `존존 -> 쫀쫀` |
| LLM | 🤖 GPT-4 |
| **Result** | **`바이오힐보\n#세로모공쫀쫀세럼\n“글로우픽 설문단 100인이 꼼꼼하게 평가했어요”\n#누적 판매액 40억\n#제품만족도 100%`** |
