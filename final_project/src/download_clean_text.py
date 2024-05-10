import PyPDF2
import re
pdf_file_path="/Users/gracecook/Desktop/final_project/texts/Elizabeth_Bishop.pdf"


#this whole code opens the pdf and cleans it and then saves the clean text as the text file
with open (pdf_file_path,'rb') as file:
	reader=PyPDF2.PdfReader(file)
	text=''
	for page_num in range(len(reader.pages)):
		if page_num==0: #skips first page because there is no poetry on it at all
			continue 
		page=reader.pages[page_num]
		page_text=page.extract_text() #this extracts the text

		page_text=page_text.replace('A Miracle for','') #this is a half title that I don't want in
		page_text=re.sub(r'www\.PoemHunter\.com.*$','',page_text,flags=re.MULTILINE) #removing footer that says where pdf is from
		page_text = re.sub(r'\b[A-Z][a-z]*\b(?: [A-Z][a-z]*)*\n', '', page_text) #remove title cased words (looked up regular expression)
		page_text = re.sub(r'\b\d+\b', '', page_text) #remove numbers

		
		text +=page_text

#cleaning
cleaned_text = re.sub(r'[^\w\s\'-]', '', text)  #remove non-alphabetical stuff except apostrophes
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple whitespace characters with a single space
cleaned_text_with_periods = re.sub(r'(?<=[^\d\s])\n(?=[A-Z])', '. ', cleaned_text) #adds periods if cnew line and uppercase letter (looked up regular expression)
cleaned_text_with_periods = re.sub(r'\b-\b', ' ', cleaned_text_with_periods) #replaces hyphens that connect words...(looked up regular expression)

#saving as txt file now 
clean_text_file_path="/Users/gracecook/Desktop/final_project/texts/elizabeth_bishop_cleaned.txt"
with open(clean_text_file_path,'w') as clean_file:
	clean_file.write(cleaned_text_with_periods)

