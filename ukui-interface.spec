%define project      ukui
%define sover        0
%define log4qt_sover 1

%define libname %mklibname ukui-interface
%define devname %mklibname -d ukui-interface

Name:           ukui-interface
Version:        1.0.1
Release:        1
Summary:        Ukui Interface
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://github.com/ukui/ukui-interface
Source:         https://github.com/ukui/ukui-interface/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-hardcode-path.patch
BuildRequires:  fdupes
BuildRequires:  qmake5
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  iniparser-devel
BuildRequires:  mate-common
BuildRequires:  intltool

%description
UKUI interface provides the interface for system configuration and related
libraries.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
UKUI interface provides the interface for system configuration and related libraries.

%package -n %{devname}
Summary:        Development tools for ukui-interface
Group:          Development/Libraries/X11
Requires:	%{libname} = %{version}-%{release}  

%description -n %{devname}
The ukui-interface-devel package contains the header files for ukui-interface.

%prep
%autosetup -p1
sed -i '/include/s|iniparser/iniparser.h|iniparser.h|' src/common/kylin-com4cxx.cpp src/common/kylin-com4c.c

%build
NOCONFIGURE=0 ./autogen.sh
%configure --enable-more-warnings
%make_build
pushd src/log4qt
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build
popd

%install
%make_install
pushd src/log4qt
mkdir -p %{buildroot}%{_libdir}  
%make_install INSTALL_ROOT=%{buildroot}
popd

rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a 
%fdupes %{buildroot}

%files
%{_bindir}/ukui-*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/org.ukui.log4qt.gschema.xml

%files -n %{libname} 
%{_libdir}/lib%{project}-backgroundclient.so.*
%{_libdir}/lib%{project}-com4c.so.*
%{_libdir}/lib%{project}-com4cxx.so.*
%{_libdir}/lib%{project}-desktopclient.so.*
%{_libdir}/lib%{project}-fontclient.so.*
%{_libdir}/lib%{project}-gsettings.so.*
%{_libdir}/lib%{project}-interfaceclient.so.*
%{_libdir}/lib%{project}-log4qt.so.*
%{_libdir}/lib%{project}-keyboardclient.so.*
%{_libdir}/lib%{project}-marcogeneralclient.so.*
%{_libdir}/lib%{project}-mouseclient.so.*
%{_libdir}/lib%{project}-network.so.*
%{_libdir}/lib%{project}-powerclient.so.*
%{_libdir}/lib%{project}-print.so.*
%{_libdir}/lib%{project}-screensaverclient.so.*
%{_libdir}/lib%{project}-sessionclient.so.*
%{_libdir}/lib%{project}-touchpadclient.so.*
%{_libdir}/lib%{project}-usersetting.so.*

%files -n %{devname}
%{_includedir}/kylin-*.h
%{_includedir}/ukui-log4qt.h
%{_libdir}/lib%{project}-*.so
