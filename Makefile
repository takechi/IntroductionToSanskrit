
PDFNAME = IntroductionToSanskrit
VGPDFNAME = $(PDFNAME)-vg

TEXS := IntroductionToSanskrit.tex preface.tex general.tex pencraft.tex pronunciation.tex inflection.tex \
declension.tex conjugation.tex declensionContinued.tex comparative.tex pronoun.tex numeral.tex compound.tex \
conjugationContinued.tex passive.tex participle.tex gerund.tex infinitive.tex future.tex perfect.tex \
aorist.tex

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
