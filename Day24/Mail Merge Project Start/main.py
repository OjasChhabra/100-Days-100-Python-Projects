with open(r"Day24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    content = file.read()

with open(r"Day24\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    name_list = file.readlines()

for name in name_list:
    stripped_name = name.strip()
    update_content = content.replace("[name]", stripped_name)
    with open(fr"Day24\Mail Merge Project Start\Output\{stripped_name}.txt", "w") as file:
        file.write(update_content)
