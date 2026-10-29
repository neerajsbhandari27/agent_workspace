test_tool_code = """
def add():
    return 10 + 20
"""

# to store the function objects
namespace = {}


# exec(source, globals, locals)
# here, soucre is obv test_tool_code, globals is {"__builtins__": {}}, and locals is namespace
# globals  - "__builtins__" - restricts access to Python's built-in functions within the supplied global namespace
# this creates the function
exec(test_tool_code, {"__builtins__": {}}, namespace)

# retrives the function object from the namespace dictionary
tool_function = namespace["add"]

# call the function 
result = tool_function()

print(result)
print(namespace)