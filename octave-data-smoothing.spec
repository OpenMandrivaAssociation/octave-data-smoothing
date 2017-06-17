%define octpkg data-smoothing

Summary:	Algorithms for smoothing noisy data with Octave
Name:		octave-%{octpkg}
Version:	1.3.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-optim >= 1.0.3

Requires(post): octave
Requires(postun): octave

%description
Algorithms for smoothing noisy data

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

