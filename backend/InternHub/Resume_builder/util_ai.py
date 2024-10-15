import os
import numpy as np
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Flatten, Dense, LSTM, Embedding, Dropout, Bidirectional, GRU, InputLayer
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

class SkillPrediction():
    def __init__(self, skill_list, role):
        self.skill_list = skill_list
        self.role = role
        self.SEQ_LEN = 17 #Padding length


    def process_skills(self, skill_list):
        # replace any spaces to "_"
        skills = [skill.strip().replace(" ", "_") for skill in skill_list]
        return ' '.join(skills)


    def process_role(self, role):
        # replace any spaces to "-"
        role = role.strip().replace(' ', "-")
        return role


    def prepare_tokens_dataset(self, skills, role):
        # Tokenize the into sequence of numbers
        skill_token_seq = self.skill_tokenizer.texts_to_sequences([skills])
        role_token_seq = self.role_tokenizer.texts_to_sequences([role])

        # Pad the sequence to get the input shape
        skill_token_seq_pad = pad_sequences(skill_token_seq, maxlen=self.SEQ_LEN, padding='pre')
        role_token_seq_pad = pad_sequences(role_token_seq, maxlen=self.SEQ_LEN, padding='pre') 

        dataset = [role_token_seq_pad[0], skill_token_seq_pad[0]]
        self.input_dataset = np.array([dataset])
        return self.input_dataset

    def load_tokenizers(self):
        file_names = ['skill_token.json', 'role_token.json']
        folder_path = os.path.join('.', "ConfigAI", "Tokens")
        skill_path = os.path.join(folder_path, file_names[0])
        role_path = os.path.join(folder_path, file_names[1])

        # Absolute path for token files
        absolute_path_skill = os.path.abspath(skill_path)
        absolute_path_role = os.path.abspath(role_path)
        
        # Reloading the tokenizer form the json file
        with open(absolute_path_skill, 'r') as file:
            self.skill_tokenizer = tokenizer_from_json(file.read())

        with open(absolute_path_role, 'r') as file:
            self.role_tokenizer = tokenizer_from_json(file.read())
        
        return self.skill_tokenizer, self.role_tokenizer


    def load_model(self):
        # file_names = "Skill_Prediction_Model_v2_17.keras"
        file_names = "Skill_Prediction_Model.keras"
        folder_path = os.path.join('.', "ConfigAI", "Model")
        model_path = os.path.join(folder_path, file_names) 
        absolute_path = os.path.abspath(model_path)

        self.model = load_model(absolute_path)
        return self.model


    def make_prediction(self):
        skill_processed = self.process_skills(self.skill_list)
        role_processed = self.process_role(self.role)
        
        skill_tokenizer, role_tokenizer = self.load_tokenizers()
        model = self.load_model()
        skill_pred_set = set()

        for i in range(10):
            input_dataset = self.prepare_tokens_dataset(skill_processed, role_processed)
            prediction = model.predict(input_dataset)
            predicted_token = np.argmax(prediction)
            predicted_skill = skill_tokenizer.sequences_to_texts([[predicted_token]])[0]

            skill_processed += ' '+predicted_skill
            skill_pred_set.add(predicted_skill)

            if len(skill_pred_set) > 4:
                break

        return skill_pred_set

