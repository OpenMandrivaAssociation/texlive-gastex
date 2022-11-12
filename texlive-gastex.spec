Name:		texlive-gastex
Version:	58505
Release:	1
Summary:	Graphs and Automata Simplified in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/gastex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gastex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gastex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
GasTeX is a set of LaTeX macros which enable the user to draw
graphs, automata, nets, diagrams, etc., very easily, in the
LaTeX picture environment. The package offers no documentation
(per se), but offers a couple of example files in the
distribution, and more on its home page. GasTeX generates its
own PostScript code, and therefore doesn't work directly under
PDFLaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/gastex
%{_texmfdistdir}/tex/latex/gastex
%doc %{_texmfdistdir}/doc/latex/gastex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
