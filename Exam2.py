# Alex Bello
# 4/13/2020
# Exam 2 for Advance Programing Tech

import random
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge
from Search_Methods import merge_sort
from Search_Methods import partition
from Search_Methods import quick_sort_recursion
from Search_Methods import quick_sort


Sorting_List = []


menu = 0


while menu != 6:
    print("Welcome to the menu! Select one of the six options below to pick how you want to sort the randomly made list!")
    print("1.Use the Bubble Sort method.")
    print("2.Use the Selection Sort method.")
    print("3.Use the Insertion Sort method.")
    print("4.Use the Merge Sort method.")
    print("5.Use the Quick Sort method.")
    print("6.Exit the menu.")
    menu = int(input(">"))

    if menu == 1:
        print("How many times do you want to add a number to the list?")
        times_to_run = int(input())
        for i in range(times_to_run):
            x = random.randint(0, 100000)
            Sorting_List.append(x)
            bubble_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()
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
            merge(Sorting_List)
            merge_sort(Sorting_List)
            print(Sorting_List)
    Sorting_List.clear()
