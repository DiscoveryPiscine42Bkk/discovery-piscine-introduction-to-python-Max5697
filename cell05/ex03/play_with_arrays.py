#!/usr/bin/python3

og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr =[x + 2 for x in og_arr]
fina_arr =[x for x in new_arr if x > 5]
end_arr = list(set(fina_arr))

print(og_arr)
print(end_arr)