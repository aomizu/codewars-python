# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    if "www" in url:
        return url.split(".")[1]
    elif "http" in url:
        return url.split("//")[1].split(".")[0]
    else:
        return url.split(".")[0]