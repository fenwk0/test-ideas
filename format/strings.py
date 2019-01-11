def create_command_001():
    command_template = "cmd_001 {param1} {param2} {param3}"
    return command_template.format(param1="one", param2="two", param3="three")


def create_command_002():
    command_template = "cmd_002 "\
                       + "{param1} "\
                       + "{param2} "\
                       + "{param3}"
    return command_template.format(param1="one", param2="two", param3="three")


def create_command_003():
    command_template = ("cmd_003 "
                        + "{param1} "
                        + "{param2} "
                        + "{param3}")
    return command_template.format(param1="one", param2="two", param3="three")


print(create_command_001())
print(create_command_002())
print(create_command_003())

