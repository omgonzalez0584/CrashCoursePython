#Processing a API response
import requests
import pygal
from  pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

#Make an API call and store th response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code: ',r.status_code)

#Store API response in a variable
response_dic = r.json()

#process results.
print(response_dic.keys())
print('Total repositories: ', response_dic['total_count'])

#Explore information about repositories
repo_dicts = response_dic['items']
print("Repositories returned: ", len(repo_dicts))

#Examine first repositories

repo_dict = repo_dicts[0]
print('Keys: ',len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#Desplegar informacion
names, plot_dicts = [] , []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
     'value':repo_dict['stargazers_count'],
     'label':repo_dict['description'],
     'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)


#Refining Pygal Charts
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000



#Visualizacion de datos
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add(' ',plot_dicts)
chart.render_to_file('python_repos.svg')


###
###
