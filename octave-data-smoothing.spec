%global octpkg data-smoothing

Summary:	Algorithms for smoothing noisy data with Octave
Name:		octave-data-smoothing
Version:	1.3.0
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/data-smoothing/
Source0:	https://downloads.sourceforge.net/octave/data-smoothing-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.6.0
BuildRequires:  octave-optim >= 1.0.3

Requires:	octave(api) = %{octave_api}
Requires:  	octave-optim >= 1.0.3

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Algorithms for smoothing noisy data.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

