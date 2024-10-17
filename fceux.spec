Summary:	NES emulator
Name:		fceux
Version:	2.2.2
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		https://fceultra.sourceforge.net/
Source0:	http://fceultra.sourceforge.net/releases/%{name}-%{version}.src.tar.gz
Patch0:		fceux-2.1.5-gcc46.patch
BuildRequires:	scons
BuildRequires:	lua5.1-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
Requires:	zenity

%description
FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom
Disk System (FDS) emulator. It supports both PAL (European) and NTSC
(USA/JPN) modes. It supports both Windows and SDL versions for cross
compatibility.

%files
%doc Authors changelog.txt NewPPUtests.txt README-SDL TODO*
%doc documentation/
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/mandriva-%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
%scons

%install
install -m 755 -D bin/fceux %{buildroot}%{_bindir}/fceux
install -D documentation/fceux.6 %{buildroot}%{_mandir}/man6/fceux.6

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=FCEUX
GenericName=NES emulator
Comment=Play Nintendo Enternainment System games
Exec=%{_bindir}/%{name}
Icon=emulators_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

