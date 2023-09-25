#!/usr/bin/env python
# coding: utf-8

# In[34]:


import random
empty_board= []
slot_matchine = [[3,2,1]]
win_count =0

number_of_slot = int(input('Enter number of slots: '))
max_slot_value = int(input('Enter Max slot value: '))


def generate_slot_values(number_of_slot, max_slot_value):
    slots = []
    for i in range(number_of_slot):
        x = random.randint(1, max_slot_value)
        slots.append(x)
    
    return slots

number_of_tries = int(input('Enter the number of tries: '))


for i in range(number_of_tries):
    slots = generate_slot_values(number_of_slot,max_slot_value)
    empty_board.append(slots)
    
    matched_slots = slots.count(slots[0])
    
    if len(slots) == matched_slots:
        win_count += 1
        print(f'Courrent slots: {slots} and YOU WIN')
    else:
        print(f'Courrent slots: {slots} and YOU LOSS')
        

