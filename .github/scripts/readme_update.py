"""
This script updates the README to have accurate language percentages for the badges.
It should be run via GitHub actions.
"""
import requests

req = requests.get("https://api.github.com/repos/cosmognaut/magpie/languages")
req_dict = req.json()
all_numbers = list(req_dict.values())
total = 0
for number in all_numbers:
    total += number

py_total = req_dict['Python']
sv_total = req_dict['Svelte']

final_percentage_python = (int(py_total) / total) * 100
final_percentage_svelte = (int(sv_total) / total) * 100

python_string = f"{round(final_percentage_python, 1)}"
svelte_string = f"{round(final_percentage_svelte, 1)}"

with open('../../README.md', 'r') as file:
    data = file.read()

start_index = data.find('<!--START_LANG-->')
end_index = data.find('<!--END_LANG-->')

svelte_line = f'\t<a href="https://api.github.com/repos/cosmognaut/magpie/languages"><img src="https://img.shields.io/badge/Svelte-{svelte_string}%25-ff3e00" alt="Svelte percentage" /></a>\n'

python_line = f'\t<a href="https://api.github.com/repos/cosmognaut/magpie/languages"><img src="https://img.shields.io/badge/Python-{python_string}%25-3776ab" alt="Python percentage" /></a>\n'

html_lines = svelte_line + python_line

data = data[:start_index] + '<!--START_LANG-->\n' + html_lines + data[end_index:]

with open('../../README.md', 'w') as file:
    file.write(data)
