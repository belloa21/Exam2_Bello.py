# Alex Bello
# 4/13/2020
# Exam 2 for Advance Programing Tech

import random
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge_sort
from Search_Methods import quick_sort

# This is the blank list we will use for all the sorting methods
Sorting_List = []


menu = 0

# The menu will loop back until a valid option is selected in which case it will take the the user to right sort method code
while menu != 6:
    print("Welcome to the menu! Select one of the six options below to pick how you want to sort the randomly made list!")
    print("When you select a sort method the list will clear in case anything is in there before you insert random numbers.")
    print("1.Use the Bubble Sort method.")
    print("2.Use the Selection Sort method.")
    print("3.Use the Insertion Sort method.")
    print("4.Use the Merge Sort method.")
    print("5.Use the Quick Sort method.")
    print("6.Exit the menu.")
    menu = int(input(">"))

    if menu == 1:
        print("How many times do you want to add a number to the list?")
        # The times_to_run is what is used to give the user the option of
        # how many times they want the random.randint to run
        times_to_run = int(input())
        for i in range(times_to_run):
            # This is the range of numbers that can be randomly selected
            x = random.randint(0, 100000)
            # Adds the numbers to the list
            Sorting_List.append(x)
            bubble_sort(Sorting_List)
            print(Sorting_List)
    # Clears the list
    # This being outside the functions allows it to be repeated after each sort option,
    # not just this one
    Sorting_List.clear()
    # This only shows up here because it repeats after each menu option
    # It also gives the visual to the user that the list is now empty
    print("We just cleared the list so you can try other sorts or try this type again.")
    print(Sorting_List)

    if menu == 2:
        print("How many times do you want to add a number to the list?")
        times_to_run = int(input())
        for i in range(times_to_run):
            x = random.randint(0, 100000)
            Sorting_List.append(x)
            selection_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()

    if menu == 3:
        print("How many times do you want to add a number to the list?")
        times_to_run = int(input())
        for i in range(times_to_run):
            x = random.randint(0, 100000)
            Sorting_List.append(x)
            insertion_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()

    if menu == 4:
        print("How many times do you want to add a number to the list?")
        times_to_run = int(input())
        for i in range(times_to_run):
            x = random.randint(0, 100000)
            Sorting_List.append(x)
            merge_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()

    if menu == 5:
        print("How many times do you want to add a number to the list?")
        times_to_run = int(input())
        for i in range(times_to_run):
            x = random.randint(0, 100000)
            Sorting_List.append(x)
            quick_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()
