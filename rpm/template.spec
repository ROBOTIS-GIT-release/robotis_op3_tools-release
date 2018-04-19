Name:           ros-kinetic-robotis-op3-tools
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS robotis_op3_tools package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/robotis_op3_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-op3-action-editor
Requires:       ros-kinetic-op3-camera-setting-tool
Requires:       ros-kinetic-op3-gui-demo
Requires:       ros-kinetic-op3-navigation
Requires:       ros-kinetic-op3-offset-tuner-client
Requires:       ros-kinetic-op3-offset-tuner-server
Requires:       ros-kinetic-op3-web-setting-tool
BuildRequires:  ros-kinetic-catkin

%description
ROS packages for the robotis_op3_tools (meta package)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 19 2018 Pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

