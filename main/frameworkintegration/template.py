pkgname = "frameworkintegration"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    # TODO: packagekitqt6 + AppStreamQt 1.0? (KPackage install handler binaries)
]
pkgdesc = "Integration of Qt application with KDE workspaces"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/frameworkintegration/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/frameworkintegration-{pkgver}.tar.xz"
sha256 = "6e64870e5d3dcee2a7f7d0a509b5236667fa11f78dd38cd8923911f1ca7ba786"
hardening = ["vis"]


@subpackage("frameworkintegration-devel")
def _(self):
    self.depends += [
        "kcolorscheme-devel",
        "kiconthemes-devel",
        "kwidgetsaddons-devel",
    ]
    return self.default_devel()
