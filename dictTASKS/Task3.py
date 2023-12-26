import webbrowser

# URL-адреса, которые вы хотите открывать
urls = ['https://t.me/anutkaaxv', 'https://t.me/annnaax']
# Количество повторений
num_repeats = 500

# Цикл с ограничением по количеству повторений
for _ in range(num_repeats):
    for url in urls:
        webbrowser.open_new_tab(url)