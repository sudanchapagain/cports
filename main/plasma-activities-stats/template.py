pkgname = "plasma-activities-stats"
pkgver = "6.4.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kconfig-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Library to access KDE activity manager statistics data"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-activities-stats"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-stats-{pkgver}.tar.xz"
sha256 = "adf5f4bfa758ff41309978ef50bbf5ff0a596eaf9137386d4b870e7bcc2330b7"
hardening = ["vis"]


@subpackage("plasma-activities-stats-devel")
def _(self):
    return self.default_devel()
