import os, json, pip


class Setup:
    def __init__(self) -> None:
        self.mainDir = os.path.dirname(os.path.realpath(__file__))
        self.settings_file_path = os.path.join(self.mainDir, "settings.json")
        self.settings = dict(json.load(open(self.settings_file_path)))

        self.dependencies = self.settings['dependencies']
        self.git_links = self.settings['git-dependencies']
        self.verbose = self.settings["verbose"]

        self.git_inst_dir = os.path.join(self.mainDir, 'temp')

        self.ChecknInstall(self.dependencies)
        self.ChecknInstall(self.git_links, git=True)

    def ChecknInstall(self, pkgs: dict, git: bool = False):
        status = dict()

        for pkg, pkg_src in pkgs.items():
            try:
                __import__(pkg)
                status[pkg] = True

            except ImportError as e:
                if self.verbose:
                    print(f'\033[31;1m[-] ModuleNotFoundError:\033[0m \033[31mNo module named \'\033[1m{pkg}\033[0m\033[31m\'.\033[0m')
                    print(f'\033[33mInstalling \'\033[1m{pkg}\033[0m\033[33m\'...\033[0m')

                if git:
                    os.system(f"git clone {pkg_src} {self.git_inst_dir}")
                    lsgitdir = os.listdir(self.git_inst_dir)

                    if pkg in lsgitdir:
                        os.system(f"mv -r {os.path.join(self.git_inst_dir, pkg)} {self.mainDir}")

                    os.system(f"rm -rf {os.path.join(self.git_inst_dir, '*')}")

                else:
                    pip.main(['install', pkg_src])

        return status