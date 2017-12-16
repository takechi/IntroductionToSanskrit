
PDFNAME = IntroductionToSanskrit
VGPDFNAME = IntroductionToSanskrit-vg

TEXS := IntroductionToSanskrit.tex preface.tex general.tex pencraft.tex pronunciation.tex flection.tex
VGTEXS := IntroductionToSanskrit-vg.tex preface-vg.tex general-vg.tex pencraft-vg.tex pronunciation-vg.tex flection-vg.tex

PYTHON = python

.PHONY: all clean

all: $(PDFNAME)

$(PDFNAME):
	PYTHON VG.py $(TEXS)
	latexmk $(VGPDFNAME)

clean:
	latexmk -C $(VGPDFNAME)
	RM $(VGTEXS)

