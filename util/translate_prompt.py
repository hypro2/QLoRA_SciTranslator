
def prompt_chat_completion(dialog, system_token="### System:", user_token="### Instruction:", assistant_token="### Response:", start_token="", end_token=""):
  
    role_dict = {"system": system_token, "human": user_token, "gpt": assistant_token}
    dialog_text = [f"""{role_dict[prompt['from']]}
{start_token}{prompt['value'].strip()}{end_token}
번역해라

{role_dict[answer['from']]}
{start_token}{(answer['value']).strip()}{end_token}</s>""" for prompt, answer in zip(dialog[::2], dialog[1::2])]
    dialog_tokens = ''.join(dialog_text).replace('\n\n</s>', '</s>')

    if '다음 문장을 영어로 번역하라:' in dialog_tokens:
        dialog_tokens = dialog_tokens.replace('다음 문장을 영어로 번역하라: ', "").replace("번역해라", "Translate")
      
    elif "Translate this sentence into Korean:" in dialog_tokens:
        dialog_tokens = dialog_tokens.replace('Translate this sentence into Korean: ', "")

    return f'<s>{dialog_tokens}'
