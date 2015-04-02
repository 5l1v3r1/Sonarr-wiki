# How to Contribute #

We're always looking for people to help make Sonarr even better, there are a number of ways to contribute.

## Documentation ##
Setup guides, FAQ, the more information we have on the wiki the better.

## Development ##

### Tools required ###
- Visual Studio 2013 ([Express Edition](http://www.microsoft.com/visualstudio/eng/products/visual-studio-express-for-web "Express Edition") might work but not tested.)
- [Git](http://git-scm.com/downloads)
- [NodeJS](http://nodejs.org/download/)
- [Gulp](http://gulpjs.com)

### Setup ###

- Make sure all the required software mentioned above are installed.
- Clone the repository into your development machine. [*info*](https://help.github.com/articles/working-with-repositories)
- install the required Node Packages `npm install`
- install gulp `npm install gulp -g`
- start gulp to monitor your dev environment for any changes that need post processing using `gulp watch` command.


### Contributing Code ###
- If you're adding a new, already requested feature, please move it to In Progress on [Trello](https://trello.sonarr.tv "Trello") so work is not duplicated.
- Rebase from Sonarr's develop branch, don't merge
- Make meaningful commits, or squash them
- Feel free to make a pull request before work is complete, this will let us see where its at and make comments/suggest improvements
- Reach out to us on the forums or on IRC if you have any questions
- Add tests (unit/integration)
- Commit with *nix line endings for consistency (We checkout Windows and commit *nix)
- Try to stick to one feature per request to keep things clean and easy to understand
- Use 4 spaces instead of tabs, this is the default for VS 2012 and WebStorm (to my knowledge)

### Pull Requesting ###
- You're probably going to get some comments or questions from us, they will be to ensure consistency and maintainability
- We'll try to respond to pull requests as soon as possible, if its been a day or two, please reach out to us, we may have missed it

If you have any questions about any of this, please let us know.