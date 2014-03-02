%define	pkgname data-smoothing

Summary:	Algorithms for smoothing noisy data with Octave
Name:		octave-%{pkgname}
Version:	1.2.0
Release:	3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/data-smoothing/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7
Requires:	octave-optim >= 1.0.3
BuildRequires:	octave-devel >= 2.9.7
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildArch:	noarch

%description
Algorithms for smoothing noisy data with Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
