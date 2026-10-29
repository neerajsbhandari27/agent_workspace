def tool_executor(tool_code: str, function_name: str):
    namespace = {}
    exec(tool_code, {"__builtins__": {}}, namespace)
    tool_function = namespace[function_name]
    return tool_function

def tool_executor(tool_code: str, function_name: str, params: dict):
    namespace = {}
    exec(tool_code, {"__builtins__": {}}, namespace)
    tool_function = namespace[function_name]
    return tool_function(**params)