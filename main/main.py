from main.gen import generate_qr_code

link = input("Please enter the link that you want a qr code: ") 
name = input("What is this link for: ")

generate_qr_code(link, name)