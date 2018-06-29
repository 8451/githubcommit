# githubcommit

githubcommit is a jupyter notebook extension enabling users push ipython notebooks to a git repo.
The git button gets displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository. There are few
environment variables that must be exported. Currently this extension supports
commits to a single github repo defined in environment variable but in the long
run need help to modify this extension allowing user to select his repo and branch.

## Installation

You can currently install this directly from git:

```
pip install git+https://github.com/sat28/githubcommit.git
jupyter serverextension enable --py githubcommit
jupyter nbextension install --py githubcommit
```

To enable this extension for all notebooks:

```
jupyter nbextension enable --py githubcommit
```

## Steps

* Install package using above commands
* Create Git repo where notebooks will be pushed if not already exists and clone it in your `GIT_PARENT_DIR`
* Clone this repo as well in your `GIT_PARENT_DIR` directory
* Replace the values in env.sh present in this repo itself
* Run the command - source ~/githubcommit/env.sh
* Configure ssh key (present in ~/.ssh/id_rsa.pub or specified location) in github account
* Run jupyter notebook from within your repo directory

## Example git configuration
export GIT_PARENT_DIR=~ <br />
export GIT_REPO_NAME=gitjupyter <br />
export GIT_BRANCH_NAME=master <br />
export GIT_REMOTE_NAME=origin
export GIT_USER=sat28 <br />
export GIT_EMAIL=anand.shaleen@gmail.com <br />
export GITHUB_ACCESS_TOKEN=#access-token from github developer settings <br />
export GIT_USER_UPSTREAM=sat28 <br />

## Screenshots

![Extension](screens/extension.png?raw=true "Extension added to toolbar")

![Commit Message](screens/commit.png?raw=true "Commit Message")

![Success Message](screens/success.png?raw=true "Success Message")

## Development
### Packaging:
The most important file for packaging is "setup.py" which exists at the root of the project directory. 

“setup.py” serves two primary functions:
- It’s the file where various aspects of the project are configured. The primary feature of setup.py is that it contains a global setup() function. The keyword arguments to this function are how specific details of your project are defined. 
- It’s the command line interface for running various commands that relate to packaging tasks. To get a listing of available commands, run python setup.py --help-commands.

### Versioning Scheme:
We are following the semantic versioning schema for this project as it is recommended in the PyPA user guide.
This is a 3-part numbering scheme:  MAJOR.MINOR.MAINTENANCE
1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. MAINTENANCE version when you make backwards-compatible bug fixes.

Make sure the version is updated in setup.py each time you make a code change.

*Important Note*: Make sure that versioning is consistent with each deployment. For example, if you choose to version it as 0.1.2 make sure it is always versioned in only numbers. If you choose to version it as 0.1.2.a1 make sure it is always versioned in that format.  

## Credits

Thanks to https://github.com/Lab41/sunny-side-up for laying the foundation of this extension.

Thanks to https://github.com/justvarshney for support.

