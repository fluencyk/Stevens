# -*- coding: utf-8 -*-
"""
School: Stevens Institute of Technology
Course: SSW 567 - A
Instructor: Prof. Andre Bondi
----- ----- ----- ----- -----
Topic: Homework # 05.a
Requirement: Understanding mock testing techniques
----- ----- ----- ----- -----
@author: Yujun Kong
"""
import sys
import random

class GitHubInfoGetter:
    """Pass"""

    def __init__(self, user_name: str) -> None:
        """ constructor """
        self.numbers: str = "0123456789"
        self.low_alpha: str = "abcdefghijklmnopqrstuvwxyz"
        self.upp_alpha: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.gh_mock_curr_user_name: str = user_name
        self.gh_mock_exst_user_name: str = "fluencyk"

        self.gh_mock_repos_stats: list = []
        self.repo_list: list = []

        if self.validate_user() is False:
            #print(f"No such user '{user_name}' in GitHub! Program ends.") <- manual testing
            self.gh_mock_repos_stats = None
        else:
            self.set_info()
            self.get_info()
            #print(self.gh_mock_repos_stats) <- manual testing

    def validate_user(self) -> bool:
        """ validate if user existed """
        if self.gh_mock_curr_user_name is not self.gh_mock_exst_user_name:
            return False
        return True

    def set_info(self) -> None:
        """ fake user repos info """
        numlow: str = self.numbers + self.low_alpha
        numpha: str = self.numbers + self.low_alpha + self.upp_alpha
        repo_names: list = []

        i: int = 0
        for i in range(0, random.randint(3, 5)):
            temp_name: str = "/" + "".join([self.numbers[random.randint(0, 9)] for j in range(0, 3)]) + "_" + "".join([self.numbers[random.randint(0, 9)] for k in range(0, 6)]) + "/"
            repo_names.append(temp_name)
            i += 1

        for name in repo_names:
            temp_dict: dict = {}
            curr_dict: dict = {}
            info_list: list = []
            commit: int = 0
            for commit in range(0, random.randint(1, random.randint(2, 7))):
                curr_dict["sha"] = "".join([numlow[random.randint(0, 35)] for each_code in range(0, 40)])
                curr_dict["node_id"] = "C_kwD" + "".join([numpha[random.randint(0, 61)] for sing_code in range(0, 65)])
                curr_dict["commit"] = {"data_key": "data_value"}
                info_list.append(curr_dict)
                commit += 1
            temp_dict["Name"] = name
            temp_dict["Info"] = info_list
            self.repo_list.append(temp_dict)

    def get_info(self) -> list:
        """ get statistics of user repos """
        repo: dict

        for repo in self.repo_list:
            temp_dict: dict = {}
            for pair_k, pair_v in repo.items():
                if pair_k == "Name":
                    temp_dict["Repo"] = pair_v
                if pair_k == "Info":
                    count: int = 0
                    for comm_item in pair_v:
                        count += 1
                    temp_dict["Number of commits"] = str(count)
            self.gh_mock_repos_stats.append(temp_dict)

    def format_info(self) -> str:
        """ format statistics of user repos """
        dic_i: dict
        line: str = ""
        lines: list = []
        for dic_i in self.gh_mock_repos_stats:
            line = str(dic_i).strip("{").strip("}").replace("'", "").replace(",", "")
            lines.append(line)

        return "\n".join(lines)

def main():
    """ entrance of program """
    print("Welcome to 'GitHub Repo-Info Peek'...\n")
    gig = GitHubInfoGetter("fluencyk")
    print(f"{gig.format_info()}\n")
    sys.exit()

if __name__ == "__main__":
    main()
