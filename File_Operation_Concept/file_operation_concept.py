def update_file_configuration(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines() #copy everything the file in the variable

    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith(key):
                file.write(key + "=" + value +"\n")
            else:
                file.write(line)

update_file_configuration("server.config", "MAX_CONNECTIONS", "800")