phones = {'a': '123456'}
print("my phone is {a}".format_map(phones))

args = {'title': 'hello', 'body': 'word'}

html = '<html><title>{title}</title><body>{body}</body></html>'
print(html.format_map(args))