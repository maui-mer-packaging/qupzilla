# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       qupzilla

# >> macros
# << macros

Summary:    A very fast open source browser based on WebKit core
Version:    1.4.4
Release:    1
Group:      Applications/System
License:    GPL-3.0+
URL:        http://qupzilla.com/
Source0:    %{name}-%{version}.tar.xz
Source100:  qupzilla.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils

%description
QupZilla is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
%fdupes %{buildroot}%{_datadir}
rm -vf %{buildroot}%{_libdir}/libQupZilla.so
rm -vf %{buildroot}%{_libdir}/qupzilla/libTestPlugin.so
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYRIGHT FAQ GPLv3
%{_bindir}/%{name}
%{_libdir}/libQupZilla.so.*
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor
%{_datadir}/%{name}/
%{_datadir}/bash-completion/completions/%{name}
# >> files
# << files
