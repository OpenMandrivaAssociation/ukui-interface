%define project      ukui
%define sover        0
%define log4qt_sover 1

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

%package -n lib%{project}-backgroundclient%{sover}
Summary:       Ukui Backgroundclient Interface Library

%description -n lib%{project}-backgroundclient%{sover}
This package provides Backgroundclient Interface Library for UKUI desktop.

%package -n lib%{project}-com4c%{sover}
Summary:       Ukui Com4c Interface Library

%description -n lib%{project}-com4c%{sover}
This package provides Com4c Interface Library for UKUI desktop.

%package -n lib%{project}-com4cxx%{sover}
Summary:       Ukui Com4cxx Interface Library

%description -n lib%{project}-com4cxx%{sover}
This package provides com4cxx Interface Library for UKUI desktop.

%package -n lib%{project}-desktopclient%{sover}
Summary:       Ukui Desktopclient Interface Library

%description -n lib%{project}-desktopclient%{sover}
This package provides desktopclient Interface Library for UKUI desktop.

%package -n lib%{project}-fontclient%{sover}
Summary:       Ukui Fontclient Interface Library

%description -n lib%{project}-fontclient%{sover}
This package provides fontclient Interface Library for UKUI desktop.

%package -n lib%{project}-gsettings%{sover}
Summary:       Ukui Gsettings Interface Library

%description -n lib%{project}-gsettings%{sover}
This package provides gsettings Interface Library for UKUI desktop.

%package -n lib%{project}-interfaceclient%{sover}
Summary:       Ukui Interfaceclient Interface Library

%description -n lib%{project}-interfaceclient%{sover}
This package provides gsettings Interface Library for UKUI desktop.

%package -n lib%{project}-log4qt%{log4qt_sover}
Summary:       Ukui Log4qt Interface Library

%description -n lib%{project}-log4qt%{log4qt_sover}
This package provides log4qt Interface Library for UKUI desktop.

%package -n lib%{project}-keyboardclient%{sover}
Summary:       Ukui Keyboardclient Interface Library

%description -n lib%{project}-keyboardclient%{sover}
This package provides keyboardclient Interface Library for UKUI desktop.

%package -n lib%{project}-marcogeneralclient%{sover}
Summary:       Ukui Marcogeneralclient Interface Library

%description -n lib%{project}-marcogeneralclient%{sover}
This package provides Marcogeneralclient Interface Library for UKUI desktop.

%package -n lib%{project}-mouseclient%{sover}
Summary:       Ukui Mouseclient Interface Library

%description -n lib%{project}-mouseclient%{sover}
This package provides mouseclient Interface Library for UKUI desktop.

%package -n lib%{project}-network%{sover}
Summary:       Ukui Network Interface Library

%description -n lib%{project}-network%{sover}
This package provides mouseclient Interface Library for UKUI desktop.

%package -n lib%{project}-powerclient%{sover}
Summary:       Ukui Powerclient Interface Library

%description -n lib%{project}-powerclient%{sover}
This package provides powerclient Interface Library for UKUI desktop.

%package -n lib%{project}-print%{sover}
Summary:       Ukui Print Interface Library

%description -n lib%{project}-print%{sover}
This package provides print Interface Library for UKUI desktop.

%package -n lib%{project}-screensaverclient%{sover}
Summary:       Ukui Screensaverclient Interface Library

%description -n lib%{project}-screensaverclient%{sover}
This package provides screensaverclient Interface Library for UKUI desktop.

%package -n lib%{project}-sessionclient%{sover}
Summary:       Ukui Sessionclient Interface Library

%description -n lib%{project}-sessionclient%{sover}
This package provides sessionclient Interface Library for UKUI desktop.

%package -n lib%{project}-touchpadclient%{sover}
Summary:       Ukui Touchpadclient Interface Library

%description -n lib%{project}-touchpadclient%{sover}
This package provides touchpadclient Interface Library for UKUI desktop.

%package -n lib%{project}-usersetting%{sover}
Summary:       Ukui Usersetting Interface Library

%description -n lib%{project}-usersetting%{sover}
This package provides usersetting Interface Library for UKUI desktop.

%package devel
Summary:        Development tools for ukui-interface
Group:          Development/Libraries/X11
Requires:       lib%{project}-backgroundclient%{sover}
Requires:       lib%{project}-com4c%{sover}
Requires:       lib%{project}-com4cxx%{sover}
Requires:       lib%{project}-desktopclient%{sover}
Requires:       lib%{project}-fontclient%{sover}
Requires:       lib%{project}-gsettings%{sover}
Requires:       lib%{project}-interfaceclient%{sover}
Requires:       lib%{project}-log4qt%{log4qt_sover}
Requires:       lib%{project}-keyboardclient%{sover}
Requires:       lib%{project}-marcogeneralclient%{sover}
Requires:       lib%{project}-mouseclient%{sover}
Requires:       lib%{project}-network%{sover}
Requires:       lib%{project}-powerclient%{sover}
Requires:       lib%{project}-print%{sover}
Requires:       lib%{project}-screensaverclient%{sover}
Requires:       lib%{project}-sessionclient%{sover}
Requires:       lib%{project}-touchpadclient%{sover}
Requires:       lib%{project}-usersetting%{sover}

%description devel
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
%make_install
popd

rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a 
%fdupes %{buildroot}

%post -n lib%{project}-backgroundclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-backgroundclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-com4c%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-com4c%{sover} -p /sbin/ldconfig

%post -n lib%{project}-com4cxx%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-com4cxx%{sover} -p /sbin/ldconfig

%post -n lib%{project}-desktopclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-desktopclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-fontclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-fontclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-gsettings%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-gsettings%{sover} -p /sbin/ldconfig

%post -n lib%{project}-interfaceclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-interfaceclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-log4qt%{log4qt_sover} -p /sbin/ldconfig
%postun -n lib%{project}-log4qt%{log4qt_sover} -p /sbin/ldconfig

%post -n lib%{project}-keyboardclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-keyboardclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-marcogeneralclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-marcogeneralclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-mouseclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-mouseclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-network%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-network%{sover} -p /sbin/ldconfig

%post -n lib%{project}-powerclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-powerclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-print%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-print%{sover} -p /sbin/ldconfig

%post -n lib%{project}-screensaverclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-screensaverclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-sessionclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-sessionclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-touchpadclient%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-touchpadclient%{sover} -p /sbin/ldconfig

%post -n lib%{project}-usersetting%{sover} -p /sbin/ldconfig
%postun -n lib%{project}-usersetting%{sover} -p /sbin/ldconfig

%files
%{_bindir}/ukui-*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/org.ukui.log4qt.gschema.xml

%files -n lib%{project}-backgroundclient%{sover}
%{_libdir}/lib%{project}-backgroundclient.so.*

%files -n lib%{project}-com4c%{sover}
%{_libdir}/lib%{project}-com4c.so.*

%files -n lib%{project}-com4cxx%{sover}
%{_libdir}/lib%{project}-com4cxx.so.*

%files -n lib%{project}-desktopclient%{sover}
%{_libdir}/lib%{project}-desktopclient.so.*

%files -n lib%{project}-fontclient%{sover}
%{_libdir}/lib%{project}-fontclient.so.*

%files -n lib%{project}-gsettings%{sover}
%{_libdir}/lib%{project}-gsettings.so.*

%files -n lib%{project}-interfaceclient%{sover}
%{_libdir}/lib%{project}-interfaceclient.so.*

%files -n lib%{project}-log4qt%{log4qt_sover}
%{_libdir}/lib%{project}-log4qt.so.*

%files -n lib%{project}-keyboardclient%{sover}
%{_libdir}/lib%{project}-keyboardclient.so.*

%files -n lib%{project}-marcogeneralclient%{sover}
%{_libdir}/lib%{project}-marcogeneralclient.so.*

%files -n lib%{project}-mouseclient%{sover}
%{_libdir}/lib%{project}-mouseclient.so.*

%files -n lib%{project}-network%{sover}
%{_libdir}/lib%{project}-network.so.*

%files -n lib%{project}-powerclient%{sover}
%{_libdir}/lib%{project}-powerclient.so.*

%files -n lib%{project}-print%{sover}
%{_libdir}/lib%{project}-print.so.*

%files -n lib%{project}-screensaverclient%{sover}
%{_libdir}/lib%{project}-screensaverclient.so.*

%files -n lib%{project}-sessionclient%{sover}
%{_libdir}/lib%{project}-sessionclient.so.*

%files -n lib%{project}-touchpadclient%{sover}
%{_libdir}/lib%{project}-touchpadclient.so.*

%files -n lib%{project}-usersetting%{sover}
%{_libdir}/lib%{project}-usersetting.so.*

%files devel
%{_includedir}/kylin-*.h
%{_includedir}/ukui-log4qt.h
%{_libdir}/lib%{project}-*.so
