%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: oxygen-sounds
Version: 5.27.11
Release: 1
Source0: https://download.kde.org/%{stable}/plasma/%(echo %{version}|cut -d. -f1-3)/oxygen-sounds-%{version}.tar.xz
Summary: Sounds for the Oxygen Plasma theme
URL: https://invent.kde.org/plasma/oxygen-sounds/
License: LGPL-3.0-or-later
Group: Graphical desktop/KDE
BuildArch: noarch
BuildRequires: cmake ninja extra-cmake-modules

%description
Sounds for the Oxygen Plasma theme

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/sounds/Oxygen-*.ogg
