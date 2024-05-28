import os
import json
import random
from collections import defaultdict

if __name__ == '__main__':
    modes = ['entity', 'inter-sent', 'intra-sent']
    splits = ['train_annotated', 'dev', 'test']
    seed = 42
    random.seed(seed)

    for split in splits:
        items_dict = defaultdict(list)
        for mode in modes:
            data = [json.loads(line) for line in open(os.path.join(mode, f"{split}.jsonl")).readlines()]
            for item in data:
                title = item['title']
                items_dict[title].append(item)
        save_name = f"{split}.jsonl"
        with open(save_name, 'w', encoding='utf-8') as f:
            for title in items_dict:
                items = items_dict[title]
                item = random.choice(items)
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
