# DPT-Agent

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sjtu-marl/DPT-Agent)

This is the official implementation of paper ["Leveraging Dual Process Theory in Language Agent Framework for Simultaneous Human-AI Collaboration"](https://arxiv.org/abs/2502.11882) accepted by ACL 2025 Main.

![image](assets/intro.png)

<p align="center">
  📄 <a href="https://arxiv.org/pdf/2502.11882" target="_blank">Paper</a> &nbsp; | &nbsp;
  🌐 <a href="https://sjtu-marl.github.io/DPT-Agent-page/" target="_blank">Website</a> &nbsp; | &nbsp;
  📘 <a href="https://mp.weixin.qq.com/s/dT9KQmebVJX0ewkzJmisPg" target="_blank">机器之心</a> &nbsp; | &nbsp;
  🧪 <a href="https://agi-eval.cn/evaluation/detail?id=56" target="_blank">AGI-Eval</a>
</p>

## 🔥News

- [2025/05/16] The DPT-agent paper has been accepted by ACL 2025!
- [2025/03/18] Our work is featured by [机器之心](https://mp.weixin.qq.com/s/dT9KQmebVJX0ewkzJmisPg) on Wechat!
- [2025/03/06] We have established a partnership with [AGI-Eval](https://agi-eval.cn/mvp/home) platform. The benchmark results of Overcooked Challenge are now available on [AGI-Eval-Overcooked Challenge](https://agi-eval.cn/evaluation/detail?id=56). 


# Overcooked Challenge
![layout](assets/overcooked.png)

# DPT-Agent Framework
![Image 1](assets/framework.png)

# Results

![Exp1](assets/exp1.png)

![Exp2](assets/exp2.png)

# Usage

## Installation

Create a new environment
```
conda create -n dptagent python=3.10 -y   # support python<=3.10
conda activate dptagent


# Install pytorch
# We do not need gpu
pip install torch torchvision torchaudio

# Installing dependencies

bash ./install.sh
```
## Running Instructions

### Set up LLMs

```
litellm -c llms/litellm/config.yml --port 40000

# check health
curl --location 'http://127.0.0.1:40000/health' -H "Authorization: Bearer sk-1234"
```


### Run LLM as Indenpendent System 1 and System 2 Experiments
For single agent exp, first change the config/envs/overcooked.yaml

```
mode: burger_exp1
...
num_agents: 1
```
Then run:
```
sh scripts/exp0/openai.sh
```

### Run Single Agent Experiments
For single agent exp, first change the config/envs/overcooked.yaml

```
mode: burger_exp1
...
num_agents: 1
```
Then run:
```
sh scripts/exp1/openai.sh
```

### Run Collaboration Experiments with Rule-baed Agents
For collaboration exp, first change the config/envs/overcooked.yaml

```
mode: burger_exp1
...
num_agents: 2
```
Then run:
```
sh scripts/exp2/openai.sh
```

### Run Human Experiment
For use map 2, change the config/envs/overcooked.yaml
```
mode: burger_aa_new
...
num_agents: 2
```
Then run:
```
sh scripts/overcooked/human_llm_app.sh
```
Then open the website http://localhost:5001

### Help
For more information, please run

```shell
python llm_agent_run_act.py --help
```


## Developing Guide

We recommend using pre-commit to unify the format before commit.

```
# Init
pre-commit install

# You can run manually (maybe multiple times)
pre-commit run --all-files

# or it will automatically run when you try to commit, which is slow and seems stuck.
```

## Cite
```
@inproceedings{zhang-etal-2025-leveraging,
    title = "Leveraging Dual Process Theory in Language Agent Framework for Real-time Simultaneous Human-{AI} Collaboration",
    author = "Zhang, Shao  and Wang, Xihuai  and Zhang, Wenhao  and Li, Chaoran  and Song, Junru  and Li, Tingyu  and Qiu, Lin  and Cao, Xuezhi  and Cai, Xunliang  and Yao, Wen  and Zhang, Weinan and Wang, Xinbing  and Wen, Ying",
    editor = "Che, Wanxiang  and Nabende, Joyce  and Shutova, Ekaterina  and Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.206/",
    doi = "10.18653/v1/2025.acl-long.206",
    pages = "4081--4108",
    ISBN = "979-8-89176-251-0",
}
```
