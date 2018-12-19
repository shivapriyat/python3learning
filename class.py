#!/usr/bin/env python3

class Duck:
    name='duck'

    def quack(self):
        print('{} is quacking'.format(self.name))
    def walk(self):
        print('{} is walking'.format(self.name))


def main():
    donald=Duck()
    donald.name='Donald'
    donald.quack()
    donald.walk()
    newDuck=Duck()
    newDuck.quack()
    newDuck.walk()

if __name__=='__main__':main()