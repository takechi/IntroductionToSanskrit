
PDFNAME = IntroductionToSanskrit
VGPDFNAME = $(PDFNAME)-vg

TEXS := IntroductionToSanskrit.tex preface.tex general.tex pencraft.tex pronunciation.tex flection.tex \
declension.tex conjugation.tex declensionContinued.tex comparative.tex pronoun.tex numeral.tex compound.tex \
conjugationContinued.tex passive.tex

VGTEXS = $(TEXS:%.tex=%-vg.tex)


PYTHON = python

.PHONY: all clean

all: $(PDFNAME)

$(PDFNAME):
	PYTHON VG.py $(TEXS)
	latexmk $(VGPDFNAME)

clean:
	latexmk -C $(VGPDFNAME)
	RM $(VGTEXS)
