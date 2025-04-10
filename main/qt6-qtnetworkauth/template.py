pkgname = "qt6-qtnetworkauth"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "module_includes"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-private-devel"]
pkgdesc = "Qt6 Networkauth component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtnetworkauth-everywhere-src-{pkgver}.tar.xz"
sha256 = "fac708b4227d4964d1d127cc6330b103a59a422a1e8334752506c454f7feb418"
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtnetworkauth-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
