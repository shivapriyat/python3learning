#!/usr/bin/env python3
def main():
    # named arguments
    print('named arguments')
    kitten(tom='meow',rose='purr',kitty='grr')
    #named args passed as dictionary using 2star
    print('named args passed as dictionary 2 star')
    keywords=dict(tom='meow',rose='purr',kitty='grr')
    kitten(**keywords)
    # named args passed as dictionary using 1 star should give error
    print('named args passed as dictionary 1 star')
    keywords = dict(tom='meow', rose='purr', kitty='grr')
    kitten(*keywords)

def kitten(**kwargs):
    if len(kwargs):
        for key in kwargs:
            print(f'\tkitten {key} says {kwargs[key]}')
if __name__ == '__main__':main()
