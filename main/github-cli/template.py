pkgname = "github-cli"
pkgver = "2.56.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/cli/cli/v2/internal/build.Version=v{pkgver}",
    "./cmd/gh",
    "./cmd/gen-docs",
]
make_check_args = ["./..."]
hostmakedepends = ["go"]
checkdepends = ["git", "openssh"]
pkgdesc = "GitHub CLI tool"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://cli.github.com"
source = f"https://github.com/cli/cli/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ed19f01df36e336472c434edfadf01a2cbe4bf07394724b064a80c8fd6a0dc1e"
# cross: uses native binary to generate completions
# check: needs network access
options = ["!cross", "!check"]


def post_build(self):
    self.do("./build/gen-docs", "--man-page", "--doc-path", "man")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"gh.{shell}", "w") as cf:
            self.do("build/gh", "completion", f"-s={shell}", stdout=cf)


def install(self):
    # Don't use go build style install because it would also install gen-docs
    self.install_bin("build/gh")
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)

    self.install_completion("gh.bash", "bash", "gh")
    self.install_completion("gh.fish", "fish", "gh")
    self.install_completion("gh.zsh", "zsh", "gh")