#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:36:29 2024

@author: kevin
"""
from openai import OpenAI
def prompt(client,prom):
    with open("query.txt",'r') as file:
        string = file.readlines()
        fine_query = ""
        for i in string:
            fine_query += i.strip() + " "
        file.close()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": fine_query},
    {"role": "user", "content": prom}])
    return completion.choices[0].message.content
