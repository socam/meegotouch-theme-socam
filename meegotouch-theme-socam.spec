# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       meegotouch-theme-socam

# >> macros
# << macros

Summary:    SOCAM theme
Version:    0.0.1
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1
URL:        https://github.com/xxx
Source:    %{name}-%{version}.tar.bz2
Provides:   meegotouch-theme-socam
BuildArch:  noarch

%define debug_package %{nil}


%description
SOCAM theme for meegotouch


%prep
%setup -q

%build
echo "build ----------------------"
exit 0

%install
echo "install ----------------------"
echo "BUILDROOT:%{buildroot}"
echo "BUILDDIR:%{_builddir}"

echo "DIR:::::`pwd`"
cp -r * %{buildroot}

#echo "COPY %{_builddir}/%{name}-%{version}/* -> %{buildroot}"
#cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}

exit 0

%clean
echo "clean ----------------------"
exit 0


%files
%defattr(-,root,root,-)
%{_datadir}/themes/base/meegotouch/icons/icon-l-meegotouchtheme-socam.png
%{_datadir}/themes/socam/index.theme
%{_datadir}/themes/socam/meegotouch/icons
%{_datadir}/themes/socam/meegotouch/images
%{_datadir}/themes/socam/meegotouch/libmeegotouchhome
%{_datadir}/themes/socam/meegotouch/libmeegotouchviews
%{_datadir}/themes/socam/meegotouch/meegotouchhome

%{_datadir}/fonts/helvetica/helvetica-75-bold.ttf
%{_datadir}/fonts/helvetica/helvetica-37-condensed-thin-oblique.ttf
%{_datadir}/fonts/helvetica/helvetica-37-condensed-thin.ttf




