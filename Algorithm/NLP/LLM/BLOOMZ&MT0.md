

[Crosslingual Generalization through Multitask Finetuning](https://arxiv.org/pdf/2211.01786.pdf)

[翻译：Crosslingual Generalization through Multitask Finetuning](https://zhuanlan.zhihu.com/p/612619041)



P3、xP3、xP3mt数据集介绍：https://github.com/bigscience-workshop/xmtf#data

| Name                                                         | Explanation                                                  | Example models                                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [xP3x](https://huggingface.co/datasets/Muennighoff/xP3x)     | Mixture of 17 tasks in 277 languages with English prompts    | WIP - Join us at Project Aya @[C4AI](https://cohere.for.ai/) to help! |
| [xP3](https://huggingface.co/datasets/bigscience/xP3)        | Mixture of 13 training tasks in 46 languages with English prompts | [bloomz](https://huggingface.co/bigscience/bloomz) & [mt0-xxl](https://huggingface.co/bigscience/mt0-xxl) |
| [xP3mt](https://huggingface.co/datasets/bigscience/xP3mt)    | Mixture of 13 training tasks in 46 languages with prompts in 20 languages (machine-translated from English) | [bloomz-mt](https://huggingface.co/bigscience/bloomz-mt) & [mt0-xxl-mt](https://huggingface.co/bigscience/mt0-xxl-mt) |
| [xP3all](https://huggingface.co/datasets/bigscience/xP3all)  | xP3 + evaluation datasets adding an additional 3 tasks for a total of 16 tasks in 46 languages with English prompts |                                                              |
| [xP3megds](https://huggingface.co/datasets/bigscience/xP3megds) | [Megatron-DeepSpeed](https://github.com/bigscience-workshop/Megatron-DeepSpeed) processed version of xP3 | [bloomz](https://huggingface.co/bigscience/bloomz)           |
| [P3](https://huggingface.co/datasets/Muennighoff/P3)         | Repreprocessed version of the English-only [P3](https://huggingface.co/datasets/bigscience/P3) with 8 training tasks | [bloomz-p3](https://huggingface.co/bigscience/bloomz-p3) & [mt0-xxl-p3](https://huggingface.co/bigscience/mt0-xxl-p3) |



[【自然语言处理】【大模型】BLOOM模型结构源码解析(单机版)](https://zhuanlan.zhihu.com/p/625911234)