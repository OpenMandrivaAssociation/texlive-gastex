# revision 15878
# category Package
# catalog-ctan /graphics/gastex
# catalog-date 2007-03-07 00:33:49 +0100
# catalog-license lppl
# catalog-version 2.8
Name:		texlive-gastex
Version:	2.8
Release:	2
Summary:	Graphs and Automata Simplified in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/gastex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gastex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gastex.doc.tar.xz
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
%{_texmfdistdir}/dvips/gastex/gastex.pro
%{_texmfdistdir}/tex/latex/gastex/gastex.sty
%doc %{_texmfdistdir}/doc/latex/gastex/README
%doc %{_texmfdistdir}/doc/latex/gastex/ex-beamer-gastex.tex
%doc %{_texmfdistdir}/doc/latex/gastex/ex-gastex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.8-2
+ Revision: 752184
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.8-1
+ Revision: 718521
- texlive-gastex
- texlive-gastex
- texlive-gastex
- texlive-gastex

