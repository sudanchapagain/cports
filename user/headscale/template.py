pkgname = "headscale"
pkgver = "0.25.1"
pkgrel = 4
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/juanfont/headscale/cmd/headscale/cli.Version=v{pkgver}",
    "./cmd/headscale",
]
hostmakedepends = ["go"]
pkgdesc = "Open source implementation of the tailscale control server"
license = "BSD-3-Clause"
url = "https://github.com/juanfont/headscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "076e59275119c1a5c6436fb2a7628c71e605ccb569fd0fb8be6a6461e035660a"
# generates completions with host binary
options = ["!cross"]

if self.profile().arch == "ppc64le":
    broken = "segfaults in tests"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"headscale.{shell}", "w") as f:
            self.do(f"{self.make_dir}/headscale", "completion", shell, stdout=f)


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "headscale")
    self.install_file("config-example.yaml", "usr/share/headscale")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"headscale.{shell}", shell)
