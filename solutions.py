#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KPO Lab1 - Codeforces Solutions
This file contains solutions for two Codeforces problems:
1. Problem 58A - Chat
2. Problem 112A - Petya and Strings
"""

def problem1():
    """حل المسألة 58A - Chat: هل يمكن تكوين كلمة hello من الكلمة المدخلة؟"""
    print("\n--- Problem 58A: Chat ---")
    s = input("Enter word: ").strip()
    
    target = "hello"
    j = 0
    
    for ch in s:
        if j < len(target) and ch == target[j]:
            j += 1
    
    if j == len(target):
        print("YES")
    else:
        print("NO")

def problem2():
    """حل المسألة 112A - Petya and Strings: مقارنة كلمتين مع تجاهل حالة الأحرف"""
    print("\n--- Problem 112A: Petya and Strings ---")
    s1 = input("Enter first word: ").strip().lower()
    s2 = input("Enter second word: ").strip().lower()
    
    if s1 < s2:
        print(-1)
    elif s1 > s2:
        print(1)
    else:
        print(0)

def show_menu():
    """عرض قائمة الاختيارات"""
    print("\n" + "=" * 50)
    print("           KPO Lab1 - Codeforces Solutions")
    print("=" * 50)
    print("1. Problem 58A - Chat")
    print("2. Problem 112A - Petya and Strings")
    print("3. Run both problems")
    print("4. Exit")
    print("=" * 50)

def main():
    """الدالة الرئيسية للبرنامج"""
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            problem1()
        elif choice == "2":
            problem2()
        elif choice == "3":
            problem1()
            print("\n" + "-" * 30)
            problem2()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()