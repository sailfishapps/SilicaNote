# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       SilicaNote

# >> macros
%{!?qtc_qmake5:%define qtc_qmake5 qmake}
%{!?qtc_qmake:%define qtc_qmake qmake}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
# << macros

Summary:    SilicaNote
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
Source0:    %{name}-%{version}.tar.bz2
Source100:  SilicaNote.yaml

%description
A simple note taking app for SailfishOS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
/opt/sdk/share/applications
/opt/sdk/share/SilicaNote
/opt/sdk/bin
/opt
# >> files
# << files
