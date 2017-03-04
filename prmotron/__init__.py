import os
import npyscreen
import forms

from github import Github
from git import Repo


def main():
    cwd = os.getcwd()
    repo = Repo(cwd)
    branch_name = repo.active_branch.name
    remotes = repo.remote().urls

    Application(branch_name=branch_name, remotes=remotes).run()

class Application(npyscreen.NPSAppManaged):
    def __init__(self, *args, **kwargs):
        self.branch_name = kwargs.pop('branch_name')
        self.remotes = kwargs.pop('remotes')

        super(Application, self).__init__(*args, **kwargs)

    @property
    def repo_name(self):
        for remote in self.remotes:
            match = re.search("\/\/github\.com\/(?P<full_name>.*)\.git", remote)
            if "full_name" in match.groupdict():
                return match.group("full_name")

    @property
    def repository(self):
        return self.github.get_repo(self.repo_name)

    @property
    def pullrequest(self):
        return self.repository

    @property
    def config(self):
        return config.Config().load_config()

    @property
    def github(self):
        return Github(self.config['username'], self.config['token'])

    def onStart(self):
        self.addFormClass("CONFIG", forms.ConfigForm)
        self.addFormClass("MAIN", forms.PRForm)

        if len(self.config.keys()) == 0:
            self.setNextForm('CONFIG')
