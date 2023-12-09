---
title: huggingface_2023_12_09
date: 2023-12-09 20:01:14
tags:
    - MLDL
    - 工具及入门
---

需要install transformers 库
及拥有cuda 核心
pipeline 是hugging face 的基础工具，端到端的工具



```python
from transformers import pipeline
classifier = pipeline("sensiment-analysis")

tes1 = classifier("the book seems interesting!")
print(tes1)
```


```python
print(pipeline("sensiment-analysis")("the book seems interesting!"))
```

需要注册一个huggingface账号, then You can create a repository from the CLI (skip if you created a repo from the website)
![](https://pic1.zhimg.com/80/v2-34c7899303bf1b5014bef9864c924d52_1440w.png)



```python
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# You can replace this embedding with your own as well.

speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
```


```python
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
from datasets import load_dataset

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

inputs = processor(text="Hello, my dog is cute.", return_tensors="pt")

# load xvector containing speaker's voice characteristics from a dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

sf.write("speech.wav", speech.numpy(), samplerate=16000)
```