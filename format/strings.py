def create_command():
    command_template = "cmd {parma1} {param2} {param3}"
    return command_template.format(param1="one", param2="two", param3="three")


print(create_command())
