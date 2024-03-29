#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fUnitRoots
Version  : 4021.80
Release  : 42
URL      : https://cran.r-project.org/src/contrib/fUnitRoots_4021.80.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fUnitRoots_4021.80.tar.gz
Summary  : Rmetrics - Modelling Trends and Unit Roots
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fUnitRoots-lib = %{version}-%{release}
Requires: R-fBasics
Requires: R-timeSeries
Requires: R-urca
BuildRequires : R-fBasics
BuildRequires : R-timeSeries
BuildRequires : R-urca
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-fUnitRoots package.
Group: Libraries

%description lib
lib components for the R-fUnitRoots package.


%prep
%setup -q -c -n fUnitRoots
cd %{_builddir}/fUnitRoots

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659973732

%install
export SOURCE_DATE_EPOCH=1659973732
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fUnitRoots
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fUnitRoots
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fUnitRoots
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fUnitRoots || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fUnitRoots/DESCRIPTION
/usr/lib64/R/library/fUnitRoots/INDEX
/usr/lib64/R/library/fUnitRoots/Meta/Rd.rds
/usr/lib64/R/library/fUnitRoots/Meta/features.rds
/usr/lib64/R/library/fUnitRoots/Meta/hsearch.rds
/usr/lib64/R/library/fUnitRoots/Meta/links.rds
/usr/lib64/R/library/fUnitRoots/Meta/nsInfo.rds
/usr/lib64/R/library/fUnitRoots/Meta/package.rds
/usr/lib64/R/library/fUnitRoots/NAMESPACE
/usr/lib64/R/library/fUnitRoots/NEWS.md
/usr/lib64/R/library/fUnitRoots/R/fUnitRoots
/usr/lib64/R/library/fUnitRoots/R/fUnitRoots.rdb
/usr/lib64/R/library/fUnitRoots/R/fUnitRoots.rdx
/usr/lib64/R/library/fUnitRoots/help/AnIndex
/usr/lib64/R/library/fUnitRoots/help/aliases.rds
/usr/lib64/R/library/fUnitRoots/help/fUnitRoots.rdb
/usr/lib64/R/library/fUnitRoots/help/fUnitRoots.rdx
/usr/lib64/R/library/fUnitRoots/help/paths.rds
/usr/lib64/R/library/fUnitRoots/html/00Index.html
/usr/lib64/R/library/fUnitRoots/html/R.css
/usr/lib64/R/library/fUnitRoots/unitTests/Makefile
/usr/lib64/R/library/fUnitRoots/unitTests/runTests.R
/usr/lib64/R/library/fUnitRoots/unitTests/runit.DickeyFullerPValues.R
/usr/lib64/R/library/fUnitRoots/unitTests/runit.MacKinnonPValues.R
/usr/lib64/R/library/fUnitRoots/unitTests/runit.UnitRootUrcaInterface.R
/usr/lib64/R/library/fUnitRoots/unitTests/runit.UnitrootTests.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fUnitRoots/libs/fUnitRoots.so
/usr/lib64/R/library/fUnitRoots/libs/fUnitRoots.so.avx2
/usr/lib64/R/library/fUnitRoots/libs/fUnitRoots.so.avx512
