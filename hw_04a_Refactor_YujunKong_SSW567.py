# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 04.a
Requirement: Get REST APIs of GitHub to peek user repos to output info
----- ----- ----- ----- -----
@author: Yujun Kong
"""

import requests, json, sys

class GitHub_Info_Getter:

    gh_url: str
    gh_stdstring_repos: str
    gh_stdstring_users: str
    gh_stdstring_commits: str
    gh_user_name: str
    repo_info: dict = {}
    repo_info_list: list = []

    def __init__(self, user_name: str) -> None:
        
        self.gh_user_name = user_name
        self.gh_url = "http://api.github.com"
        self.gh_stdstring_repos = "/repos"
        self.gh_stdstring_users = "/users"
        self.gh_stdstring_commits = "/commits"
        self.get_info()

    def get_info(self) -> list:

        count: int = 0
        dic_i: dict
        for dic_i in requests.get(self.gh_url + self.gh_stdstring_users + "/" + self.gh_user_name + self.gh_stdstring_repos).json():
            for key, value in dic_i.items():
                if key == "name":
                    for dic_j in requests.get(self.gh_url + self.gh_stdstring_repos + "/" + self.gh_user_name + "/" + value + self.gh_stdstring_commits).json():
                        count += 1
                    self.repo_info[value] = count

        for k, v in self.repo_info.items():
            self.repo_info_list.append({"Repo": k, "Number of commits": v})

        return self.repo_info_list

    def format_info(self) -> None:

        dic_i: dict
        line: str = ""
        lines: list = []     
        for dic_i in self.repo_info_list:
            line = str(dic_i).strip("{").strip("}").replace("'", "").replace(",", "")
            lines.append(line) 

        return "\n".join(lines)

def main():

    print("Welcome to 'GitHub Repo-Info Peek'...\n")    
    gig = GitHub_Info_Getter("fluencyk")
    print(f"{gig.format_info()}\n")
    print("The above is the repo-info of the GitHub user: " + "'" + gig.gh_user_name + "'" +"\n" + "-" * 100)    
    sys.exit()    

if __name__ == "__main__":
    main()