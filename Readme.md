# Can ChatGPT Defend its Belief in Truth? Evaluating LLM Reasoning via Debate

Original implementation of the paper "[Can ChatGPT Defend its Belief in Truth? Evaluating LLM Reasoning via Debate](https://arxiv.org/abs/2305.13160v2)" in Findings of EMNLP-23 by [Boshi Wang](https://boshi-wang.github.io/), [Xiang Yue](https://xiangyue9607.github.io/) and [Huan Sun](http://web.cse.ohio-state.edu/~sun.397/).

## Setup

Put your OpenAI API key in a file called "api_key.txt".

## Repo Tour
    .
    ├── grade-school-math/             # GSM8K (https://arxiv.org/abs/2110.14168)
    ├── prontoqa/                      # PrOntoQA (https://arxiv.org/abs/2210.01240)
    ├── commonsense/                   # commonsense reasoning, including StrategyQA, CommonsenseQA-2.0, and Creak
    └── BBH/                           # big-bench-hard (https://arxiv.org/abs/2210.09261)

- ```main.ipynb``` in each sub-directory contains the code and cached evaluation results.

## Citation
```
@inproceedings{wang2023can,
    title={Can ChatGPT Defend its Belief in Truth? Evaluating LLM Reasoning via Debate},
    author={Wang, Boshi and Yue, Xiang and Sun, Huan},
    booktitle={Findings of EMNLP},
    year={2023}
}
```