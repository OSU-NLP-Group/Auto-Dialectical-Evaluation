#!/usr/bin/env python
# coding: utf-8

import os
import openai
import json
import jsonlines
import re
import numpy as np
import argparse
import time
from termcolor import colored
import matplotlib.pyplot as plt
from copy import deepcopy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default=None, type=str, required=True, help="")
    args = parser.parse_args()
    print(args)

    with open("../../api_key.txt", "r") as f:
        openai.api_key = f.read().strip()

    with open("bbh_selected/{}.json".format(args.dataset), "r", encoding='utf-8') as f:
        item_list = json.load(f)['examples']
        for i in range(len(item_list)):
            item = item_list[i]
            assert set(item.keys()) == {'input', 'target'}
            item['question'] = item['input']
            item['answer'] = item['target']
            del item['input'], item['target']
            item_list[i] = item
    print("#examples:", len(item_list))

    for i in range(len(item_list)):
        print(i)
        item = item_list[i]
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Think step by step and provide a correct and thoughtful answer (yes or no) to the given question with explanations. State your final answer in the last sentence in your response, beginning with \"So the answer is yes/no\". Try to make your solution concise."},
            {"role": "assistant", "content": "Sure, I'd be happy to help! Can you please provide me with the question?"}
        ]
        
        # add question
        messages.append({"role": "user", "content": item['question']})
        
        while True:
            try:
                # get CoT/SC response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0,
                    max_tokens=512,
                    n=1
                )
                item['prediction_CoT_turbo'] = response['choices'][0]['message']['content'].strip()
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=1,
                    max_tokens=512,
                    n=9
                )
                item['prediction_SC_turbo'] = [response['choices'][i]['message']['content'].strip()
                                               for i in range(len(response['choices']))]
                
                item_list[i] = item
                break
            except:
                print("error during index", i)
                time.sleep(5)

    with open("item_list_{}.json".format(args.dataset), "w", encoding='utf-8') as f:
        json.dump(item_list, f)


if __name__ == '__main__':
    main()
