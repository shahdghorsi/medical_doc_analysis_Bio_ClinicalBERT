from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import json
import text_extractor

model_name = "emilyalsentzer/Bio_ClinicalBERT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

pdf_file_path = "medical-record.pdf"

''' This is the first set of questions I used for the task, I tried reforming agşn cause these questions did not give good results
questions = [
    "What is the patient's chief complaint?",
    "What is the suggested treatment plan?",
    "What are the patient's allergies?",
    "What medications is the patient taking?",
    "Does the patient have a family history of hypertension?",
    "Does the patient have a family history of colon cancer?",
    "Has the patient experienced minimal bright red blood per rectum?"
]'''
questions = ["What is the reason for the patient's visit or main health concern?",
"What treatment has been recommended or prescribed by the doctor?",
"Are there any known allergies that the patient has?",
"What medications is the patient currently using, and are there any associated side effects?",
"Is there a history of hypertension in the patient's family?",
"Is there a family history of colon cancer?",
"Has the patient reported any instances of minimal bright red blood per rectum?"]

images_path = 'images'
context = text_extractor.extract_text_from_images(images_path)
#print("CONTEXT" + context)
answers = []

for question in questions:
    
    result = nlp(question=question, context=context)
    print("RESULT" , result)
    answer = result['answer']
    confidence = result['score']
    answer_dict = {
        "question": question,
        "answer": answer,
        "confidence": confidence
    }
    print(answer_dict)
    answers.append(answer_dict)

# Determine treatment plan appropriateness
yes_count = sum(answer["answer"].lower() == "yes" for answer in answers[-3:])
no_count = 3 - yes_count
treatment_plan_appropriate = "Yes" if yes_count > no_count else "No"

# Construct the JSON object with the retrieved information
output = {
    "answers": answers,
    "treatment_plan_appropriate": treatment_plan_appropriate
}

# Save the JSON output to a file
output_file = "output.json"
with open(output_file, 'w') as f:
    json.dump(output, f)

print("Output saved to", output_file)
