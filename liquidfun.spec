%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define oname Box2D

Summary:	A 2D physics engine for games based on Box2D
Name:		liquidfun
Version:	1.1.0
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://google.github.io/liquidfun/
Source0:	https://github.com/google/liquidfun/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		liquidfun-1.1.0-cmake.patch
BuildRequires:	cmake

%description
LiquidFun is a 2D rigid body simulation library for games. Programmers can
use it in their games to make objects move in believable ways and make the
game world more interactive. From the game's point of view a physics engine
is just a system for procedural animation.

LiquidFun is written in portable C++ and based on Box2D. Most of the types
defined in the engine begin with the b2 prefix. Hopefully this is sufficient
to avoid name clashing with your game engine.

#----------------------------------------------------------------------------

%package devel
Summary:	A 2D physics engine for games based on Box2D
Group:		Development/C++
Conflicts:	box2d-devel

%description devel
LiquidFun is a 2D rigid body simulation library for games. Programmers can
use it in their games to make objects move in believable ways and make the
game world more interactive. From the game's point of view a physics engine
is just a system for procedural animation.

LiquidFun is written in portable C++ and based on Box2D. Most of the types
defined in the engine begin with the b2 prefix. Hopefully this is sufficient
to avoid name clashing with your game engine.

%files devel
%doc License.txt Documentation
%{_libdir}/lib*.a
%{_libdir}/%{oname}
%{_libdir}/cmake/%{oname}
%{_includedir}/%{oname}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}/%{oname}
%patch0 -p2
find . -perm 0640 | xargs chmod 0644
find . -perm 0750 | xargs chmod 0755

%build
%cmake \
	-DBOX2D_INSTALL:BOOL=ON \
	-DBOX2D_BUILD_EXAMPLES:BOOL=OFF \
	-DBOX2D_BUILD_UNITTESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

