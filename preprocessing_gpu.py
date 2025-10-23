# Data Pre-Processing with Domain Feature Engineering (GPU-Accelerated for Kaggle)

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer
import nltk
import torch

# --- Step 0.0: Check GPU Availability ---
print("="*60)
print("🖥️  GPU AVAILABILITY CHECK")
print("="*60)
if torch.cuda.is_available():
    device = 'cuda'
    print(f"✅ GPU is available: {torch.cuda.get_device_name(0)}")
    print(f"   GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    print(f"   CUDA Version: {torch.version.cuda}")
else:
    device = 'cpu'
    print("⚠️  No GPU found - using CPU")
print(f"🎯 Using device: {device.upper()}")
print("="*60)

# --- Step 0.1: Download NLTK data directly ---
print("\nDownloading NLTK stopwords and punkt tokenizer...")
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)
print("✅ Downloads complete.")

try:
    # --- Step 1: Load and Rename Columns ---
    print("\n[1/9] Loading dataset...")
    df = pd.read_csv('/kaggle/working/career_recommender_augmented_eda.csv')
    print("✅ Dataset loaded successfully!")

    new_names = {
        'Did you do any certification courses additionally?': 'has_certifications',
        'Have you done masters after undergraduation? If yes, mention your field of masters.(Eg; Masters in Mathematics)': 'masters_field',
        'What is your UG specialization? Major Subject (Eg; Mathematics)': 'ug_major',
        'What was the average CGPA or Percentage obtained in under graduation?': 'cgpa',
        'Are you working?': 'is_working',
        'If yes, then what is/was your first Job title in your current field of work? If not applicable, write NA.': 'job_title',
        'What was your course in UG?': 'ug_course',
        'What is your gender?': 'gender',
        'What are your interests?': 'interests',
        'What is your name?': 'name',
        'If yes, please specify your certificate course title.': 'certification_title',
        'What are your skills ? (Select multiple if necessary)': 'skills'
    }
    df.rename(columns=new_names, inplace=True)
    df.drop(columns=['name'], inplace=True)
    print("✅ Step 1: Columns renamed.")

    # --- Step 2: Define Job Role Mapping ---
    print("\n[2/9] Defining job role mapping...")
    job_role_map = {
        'Software Engineer': ['software engineer','computer software engineer', 'programmer analyst', 'application development analyst', 'ase', 'aws developer', 'rpa developer', 'game programmer', 'software development engineer', 'specialist programmer', 'entry level software engineer', 'assistant system engineer (tcs)', 'junior programmer', 'assistant system engineer', 'associate system engineer', 'software programmer', 'software engineer 1', 'program engineering (it)', 'senior software engineer', 'software engineer trainee', 'automation in java lang', 'mechine learning engineer', 'associate engineer - controls & software', 'product engineer (ai/ml)', 'software developer executive', 'aws architect', 'programmer', 'ml engineer', 'executive engineer', 'software', 'apac engineer', 'se'],
        'Software Development': ['software developer', 'web developer', 'application developer', 'java developer', 'full stack developer', 'developer', '.net developer', 'ios developer', 'python developer','front end java developer', 'back-end developer', 'java full stack developer','junior developer', 'trainee developer', 'asp.net developer', 'back end developer', 'dot net developer', 'front end developer', 'mobile application developer', 'junior software engineer', 'saleforce developer', 'sales force'],
        'Data Science & Analytics': ['data analyst', 'data scientist', 'business analyst', 'data engineer', 'analyst', 'senior business analyst', 'business intelligence developer', 'data science', 'qualitative analyst', 'process executive-data', 'data entry', 'data entry operator', 'sr. political analyst', 'associate data scientist', 'researcher', 'senior editor', 'sr. executive in data management.', 'process analyst', 'risk analyst', 'research fellow', 'senior pmo - data analyst', 'senior analyst', 'statistical programmer', 'sql developer', 'test analyst', 'research associate', 'video labeling(artificial intelligence) and medical coding', 'process exceutive'],
        'IT, Networking & DevOps': ['it support engineer', 'system engineer', 'network engineer', 'devops engineer', 'technical support engineer', 'it analyst', 'associate engineer - devops', 'database administrator', 'system administrator', 'it support', 'systems engineer', 'cyber security engineer', 'information secuirty analyst', 'tech support', 'it engineer', 'associate it consultant', 'junior system engineer trainee', 'network analyst', 'linux administrator', 'desktop support engineer', 'lotus notes admin', 'it operations', 'associate technology l2', 'bms executive', 'buliding management system', 'cloud engineer', 'cyber security analyst', 'erp implementation', 'salesforce admin', 'associate it consultant - erp'],
        'Core, Industrial & Hardware Engineering': ['electrical engineer', 'mechanical engineer', 'civil engineer', 'production engineer', 'service engineer', 'plant instrumentation engineer', 'automation engineer', 'engineer', 'plm engineer', 'site engineer', 'process operations engineer', 'sub engineer', 'compliance engineer', 'mechanical product developer', 'maintenance engineer', 'procurement engineer', 'chemical process engineer', 'gis engineer', 'assistant engineer', 'qc engineer', 'hardware design engineer', 'gat- engine testing engineer', 'r&d engineer', 'structural engineer', 'field engineer', 'mine engineer', 'assistent engineer', 'embedded system engineer', 'operation & maintenance engineer', 'civil & structural engineer', 'mechanical design engineer', 'embedded developer', 'quality control engineer', 'civil design engineer', 'hardware pcb design engineer', 'design engineer', 'instrumentation and control engineer', 'ces-cae- fea analyst', 'hardware engineer', 'vlsi developer', 'electrician', 'engineer-power electronics', 'jr. engineer', 'maintenance engineer-electrical', 'maintenance engineer-mechanical', 'mechanical supervisor', 'motor controller', 'site civil engineer', 'vlsi digital design', 'electronics engineer- research analyst', 'loco pilot', 'machine operator', 'production supervisor', 'mapping', 'power'],
        'Quality Assurance & Testing': ['test engineer', 'qa analyst', 'automation test engineer', 'software tester', 'quality assurances engineer', 'quality analyst', 'qa specialist', 'testing engineer', 'trainee consultant - quality', 'software testing', 'graduate quality engineer', 'quality engineer', 'jumio document verification team', 'quality assurance'],
        'Management, Consulting & Advisory': ['project manager', 'assistant manager', 'associate consultant', 'consultant', 'management trainee', 'project engineer', 'product specialist', 'relationships manager', 'tax consultant', 'senior associate', 'operations engineer', 'get', 'associate', 'business trainee', 'manager', 'operation manager', 'supervisor', 'asst. manager', 'business consultant', 'deputy warden', 'assistent manger', 'plm consultant', 'key account manager', 'planning manager', 'production manager', 'entrepreneur', 'national head', 'finance manager', 'product manager', 'regional sales manager', 'request proposal manager', 'associate scm', 'functional consultant', 'store manager', 'project coordinator', 'managing director', 'business developer', 'associate engineer', 'associate software engineer', 'associate system engineer trainee', 'associate trainee', 'operations management', 'retail manager', 'sap consultant', 'senior assistant delivery coordinator', 'team leader', 'ups supervisor', 'relationship manager at icici'],
        'HR, Administration & Recruiting': ['human resources', 'recruiter', 'hr assistant ii', 'traning and development', 'human resources assistant', 'talent acquisition executive', 'placement trainee', 'hr executive', 'senior technical recruiter, recruitment specialist, talent acquisition specialist (it)', 'admin', 'technical recruiter', 'operation specialist', 'operations specialist', 'hr'],
        'Finance, Accounting & Legal': ['financial analyst', 'accountant', 'finance executive', 'corporate and disputes lawyer', 'tax consultant', 'school accountant', 'litigation lawyer', 'chartered accountant', 'lawyer -ipr', 'lawyer-forensic investigations', 'advocate', 'computerized accounting', 'legal associate', 'investment banking associate', 'investment banking analyst', 'accountent', 'account assistant', 'asst finance manager', 'ca', 'life insurance', 'company secretary', 'law intern', 'active trading service', 'finance consultant', 'personal advisory', 'litigation'],
        'Academia, Research & Medical': ['dean r n d', 'dance teacher', 'data science and game design trainer', 'teaching assistant-biotechnology', 'senior chemist', 'i was working as dean r n d', 'biocurator', 'psychologist', 'researcher', 'maths content developer', 'teaching job', 'teaching experience 5 years', 'scientist', 'chemist in pharmaceutical', 'worked in research institute', 'research fellow', 'clinical research associate', 'dental surgeon', 'medical practitioner', 'teacher', 'assistant professor', 'lecturer', 'lab technician -food safety & quality', 'lab assistent', 'medical posting', 'python instructor', 'young horticulture expert', 'teaching'],
        'Trainee & Entry-Level Roles': ['assistant system engineer trainee', 'data scientist-intern', 'intern', 'intern at innodatatics', 'project intern', 'trainee', 'traniee', 'graduate trainee', 'graduatee engineer', 'logical trainee associate', 'trainee and associates', 'programmer analyst trainee (pat)', 'apprentice dp world navi mumbai'],
        'General & Customer Support': ['telecaller', 'flipkart customer care executive', 'customer care', 'telemarketer', 'customer operation associate', 'service advisor', 'associative staff', 'back office executive', 'receptionist in coaching center', 'customer service', 'fitness consultant expert', 'tele-caller', 'telecaller,sale exicutive'],
        'Business Operations, Sales & Marketing': ['business development associate', 'sales executive', 'operations analyst', 'mis', 'real e-state agent', 'field sales officer', 'i m a marketing head', 'ast.purchase manager', 'buisness devlopment excutive', 'sales excellent', 'marketing guy (tma)', 'business operations', 'purchase executive', 'sr. territory sales manager', 'sales manager', 'sales service engineer-electrical', 'medical representative', 'sale executive', 'tele caller', 'associate operations processor-1', 'catalog associate', 'material planner', 'techno commercial', 'store keeper', 'supply chain', 'production specialist', 'medical and sales reprasentative', 'store assistant'],
        'UX/UI & Creative Design': ['graphic designer', 'social media manager', 'vfx production assistant', 'junior architect', 'graphics designer', 'clothes designer', 'ux designer', 'vfx artist', 'junior interior designer', 'vfx designer', 'modeler', 'dancing'],
        'Digital Marketing': ['digital marketing manager', 'social media executive', 'marketing executive', 'business development manager', 'digital marketing reqruiter', 'web developer and digital marketer', 'marketing manager', 'digital/social media marketer'],
        'Creative, Content & Design': ['content writer', 'sub editor', 'sub-editor', 'content creator', 'technical writer', 'copywriter', 'journalist', 'content writer and creative strategist', 'crime reporter', 'junior sub editor', 'publishing executive']
    }
    role_to_category = {role: category for category, roles in job_role_map.items() for role in roles}
    def map_job_role(title):
        if not isinstance(title, str): return 'Other'
        return role_to_category.get(title.lower().strip(), 'Other')
    print("✅ Step 2: Job role mapping defined.")

    # --- Step 3: Initial Data Separation (Train/Test) ---
    print("\n[3/9] Separating data into train/test sets...")
    df['job_title'].fillna('NA', inplace=True)
    df['job_category'] = df['job_title'].apply(map_job_role)

    # Separate the 'unemployed/student' data as the final, unseen test set
    invalid_titles_lower = ['na', 'student (unemployed)', 'nothing', 'no']
    test_mask = df['job_title'].str.lower().isin(invalid_titles_lower)
    unseen_test_df = df[test_mask].copy()
    model_data_df = df[~test_mask].copy()

    # The target variable for the model data
    y = model_data_df['job_category']
    X = model_data_df.drop('job_category', axis=1)

    X = X.drop(columns=['job_title'])
    unseen_test_df = unseen_test_df.drop(columns=['job_title'])
    print(f"✅ Step 3: Data separated. {len(X)} for modeling, {len(unseen_test_df)} for final testing.")

    # --- Step 4: Create Train and Validation Splits ---
    print("\n[4/9] Creating train/validation splits...")
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    # The final test set does not have a job category, so we drop it
    X_test = unseen_test_df.drop('job_category', axis=1)
    print(f"✅ Step 4: Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")

    # --- Step 5: Domain Feature Engineering ---
    print("\n[5/9] Creating domain features...")
    def create_domain_features(df_in):
        df = df_in.copy()
        df['ug_major'] = df['ug_major'].astype(str).str.lower()
        tech_domain = ['computer', 'information technology', 'it', 'software', 'data science', 'coding', 'programming', 'artificial intelligence', 'csit']
        core_eng_domain = ['mechanical', 'electrical', 'electronics', 'civil', 'automobile', 'instrumentation', 'production', 'chemical', 'telecommunication', 'industrial', 'aerospace', 'aeronautical', 'construction']
        business_domain = ['commerce', 'business', 'bba', 'mba', 'accounts', 'accountancy', 'finance', 'marketing', 'management', 'taxation']
        science_domain = ['physics', 'chemistry', 'biotechnology', 'mathematics', 'math', 'statistics', 'biology', 'zoology', 'pharmacy', 'microbiology', 'geology']
        arts_humanities_domain = ['history', 'english', 'law', 'economics', 'political', 'psychology', 'sociology', 'journalism', 'literature', 'arts', 'communication', 'geography', 'design', 'animation', 'media', 'fashion']

        df['ug_domain'] = 'Other'
        df.loc[df['ug_major'].str.contains('|'.join(tech_domain), na=False), 'ug_domain'] = 'Tech'
        df.loc[df['ug_major'].str.contains('|'.join(core_eng_domain), na=False), 'ug_domain'] = 'Core_Engineering'
        df.loc[df['ug_major'].str.contains('|'.join(business_domain), na=False), 'ug_domain'] = 'Business'
        df.loc[df['ug_major'].str.contains('|'.join(science_domain), na=False), 'ug_domain'] = 'Science'
        df.loc[df['ug_major'].str.contains('|'.join(arts_humanities_domain), na=False), 'ug_domain'] = 'Arts_Humanities'
        return df

    X_train = create_domain_features(X_train)
    X_val = create_domain_features(X_val)
    X_test = create_domain_features(X_test)
    print("✅ Domain features created successfully!")

    # --- Step 6: Skill Feature Engineering ---
    print("\n[6/9] Creating skill features...")
    def create_skill_features(df_in):
        df = df_in.copy()
        skills_str = df['skills'].astype(str).str.lower()

        # Create binary flags for key skill categories
        df['has_web_skills'] = skills_str.str.contains('javascript|html|css|react|django|node').astype(int)
        df['has_data_skills'] = skills_str.str.contains('python|sql|tableau|power bi|machine learning|data analysis').astype(int)
        df['has_cloud_skills'] = skills_str.str.contains('aws|azure|gcp|docker|cloud').astype(int)
        df['has_core_eng_skills'] = skills_str.str.contains('autocad|matlab|catia|ansys').astype(int)

        return df

    X_train = create_skill_features(X_train)
    X_val = create_skill_features(X_val)
    X_test = create_skill_features(X_test)
    print("✅ Skill features created successfully!")

    # --- Step 7: Process and Vectorize Text with Sentence-BERT (GPU-Accelerated) ---
    print("\n[7/9] 🚀 Loading SBERT model and vectorizing text features...")
    print(f"   Using device: {device.upper()}")
    
    # Load SBERT model and explicitly move to GPU if available
    sbert_model = SentenceTransformer('all-MiniLM-L6-v2', device=device)
    
    if device == 'cuda':
        print(f"   ✅ SBERT model loaded on GPU: {torch.cuda.get_device_name(0)}")
        # Optimize batch size for GPU
        batch_size = 128  # Larger batch size for GPU
    else:
        print("   ⚠️  SBERT running on CPU")
        batch_size = 64  # Smaller batch size for CPU
    
    text_cols_to_vectorize = ['skills', 'interests', 'certification_title']

    def vectorize_text_features(df_in, model, batch_sz):
        df = df_in.copy()
        for col in text_cols_to_vectorize:
            print(f"   - Vectorizing '{col}' (batch_size={batch_sz})...")
            df[col].fillna('', inplace=True)
            
            # Encode on GPU with progress bar
            embeddings = model.encode(
                df[col].tolist(), 
                show_progress_bar=True,
                batch_size=batch_sz,
                device=device,
                convert_to_numpy=True
            )
            
            vec_df = pd.DataFrame(embeddings, index=df.index).add_prefix(f'{col}_sbert_')
            df = pd.concat([df, vec_df], axis=1)
            df.drop(columns=[col], inplace=True)
            
            # Clear GPU cache after each column
            if device == 'cuda':
                torch.cuda.empty_cache()
                
        return df

    X_train = vectorize_text_features(X_train, sbert_model, batch_size)
    X_val = vectorize_text_features(X_val, sbert_model, batch_size)
    X_test = vectorize_text_features(X_test, sbert_model, batch_size)
    
    # Final GPU cleanup
    if device == 'cuda':
        torch.cuda.empty_cache()
        print(f"   📊 GPU Memory Used: {torch.cuda.memory_allocated(0) / 1e9:.2f} GB")
        
    print("✅ Text features vectorized successfully!")

    # --- Step 8: Encode and Scale Features ---
    print("\n[8/9] Encoding and scaling features...")
    categorical_cols = X_train.select_dtypes(include=['object', 'category']).columns
    numerical_cols = ['cgpa']

    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        # Fit on training data
        X_train[col] = le.fit_transform(X_train[col].astype(str))
        label_encoders[col] = le
        # Transform val and test sets, handling labels that weren't in the training data
        for dataset in [X_val, X_test]:
            dataset[col] = dataset[col].astype(str).map(lambda s: s if s in le.classes_ else '<unknown>')
            # Temporarily add '<unknown>' to the encoder's classes if it's not there
            if '<unknown>' not in le.classes_:
                le.classes_ = np.append(le.classes_, '<unknown>')
            dataset[col] = le.transform(dataset[col])
    print("   ✅ Categorical features encoded.")

    scaler = MinMaxScaler()
    X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
    X_val[numerical_cols] = scaler.transform(X_val[numerical_cols])
    X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])
    print("   ✅ Numerical features scaled.")

    # --- Step 9: Encode Target Variable ---
    y_encoder = LabelEncoder()
    y_train_encoded = y_encoder.fit_transform(y_train)
    y_val_encoded = y_encoder.transform(y_val)
    print("   ✅ Target variable encoded.")

    # --- Step 10: Save all preprocessing artifacts ---
    print("\n[9/9] 💾 Saving all files...")
    X_train.to_csv('train_features.csv', index=False)
    pd.DataFrame(y_train_encoded, columns=['target']).to_csv('train_target.csv', index=False)
    X_val.to_csv('validation_features.csv', index=False)
    pd.DataFrame(y_val_encoded, columns=['target']).to_csv('validation_target.csv', index=False)
    X_test.to_csv('test_features.csv', index=False)
    print("   ✅ Saved train, validation, and test CSV files.")

    with open("y_encoder.pkl", "wb") as f: pickle.dump(y_encoder, f)
    print("   ✅ Saved target variable encoder (y_encoder.pkl)")
    with open("feature_encoders.pkl", "wb") as f: pickle.dump(label_encoders, f)
    print("   ✅ Saved categorical feature encoders (feature_encoders.pkl)")
    with open("scaler.pkl", "wb") as f: pickle.dump(scaler, f)
    print("   ✅ Saved numerical scaler (scaler.pkl)")

    print("\n" + "="*60)
    print("🎉 PREPROCESSING COMPLETE!")
    print("="*60)
    if device == 'cuda':
        print(f"⚡ GPU Acceleration: ENABLED")
        print(f"   Device: {torch.cuda.get_device_name(0)}")
    else:
        print("⚠️  GPU Acceleration: DISABLED (CPU mode)")
    print("✅ All files saved successfully!")
    print("="*60)

except FileNotFoundError:
    print("\n❌ Error: 'career_recommender_augmented_eda.csv' not found.")
    print("   Make sure the file is in /kaggle/working/ directory")
except Exception as e:
    print(f"\n❌ An error occurred: {e}")
    import traceback
    traceback.print_exc()
