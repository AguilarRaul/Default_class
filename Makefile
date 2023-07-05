# Default Credit Pipeline, pre processing test

# Example usage: 
# make all 
# make clean 

all : doc/Final_report.pdf

#preprocessing
data/clean/train.csv data/clean/test.csv : data/raw/UCI_Credit_Card.csv src/pre_process.py
	python src/pre_process.py

data/clean/train_f_enf.csv data/clean/test_f_eng.csv : data/clean/train.csv data/clean/test.csv src/feature_eng.py
	python src/feature_eng.py

doc/Final_report.pdf : doc/Final_report.Rmd data/clean/train_f_enf.csv
	Rscript -e "rmarkdown::render('doc/Final_report.Rmd')"

clean :
	rm -f doc/Final_report.pdf 