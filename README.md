## NeZha-Pytorch

pytorch版NEZHA，适配transformers

### 安装
> pip install git+https://github.com/yanqiangmiffy/Nezha-Pytorch.git
### 权重下载地址

https://github.com/lonePatient/NeZha_Chinese_PyTorch

###  torch使用样例
```
import torch
from transformers import BertTokenizer
from nezha import NeZhaModel, NeZhaConfig

text = "华为开源中文版BERT模型 NEZHA 哪吒。"
tokenizer = BertTokenizer.from_pretrained(
    "quincyqiang/nezha-cn-base"
)
model = NeZhaModel.from_pretrained(
    "quincyqiang/nezha-cn-base"
)

config = NeZhaConfig.from_pretrained(
    "quincyqiang/nezha-cn-base"
)
model.eval()
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
```
> quincyqiang/nezha-cn-base可以改成本地路径
