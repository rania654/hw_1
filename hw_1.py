python = ["P","Y", "T", "H", "O", "N"]
empty = []
var = ""

def operation_backwards():
    for i in range(len(python)):
        empty.append(python[len(python)-1-i])
    return "".join(empty)

def push():
    for i in range(len(python)):
        empty.append(python[i])
    return empty

def pop(var):
    for i in range(len(empty)):
        var = var + empty.pop(-1)
    return var
        

print(f"Fun Fact! Python backwards is {operation_backwards()}!")
print(push())
print(pop(var))
