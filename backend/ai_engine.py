import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "isolation_forest.pkl")
TRAINING_LIMIT = 1000  

class AnomalyDetector:
    def __init__(self):
        # Set to 0.001 (0.1%) to completely eliminate normal traffic false positives
        self.model = IsolationForest(contamination=0.02, random_state=42)
        self.training_data = []
        self.is_trained = os.path.exists(MODEL_PATH)
        self.training_complete_message_shown = False
        
        if self.is_trained:
            self.model = joblib.load(MODEL_PATH)
            print(">>> [AI ENGINE] Loaded existing behavioral profile.")
        else:
            print(">>> [AI ENGINE] Learning Mode: Gathering baseline traffic...")
            
    def evaluate(self, packet_size, frequency):
        features = [packet_size, frequency]
        
        if not self.is_trained:
            self.training_data.append(features)
            if len(self.training_data) >= TRAINING_LIMIT:
                self.train_model()
            return 1 
            
        try:
            prediction = self.model.predict([features])
            return prediction[0] 
        except Exception as e:
            return 1

    def train_model(self):
        print(f">>> [AI ENGINE] Training on {len(self.training_data)} normal packets...")
        X = np.array(self.training_data)
        self.model.fit(X)
        joblib.dump(self.model, MODEL_PATH)
        self.is_trained = True
        
        if not self.training_complete_message_shown:
            print(">>> [AI ENGINE] Training Complete! AI is now actively protecting the network.")
            self.training_complete_message_shown = True

detector = AnomalyDetector()