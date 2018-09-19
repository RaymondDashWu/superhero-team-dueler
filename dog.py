class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration
    def sleep(self):
        print("{} sleeps for {} hours".format(self.name, self.sleep_duration))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()







# class Dog:
#     greeting = "Woof!"

#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.greeting)

# my_dog = Dog("Spot")
# my_dog.bark()
# print(my_dog.name)
# print(__name__)

# if __name__ == "__main__":
#     my_dog = Dog("Spot")
#     my_dog.bark()

# my_other_dog = Dog("Annie")
# print(my_other_dog.name)

# my_first_dog = Dog("Annie")
# my_second_dog = Dog("Wyatt")

# print(my_first_dog.name)
# print(my_second_dog.name)

# my_first_dog.bark()
# my_second_dog.bark()