def check_list(incomplete_list, highest_list_value):
    return [element for element in range(1, highest_list_value + 1) if element not in incomplete_list]
