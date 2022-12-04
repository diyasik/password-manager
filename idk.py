def save():
    data_field = f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()} \n"

    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"email: {username_entry.get()} \n"
                                                                      f"password: {password_entry.get()} \n"
                                                                      f"Press OK to continue")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(data_field)
            website_entry.delete(0, END)
            password_entry.delete(0, END)