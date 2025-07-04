%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		oxygen-sounds
Version:	6.4.2
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/oxygen-sounds/-/archive/%{gitbranch}/oxygen-sounds-%{gitbranchd}.tar.bz2#/oxygen-sounds-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/plasma/%(echo %{version}|cut -d. -f1-3)/oxygen-sounds-%{version}.tar.xz
%endif
Summary:	Sounds for the Oxygen Plasma theme
URL:		https://invent.kde.org/plasma/oxygen-sounds/
License:	LGPL-3.0-or-later
Group:		Graphical desktop/KDE
BuildArch:	noarch
BuildRequires:	cmake ninja extra-cmake-modules
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DBUILD_WITH_QT6:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-01 after 6.0
%rename plasma6-oxygen-sounds

%description
Sounds for the Oxygen Plasma theme

%files
%{_datadir}/sounds/Oxygen-*.ogg
%{_datadir}/sounds/oxygen
