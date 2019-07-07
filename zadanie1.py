def create_post_office_code(first_post_office_code, last_post_office_code):
    generated_post_office_code = []

    start_post_office_code = int(first_post_office_code.replace("-", ""))
    end_post_office_code = int(last_post_office_code.replace("-", ""))

    for post_office_code in range(start_post_office_code, end_post_office_code + 1):
        generated_post_office_code.append(str(post_office_code)[:2] + "-" + str(post_office_code)[2:])

    return generated_post_office_code
