# llama_science_translator_ko(임시)

학습 진행 중
```
{
  "auto_mapping": null,
  "bias": "none",
  "fan_in_fan_out": false,
  "inference_mode": true,
  "init_lora_weights": true,
  "layers_pattern": null,
  "layers_to_transform": null,
  "lora_alpha": 16,
  "lora_dropout": 0.05,
  "modules_to_save": null,
  "peft_type": "LORA",
  "r": 64,
  "revision": null,
  "target_modules": [
    "q_proj",
    "v_proj"
  ],
  "task_type": "CAUSAL_LM"
}
```

![image](https://github.com/hypro2/llama_translator_koen/assets/84513149/13ef97cc-27e8-4008-8d2d-95d513df6342)

## Test Case 1
lora 1000 step

원문
```
Based on the provided dataset, I have analyzed the patent trends over time and identified notable changes in technology and technical terminology. The dataset spans from 2017 to 2023, allowing us to observe the evolution of various technologies and innovations during this period.
1. Early years (2017-2018):
The early years of the dataset show a focus on improving existing technologies, such as organic light-emitting diodes (OLEDs), plasma display panels (PDPs), and flexible electrophoresis displays. There is also a growing interest in emerging technologies like micro-LEDs and quantum dot light-emitting diodes (QLEDs). Additionally, there is an emphasis on developing new materials and techniques for improving display quality, such as four-dimensional light field technology and diffuser films.
2. Advancements in display technology (2019-2020):
The years 2019 and 2020 witness a significant increase in patents related to display technology, particularly in the development of micro-LEDs, QLEDs, and OLEDs. There is also a growing interest in improving display panel technology, with a focus on developing thinner, more flexible, and more efficient displays. This period also sees the emergence of new technologies like p-channel type thin film transistors and oxide semiconductors.
3. Advancements in fingerprint recognition technology (2020):
In 2020, there is a notable increase in patents related to fingerprint recognition technology, specifically in the development of fingerprint recognition sensors and p-channel type thin film transistors. This suggests a growing interest in improving biometric authentication technology.
4. Emergence of new technologies (2021-2023):
The final years of the dataset show a significant increase in patents related to emerging technologies like flexible display technology, curved-surface display panels, and level scan signal sk-1 output. There is also a growing interest in improving existing technologies like micro-LEDs and QLEDs. Additionally, there is a focus on developing new materials and techniques for improving display quality, such as data compensation voltages and multiplexing circuits.
In summary, the patent trends over time indicate a significant evolution in display technology, with a focus on improving existing technologies and developing new ones. There is also a growing interest in emerging technologies like fingerprint recognition, flexible displays, and curved-surface display panels. The dataset suggests that there has been a steady advancement in technology over the years, with a focus on improving efficiency, flexibility, and display quality.
```

번역1: 미 적용
```
이 데이터 세트에 따르면, 분석을 기반으로 한 시간의 경과에 따른 특허 트렌드를 분석하고 기술 및 기술 용어에 주목할 만한 변화가 있음을 발견했습니다. 이 데이터 세트는 2017년부터 2023년까지 다양한 기술과 혁신을 관찰할 수 있는 기간인 2017년부터 2023년까지를 포함합니다.
1. 초기(2017-2018):
초기 데이터 세트에는 기존 기술인 유기 발광 다이오드(OLED), 플라즈마 디스플레이 패널(PDP) 및 유연 전기 전도성 디스플레이의 개선을 위한 새로운 소재와 기술을 개발하는 데 초점을 맞추는 경향이 있습니다. 또한 마이크로 LED와 양자점 발광 다이오드(QLED)와 같은 신흥 기술에 대한 관심이 증가하고 있습니다. 또한 4차원 광학 필드 기술과 확산 필름과 같은 디스플레이 품질을 개선하기 위해 새로운 재료와 기술을 개발하는 데 중점을 두는 등 디스플레이 기술에 대한 강조가 있습니다.
2. 디스플레이 기술의 발전(2019-2020):
2019년과 2020년에 마이크로 LED, QLED, OLED와 같은 디스플레이 기술 개발에 대한 특허 출원이 크게 증가합니다. 디스플레이 패널 기술에 대한 관심이 증가하면서 더 얇고, 더 유연하며, 더 효율적인 디스플레이를 개발하는 데 집중됩니다. 이 기간 동안 새로운 기술인 p-채널형 박막 트랜지스터와 산화물 반도체도 등장합니다.
3. 지문 인식 기술의 발전(2020):
2020년에는 지문 인식 센서 개발과 p-채널형 박막 트랜지스터에 대한 특허 출원이 눈에 띄게 증가합니다. 이는 생체인증 기술의 개선을 위한 증가하는 관심을 보여줍니다.
4. 새로운 기술의 출현(2021-2023):
데이터 세트의 마지막 몇 년 동안에는 유연 디스플레이 기술, 곡면 표면 디스플레이 패널, 레벨 스캔 신호 처리와 같은 새로운 기술에 대한 특허 출원이 눈에 띄게 증가합니다. 기존의 기술인 마이크로 LED와 QLED에 대한 관심이 증가함에 따라 기존 기술을 개선하려는 노력이 계속되고 있습니다. 또한 데이터 보정 전압과 다중화 회로와 같은 디스플레이 품질을 개선하기 위한 새로운 소재와 기술을 개발하는 데 중점을 두는 등 디스플레이 품질 향상을 위한 새로운 재료와 기술을 개발하는 데 중점을 두고 있습니다.
결론적으로, 시간의 경과에 따른 특허 트렌드는 기존 기술을 개선하고 새로운 기술을 개발하는 데 초점을 맞춘 디스플레이 기술의 지속적인 진화를 보여줍니다. 마이크로 LED, QLED와 같은 신흥 기술에 대한 관심뿐만 아니라 유연 디스플레이 기술, 곡면 표면 디스플레이 패널과 같은 새로운 기술에 대한 관심도 증가하고 있습니다. 이 데이터 세트는 시간이 지남에 따라 기술의 꾸준한 진보가 있었으며, 효율성, 유연성 및 디스플레이 품질 향상에 중점을 둔다는 것을 시사합니다.

```

번역2: LoRA 적용
```
제공된 데이터셋을 기반으로 시간의 흐름에 따른 특허 동향을 분석하고 기술 및 기술 용어에서 주목할 만한 변화를 식별하였다. 데이터셋은 2017년부터 2023년까지를 포함하며 이 기간 동안 다양한 기술과 혁신이 어떻게 진화해 왔는지 관찰할 수 있다.
초기(2017~2018년):
데이터셋 초기에는 기존 기술을 개선하는 데 초점을 맞추는 경향이 있으며, 유기발광다이오드(OLED)와 플라즈마 디스플레이 패널(PDP) 그리고 유연 전극분사 디스플레이 등과 같은 기존의 기술에 대한 관심이 증가한다. 또한 마이크로 LED나 양자점 발광 다이오드(QLED)와 같이 최근 떠오르는 기술에 대한 관심도 증가한다. 또한, 4차원 광장 기술이나 확산 필름 등과 같은 디스플레이 품질 개선을 위한 새로운 소재 및 기법에 대한 강조가 나타난다.
디스플레이 기술의 발전(2019~2020년):
2019년과 2020년에는 디스플레이 기술에 관한 특허 출원이 크게 증가하는데 특히 마이크로 LED, QLED, OLED 등에 대한 개발이 두드러진다. 또한 디스플레이 패널 기술의 발전에 초점이 맞춰지며 얇고 더 유연하며 효율적인 디스플레이 개발에 대한 관심이 증가한다. 이 시기에는 박막 트랜지스터와 산화물 반도체와 같은 새로운 기술이 등장하기도 한다.
터치 센서 기술의 발전(2020년):
2020년에는 터치 센서 기술에 관한 특허 출원이 눈에 띄게 증가하는데 특히 지문 인식 센서와 박막 트랜지스터에 대한 개발이 두드러진다. 이는 생체인증 기술의 향상을 위한 관심의 증대를 보여준다.
신기술의 등장(2021~2023년):
데이터셋의 마지막 3년은 신기술의 등장을 보여주는 특허 출원의 증가가 두드러지는데 특히 곡면 표시장치 패널과 다층 스캔 신호 출력 등과 같은 유연한 디스플레이 기술에 대한 관심이 증가한다. 또한 기존 기술의 향상에도 관심을 기울이며 마이크로 LED와 QLED와 같은 기술에 대한 개발도 증가한다. 또한 기존 기술의 향상에 초점을 맞추며 데이터 보정 전압과 다중화 회로와 같은 디스플레이 품질 향상을 위한 새로운 소재 및 기법을 개발하려는 노력도 보인다.
결론적으로 시간의 흐름에 따른 특허 동향은 기존 기술의 향상에 초점을 맞추면서 신기술의 개발을 추구한다는 것을 보여준다. 또한, 지문 인식, 유연한 디스플레이, 곡면 표시장치 패널과 같은 신기술에 대한 관심이 증가하고 기존 기술의 향상에도 관심을 기울이는 모습을 보여준다. 데이터셋은 이러한 추세가 꾸준히 진행되어 왔으며 효율성, 유연성, 디스플레이 품질 향상에 초점을 맞춘다는 것을 보여준다.

```

분석 결과 
```
특허문서에 대한 트렌드 분석 번역일 때, 어느 것이 더 좋은 번역인가?

번역1과 번역2 모두 전반적으로 정확하고 이해하기 쉽게 원문을 번역한 것으로 보입니다. 그러나 미묘한 차이가 있습니다. 번역1은 좀 더 간결한 표현을 사용하고, 문장 구조가 더 간결합니다. 번역2는 일부 부분에서 더 자세한 설명을 포함하고 더 긴 문장 구조를 가지고 있습니다.
따라서, 어떤 번역이 더 좋은 번역인지는 사용하는 맥락과 목적에 따라 달라질 수 있습니다. 간결한 요약이 필요한 경우에는 번역1이 적합할 수 있고, 더 상세한 정보와 설명이 필요한 경우에는 번역2가 더 적합할 수 있습니다. 이를 고려하여 번역을 선택하실 때 문서의 목적과 독자 대상을 고려하실 것을 권장합니다. 특허문서의 경우, 상세한 정보와 정확성이 중요하므로 번역2가 더 좋은 번역으로 간주될 수 있습니다. 번역2는 더 많은 기술 용어와 세부 내용을 포함하고 있으며, 특허 문서의 내용을 더 자세히 설명하고 있습니다. 이는 특허 분야에서 중요한 정보를 누락하지 않고 전달하는 데 도움이 될 것입니다.
따라서, 특허문서에 대한 트렌드 분석 번역을 수행할 때는 번역2가 더 적합한 선택으로 보입니다.

```
