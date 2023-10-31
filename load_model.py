import os
import gc
import sys
from typing import List
import time
import torch

from nltk.tokenize import sent_tokenize
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
from peft import PeftModel, PeftConfig

class LlamaTranslate():

    def __init__(self, model_name = '', split_token="### Response:"):
        self.model_name = model_name
        self.split_token = split_token
        self.model_name_or_path: str = os.path.join(gv.ROOT_PATH, f"llm_model/{self.model_name}/")

    def translate_completion(self, prompt):
        prompt_templete = f"""### Instruction:\n\n{prompt}\n번역해라\n\n### Response:"""
        return prompt_templete

    def chat(self, prompt):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        model = AutoModelForCausalLM.from_pretrained(self.model_name_or_path,
                                                     return_dict=True,
                                                     torch_dtype=torch.float16,
                                                     device_map='auto',
                                                     do_sample=True,
                                                     # load_in_8bit=True
                                                     )

        model = PeftModel.from_pretrained(model, os.path.join(gv.ROOT_PATH, f"llm_model/{self.model_name}_LoRA/"))
        print(model)
        prompt_templete = self.translate_completion(prompt)
        input_ids = tokenizer(prompt_templete, max_length=2048, truncation=True, return_tensors='pt').input_ids.cuda()
        output = model.generate(inputs=input_ids,
                                max_new_tokens=1024,
                                streamer=TextStreamer(tokenizer),
                                repetition_penalty=1.1,
                                temperature=0.01)

        decode_output = tokenizer.decode(output[0])
        decode_output = decode_output.split(self.split_token)[1]
        decode_output = decode_output.replace("</s>", "")
        result = decode_output.strip()

        model.to("cpu")
        del model
        torch.cuda.empty_cache()
        gc.collect()

        return result


if __name__ == '__main__':
  
    trans = LlamaTranslate()
  
    print(trans.chat("""Based on the provided dataset, I have analyzed the patent trends over time and identified notable changes in technology and technical terminology. The dataset spans from 2017 to 2023, allowing us to observe the evolution of various technologies and innovations during this period.
1. Early years (2017-2018):
The early years of the dataset show a focus on improving existing technologies, such as organic light-emitting diodes (OLEDs), plasma display panels (PDPs), and flexible electrophoresis displays. There is also a growing interest in emerging technologies like micro-LEDs and quantum dot light-emitting diodes (QLEDs). Additionally, there is an emphasis on developing new materials and techniques for improving display quality, such as four-dimensional light field technology and diffuser films.
2. Advancements in display technology (2019-2020):
The years 2019 and 2020 witness a significant increase in patents related to display technology, particularly in the development of micro-LEDs, QLEDs, and OLEDs. There is also a growing interest in improving display panel technology, with a focus on developing thinner, more flexible, and more efficient displays. This period also sees the emergence of new technologies like p-channel type thin film transistors and oxide semiconductors.
3. Advancements in fingerprint recognition technology (2020):
In 2020, there is a notable increase in patents related to fingerprint recognition technology, specifically in the development of fingerprint recognition sensors and p-channel type thin film transistors. This suggests a growing interest in improving biometric authentication technology.
4. Emergence of new technologies (2021-2023):
The final years of the dataset show a significant increase in patents related to emerging technologies like flexible display technology, curved-surface display panels, and level scan signal sk-1 output. There is also a growing interest in improving existing technologies like micro-LEDs and QLEDs. Additionally, there is a focus on developing new materials and techniques for improving display quality, such as data compensation voltages and multiplexing circuits.
In summary, the patent trends over time indicate a significant evolution in display technology, with a focus on improving existing technologies and developing new ones. There is also a growing interest in emerging technologies like fingerprint recognition, flexible displays, and curved-surface display panels. The dataset suggests that there has been a steady advancement in technology over the years, with a focus on improving efficiency, flexibility, and display quality."""))
