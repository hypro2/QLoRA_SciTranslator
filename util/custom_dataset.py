# CustomDataset 정의
from torch.utils.data import Dataset


class CustomDataset(Dataset):
    def __init__(self, data, tokenizer, max_sequence_length):
        self.data = data
        self.tokenizer = tokenizer
        self.max_sequence_length = max_sequence_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        conversation = self.data[idx]
        prompt_templete = conversation

        # 텍스트를 토큰화하고 인코딩
        encoding = self.tokenizer(
            prompt_templete,
            truncation=True,
            max_length=self.max_sequence_length,
            return_tensors='pt'
        )

        input_ids = encoding['input_ids'].squeeze()
        attention_mask = encoding['attention_mask'].squeeze()

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask
        }
