Name:           polybar
Version:        3.3.1
Release:        1
Summary:        A fast and easy-to-use status bar
License:        MIT
URL:            https://github.com/jaagr/polybar
Source:         https://github.com/jaagr/polybar/archive/%{version}.tar.gz
BuildRequires:  clang >= 3.4
BuildRequires:  cmake >= 3.1
BuildRequires:  cairo-devel
BuildRequires:  xcb-util-devel 
BuildRequires:  libxcb-devel
BuildRequires:  xcb-proto
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
# optional
BuildRequires:  xcb-util-xrm-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  i3-ipc
BuildRequires:  jsoncpp-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libcurl-devel
BuildRequires:  wireless-tools-devel
BuildRequires:  libnl3-devel
BuildRequires:  alsa-lib-devel


%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup -q

%build
%cmake
make

%install
%cmake_install

%files
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/doc/%{name}/config
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg

%changelog
* Fri Apr  4 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 3.3.1-1
- Initial import
