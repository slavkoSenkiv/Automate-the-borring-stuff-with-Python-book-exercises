import webbrowser
address = input('enter address...')
address = address.replace(' ', '+')
webbrowser.open(f'https://www.google.com.ua/maps/place/{address}')
print(f'https://www.google.com.ua/maps/place/{address}')
