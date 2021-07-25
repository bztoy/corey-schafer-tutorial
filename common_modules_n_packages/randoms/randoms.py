from utilities import (space, separated, start, end, sub, new_topic)
import random

# Key
key = 'randoms_basic'

# Dummy data
# Security purpose


def run():
    start('Random Module')

    new_topic('Random value')
    for i in range(4):
        value = random.random()
        print(f'loop {i + 1}: {value}')

    new_topic('Random value with uniform', True)
    value = random.uniform(1, 10)
    print(value)

    new_topic('Random Integer', True)
    for i in range(4):
        value = random.randint(1, 8)
        print(f'loop {i + 1}: {value}')

    new_topic('Random Choice', True)
    greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
    for i in range(2):
        value = random.choice(greetings)
        print(f'loop {i + 1}: {value}')

    new_topic('Random Choices', True)
    colors = ['Red', 'Orange', 'Pink', 'Green', 'Yellow']
    values = random.choices(colors, k=8)
    print(values)

    new_topic('Random Choices - weights option', True)
    colors = ['Red', 'Orange', 'Green', 'Yellow']
    values = random.choices(colors, weights=[3, 15, 10, 5], k=12)
    print(values)

    new_topic('Random Shuffle list', True)
    desk = list(range(1, 53))
    for i in range(2):
        value = random.shuffle(desk)
        print(f'loop {i + 1}: {desk}')

    new_topic('Random Sample', True)
    desk = list(range(1, 53))
    for i in range(2):
        hand = random.sample(desk, k=5)
        print(f'loop {i + 1}: {hand}')

    end()
