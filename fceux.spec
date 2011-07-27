%define name	fceux
%define version 2.1.5
%define release %mkrel 1

Summary:	NES emulator
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Emulators
License:	GPLv2+
URL:		http://fceultra.sourceforge.net/
Source0:	http://fceultra.sourceforge.net/releases/%name-%version.src.tar.bz2
Patch0:		fceux-2.1.5-gcc46.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	scons
BuildRequires:  lua5.1-devel
BuildRequires:  gtk2-devel
BuildRequires:  GL-devel
BuildRequires:  SDL-devel
Requires: zenity
Obsoletes: fceu

%description
FCEUX is a Nintendo Entertainment System (NES), Famicom, and Famicom
Disk System (FDS) emulator. It supports both PAL (European) and NTSC
(USA/JPN) modes. It supports both Windows and SDL versions for cross
compatibility.

%prep
%setup -q -c
%patch0 -p0

%build
cd fceu%{version}
%scons

%install
rm -rf %{buildroot}
install -m 755 -D fceu%{version}/bin/fceux %{buildroot}%{_bindir}/fceux
install -D fceu%{version}/documentation/fceux.6 %{buildroot}%{_mandir}/man6/fceux.6

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
Categories=GTK;Game;Emulator;
EOF


%files
%defattr(-,root,root)
%doc fceu%{version}/Authors.txt fceu%{version}/changelog.txt fceu%{version}/NewPPUtests.txt
%doc fceu%{version}/README-SDL fceu%{version}/TODO*
%doc fceu%{version}/documentation/
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/mandriva-%{name}.desktop

%clean
rm -rf %{buildroot}

