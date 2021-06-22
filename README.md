# spam-classifier
My team's capstone project to classify emails as spam or ham using various machine learning based classifiers.

text_to_csv.py was used to convert the hundreds of text files (pre-classified as spam or ham) into one csv file using the glob library. The spam emails would have a 1 add at the end and the ham, 0. The script outputs a TSV file as most emails contain all of the other commonly used delimiters and those could not be used. Hence the script had to be run once on the spam email folder and once on the ham email folder from the Enron dataset. The resulting two tsv files were combined into one file using Microsoft Excel and separated into two columns.
The resulting CSV file was passed through three classifiers, namely CNN.ipynb, MLP.ipynb and NBspam.ipynb. Accuracy reports were also generated at the end of these runs after ten-fold cross validation and the MLP/MNN classifier resulted with the highest accuracy of ~96%.
