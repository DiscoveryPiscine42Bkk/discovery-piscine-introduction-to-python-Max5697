#!/usr/bin/python3

first_word = input("What you gotta say? : ")
sec_word = input("I got that! Anything else? : ")
end_word = "STOP"

while True:
    sec_word = input("I got that! Anything else? : ")
    if sec_word == end_word:
        break