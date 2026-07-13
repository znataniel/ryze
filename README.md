# Ryze

### Setup

Clone the repo
`git clone --bare <git-repo-url> $HOME/.cfg`

Alias for current session
`alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'`

Pull and remove any old files that need to be overwritten
`config pull origin main`

Disable showUntrackedFiles
`config config --local status.showUntrackedFiles no`

> [Original Atlassian Guide](https://www.atlassian.com/git/tutorials/dotfiles)
