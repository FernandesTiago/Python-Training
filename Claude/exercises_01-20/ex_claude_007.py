# global

x = 10
def my_function():
    global x
    x = 20

my_function()
print(x)  # now it will print 20
