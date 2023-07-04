from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import PyPDF2

# Import the text_extractor module (not provided in the code snippet)
import text_extractor

model_name = "emilyalsentzer/Bio_ClinicalBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

pdf_file_path = "medical-record.pdf"

chief_complaint_question = "What is the patient's chief complaint?"
treatment_plan_question = "What is the suggested treatment plan?"
allergies_question = "What are the patient's allergies?"
medications_question = "What medications is the patient taking?"

def extract_information(context, question):
    """
    Extracts information from a given context by answering a question using the pre-trained model.
    
    Args:
        context (str): The text context in which to search for the answer.
        question (str): The question to be answered.
    
    Returns:
        answer (str): The extracted answer to the question.
        confidence (float): The confidence score of the extracted answer.
    """
    result = nlp(question=question, context=context)
    return result['answer'], result['score']

def answer_question(question, context):
    """
    Answers a specific question using the pre-trained model.
    
    Args:
        question (str): The question to be answered.
        context (str): The text context in which to search for the answer.
    
    Returns:
        answer (str): The extracted answer to the question.
        confidence (float): The confidence score of the extracted answer.
    """
    result = nlp(question=question, context=context)
    answer = result['answer']
    confidence = result['score']
    return answer, confidence

# Call the text_extractor.extract_text_from_images() function to get the text context from images
image_folder = 'images'
context = text_extractor.extract_text_from_images(image_folder)

# Uncomment the following line if using the extract_text_from_pdf() function to get the text context from a PDF file
# context = extract_text_from_pdf(pdf_file_path)

# Extract information for various questions
chief_complaint, chief_complaint_confidence = extract_information(context, chief_complaint_question)
treatment_plan, treatment_plan_confidence = extract_information(context, treatment_plan_question)
allergies, allergies_confidence = extract_information(context, allergies_question)
medications, medications_confidence = extract_information(context, medications_question)

hypertension_question = "Does the patient have a family history of hypertension?"
colon_cancer_question = "Does the patient have a family history of colon cancer?"
bright_red_blood_question = "Has the patient experienced minimal bright red blood per rectum?"

# Answer additional questions using the answer_question() function
hypertension_answer, hypertension_confidence = answer_question(hypertension_question, context)
colon_cancer_answer, colon_cancer_confidence = answer_question(colon_cancer_question, context)
bright_red_blood_answer, bright_red_blood_confidence = answer_question(bright_red_blood_question, context)

# Print the extracted information and confidence scores
print("Chief Complaint:", chief_complaint)
print("Chief Complaint Confidence:", chief_complaint_confidence)
print("Treatment Plan:", treatment_plan)
print("Treatment Plan Confidence:", treatment_plan_confidence)
print("Allergies:", allergies)
print("Allergies Confidence:", allergies_confidence)
print("Medications:", medications)
print("Medications Confidence:", medications_confidence)
print("Hypertension Answer:", hypertension
