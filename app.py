from pathlib import Path 

import streamlit as st 
from PIL import Image


#-----PATH SETTING ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles" /"main.css"
resume_file =current_dir /"assets"/"MEZOUARI.pdf"
profile_pic= current_dir/"assets"/"IMG.png"




#----- general setting----
PAGE_TITLE = "Digital CV | MEZOUARI Mohamed"
PAGE_ICON =":wave:"
Name ="MEZOUARI Mohamed"
Description = """ 
Etudiant Master en Ingénierie des Énergies Renouvelables et Efficacité Énergétique. 
Licencié en énergies renouvelables. 
Technicien spécialisé en automatisation et instrumentation industrielle. """ 
Email = "mezouarii.mohamedd@gmail.com"
Tel="+212705425436"
Media_Social= {"LinkedIn":"https://www.linkedin.com/in/mohamed-mezouari/"}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

#--- lOAD CSS,PDF & PROFILE PIC---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
    with open (resume_file,"rb") as pdf_file:
        PDFbyte = pdf_file.read()
        profile_pic = Image.open(profile_pic)

#----HERO SECTION------
col1, col2 =st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)
    with col2:
        st.title(Name)
        st.write(Description)
        st.write ("Email",Email)
        st.write ("Telephone",Tel)
        st.download_button(
            label="Telecharger CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",)
        #st.write ("________________________________________")

                               
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(Media_Social))
for index, (platform, link) in enumerate(Media_Social.items()):
    cols[index].write(f"[{platform}]({link})")
    
    # Education
    education_data = [
        {
            "degree": "Master en Ingénierie des Énergies Renouvelables et Efficacité Énergétique",
            "option": "Réseau et Énergie Electriques",
            "school": "Beni Mellal- Faculté Polydisciplinaire",
            "date": "2022"
        },
        {
            "degree": "Licence professionnelle en énergies renouvelables",
            "school": "Beni Mellal- Faculté Polydisciplinaire",
            "date": "2019-2020"
        },
        {
            "degree": "Diplôme de technicien spécialisé en automatisation et instrumentation industrielle",
            "school": "Beni Mellal- Institut Spécialisé de Technologie Appliquée",
            "date": "2017-2019"
        },
        {
            "degree": "Baccalauréat en science expérimentale option sciences physique et chimie",
            "school": "Beni Mellal- lycée Zerktouni",
            "date": "2016-2017"
        }
    ]
    
    with st.expander("## FORMATIONS", expanded=True):
        for entry in education_data:
            st.write(f"**{entry['degree']}** - {entry['school']} ({entry['date']})")
            if 'option' in entry:
                st.write(f"    Option: {entry['option']}")

    # Experiences (stage and Education)
    experiences_data = [
        {
            "type": "Stage",
            "name": "AUTOMATION S.A.R.L, Casablanca",
            "position": " Département des travaux en qualité d’Automaticien.",
            "date": "Mars 2021-Juin 2021",
            "tasks": [
                "Programmation de PLC (automates programmables).",
                "Systèmes de contrôle et régulation.",
                "Interfaces homme-machine (IHM).",
                "Maintenance préventive.",
                "Documentation et rapports."
            ]
        },
        {
            "type": "Stage",
            "name": "CIMENTS DE L’ATLASSE, Ighrem Laàlam",
            "position": "Service Maintenance Electrique.",
            "date": "Avril 2021",
            "tasks": [
                "Diagnostic et Dépannage.",
                "Entretien Préventif."
            ]
        },
        {
            "type": "Éducation",
            "name": "Ecole Marocaine des Sciences et Techniques Industrielles, Beni Mellal",
            "position": "formation en automates programmables.",
            "date": "Décembre 2018-Mai 2019",
            "tasks": [
                "Comprendre les Concepts de Base.",
                "Programmation Structurée.",
                "Pratique en Laboratoire/Simulation."
            ]
        }
    ]
    
    with st.expander("## EXPERIENCES PROFESSIONNELLES", expanded=True):
        for entry in experiences_data:
            st.write(f"**{entry['type']}**: {entry['name']} - {entry['position']} ({entry['date']})")
            for task in entry['tasks']:
                st.write(f"* {task}")

    # Technical Skills
    technical_skills_data = [
        {
            "category": "Énergies renouvelables",
            "skills": ["WindPRO", "SolidWorks"]
        },
        {
            "category": "Langages de programmation",
            "skills": ["Python", "C", "Ladder", "Grafcet"]
        },
        {
            "category": "Méthode numérique et programmation",
            "skills": ["Matlab"]
        },
        {
            "category": "Microcontrôleur",
            "skills": ["Arduino", "MicroC pro"]
        },
        {
            "category": "Systèmes industriels",
            "skills": ["Step 7 Professional", "Wincc Flexible", "EcoStruxure Machine Expert"]
        },
        {
            "category": "Simulation et conception des circuits électroniques",
            "skills": ["Proteus Professional"]
        }
    ]
    
    with st.expander("## COMPETENCES TECHNIQUES ", expanded=True):
        for entry in technical_skills_data:
            st.write(f"**{entry['category']}**")
            for skill in entry['skills']:
                st.write(f"* {skill}")

 # Projects
    projects_data = [
        {
            "title": "Projet de Fin d'Étude",
            "description": "Conception et Réalisation d'un Analyseur de Qualité d'Onduleur Photovoltaïque Embarqué 'THD Analyser' (2019-2020)."
        },
        {
            "title": "Projet",
            "description": "Modélisation d'une Cellule Photovoltaïque avec Logiciel Matlab (2019-2020)."
        },
        {
            "title": "Projet",
            "description": "Réalisation d'un Four Suiveur de Soleil à Base d'un Microcontrôleur (2018-2019)."
        }
    ]
    
    with st.expander("## PROJETS ", expanded=True):
        for project in projects_data:
            st.write(f"**{project['title']}** - {project['description']}")

    # Languages
    languages_data = [
        {
            "language": "Français",
            "level": "niveau seuil"
        },
        {
            "language": "Anglais",
            "level": "niveau seuil"
        },
        {
            "language": "Arabe",
            "level": "niveau autonome"
        }
    ]
    
    with st.expander("## Langues", expanded=True):
        for language_entry in languages_data:
            st.write(f"**{language_entry['language']}** - {language_entry['level']}")
    
    