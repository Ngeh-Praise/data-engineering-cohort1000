count=0
def update_counter():
    global count
    count += 1
    return count
update_counter()
update_counter()
update_counter()
print(count)