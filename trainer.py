import os
import json
import torch

from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling

from common.static.global_variable import GlobalVariable as gv
from util.custom_dataset import CustomDataset
from util.translate_prompt import prompt_chat_completion

def main(model_id, tokenizer_id=None):

    if tokenizer_id is None:
        tokenizer_id = model_id

    model = AutoModelForCausalLM.from_pretrained(model_id,
                                                 return_dict=True,
                                                 torch_dtype=torch.float16,
                                                 device_map='auto',
                                                 # load_in_8bit=True
                                                )
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_id)

    model.gradient_checkpointing_enable()
    model = prepare_model_for_kbit_training(model)

    config = LoraConfig(r=64,
                        lora_alpha=16,
                        target_modules=["q_proj","v_proj"],
                        lora_dropout=0.05,
                        bias="none",
                        task_type="CAUSAL_LM")

    model = get_peft_model(model, config)
    model.print_trainable_parameters()

    with open('./translation_data_science.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    split_data = []
    for i in range(len(data)):
        split_data.append(prompt_chat_completion(data[i]['conversations']))

    custom_dataset = CustomDataset(split_data, tokenizer, 4096)
    tokenizer.pad_token = tokenizer.eos_token
    trainer = Trainer(
        model=model,
        train_dataset=custom_dataset,
        args=TrainingArguments(
            per_device_train_batch_size=1,
            gradient_accumulation_steps=4,
            warmup_steps=2,
            max_steps=20,
            learning_rate=3e-4,
            fp16=True,
            logging_steps=1,
            output_dir="./output_dir",
            optim='adamw_hf'
        ),
        data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
    )

    model.config.use_cache = False
    trainer.train()
    trainer.save_model("./save_lora_dir")

if __name__=="__main__":
    main(os.path.join(gv.ROOT_PATH, f"llm_model/KO-Platypus2-7B-ex/"))