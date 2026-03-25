#api  set
import requests


url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNTQ5YTY2YTExNGQzNzc2ZjNhZjI1Njc0ODllMjNjZCIsIm5iZiI6MTc3MTM3OTIwMS40NzgwMDAyLCJzdWIiOiI2OTk1MWEwMWM4ZGM4YTAyZGYwNjY2NTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Y-xqZRbWVWliUJU-u9zivWhiQZY3t-edsjIpUDkv4-U"
}

response = requests.get(url, headers=headers)

print(response.text)
