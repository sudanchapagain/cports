pkgname = "tailscale"
pkgver = "1.84.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    + f" -X tailscale.com/version.longStamp={pkgver}"
    + f" -X tailscale.com/version.shortStamp={pkgver}",
    "./cmd/tailscale",
    "./cmd/tailscaled",
]
hostmakedepends = ["go"]
depends = ["iptables", "ca-certificates"]
pkgdesc = "Mesh VPN daemon based on WireGuard"
license = "BSD-3-Clause"
url = "https://github.com/tailscale/tailscale"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "32673e5552e1176f1028a6a90a4c892d2475c92d1e952ca16156dc523d14d914"
# check: needs network access
# cross: completions with host bin
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"tailscale.{shell}", "w") as outf:
            self.do(
                f"{self.make_dir}/tailscale",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/tailscaled")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_file("^/envfile", "usr/share/tailscale")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"tailscale.{shell}", shell)
