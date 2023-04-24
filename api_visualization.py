import requests
from plotly.graph_objs import Bar, Layout
from plotly import offline


# defining api url and its version
url = "https://api.github.com/search/repositories?q=language:python&sort:stars"
headers = {"Accept" : "application/vnd.github.v3+json"}

# creating response object using .get method
r = requests.get(url, headers=headers)

# printing status code to check out status of API call --> 200 for successful
print("status code:  ", r.status_code) 

# because r is response object and it is in json format so using .json() method to convert it into python dictionary
response_dicts= r.json()

# printing keys of our response dictionary
print(response_dicts.keys())   # -->  dict_keys(['total_count', 'incomplete_results', 'items'])
print("Total repositories:  ", response_dicts["total_count"])   # --> 10184271

# parsing required data from responce distionary
repo_dicts = response_dicts["items"]
print("Repositories retured:  ",len(repo_dicts))   # --> 30

# eyeballing first object in repo_dicts
for repo_dict in repo_dicts[:1]:
    print("Keys in first repository:  ", len(repo_dict))
    print("Keys are:", "\n", sorted(repo_dict.keys()))
    
# eyeballing required information of each repository
for index, repo_dict in enumerate(repo_dicts):
    print(f"{index+1}st Repository:")
    print(f'\t\tName:  {repo_dict["name"]}')
    print(f'\t\tOwner:  {repo_dict["owner"]["login"]}')
    print(f'\t\tStars:  {repo_dict["stargazers_count"]}') # --.dtype= INT,  print(f'DataType: {type(repo_dict["stargazers_count"])}')
    print(f'\t\tRepository:  {repo_dict["html_url"]}')
    print(f'\t\tDescription:  {repo_dict["description"]}\n\n')
    

# visulazing it using plotly
links, labels, names, stars = [],[],[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["html_url"]
    name = repo_dict["name"]
    links.append(f'<a href= "{owner}">{name}</a>')
    labels.append(f'{repo_dict["owner"]["login"]}</br>{repo_dict["description"]}')

print(names,"\n",stars, len(names), len(stars))

data = [{
    "type": 'bar',
    "x": links,
    "y": stars,
    "hovertext": labels,
    "marker": {"color":"rgb(60,75,180)",
               "line": {"width": 1.5,
                        "color": "rgb(20,20,20)"}},
    "opacity": 0.6
}]


mylayout = {
    "title": "Most Stared Python Project on GitHub",
    "xaxis": {"title" : "Repository"},
    "yaxis": {"title" : "Stars"},
}

offline.plot({"data": data, "layout": mylayout}, filename="github_api.html")

    

