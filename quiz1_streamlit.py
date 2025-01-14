import streamlit as st
st.title("Quiz Interactif sur les Actualités")
st.write("Bienvenue dans ce quiz interactif. Testez vos connaissances sur les actualités récentes !")
if "score" not in st.session_state:
    st.session_state.score = 0

if "validated_questions" not in st.session_state:
    st.session_state.validated_questions = set()
questions = [
    {
        "question": "Quel projet de loi est actuellement débattu au Maroc pour encadrer le droit de grève ?",
        "options": ["Loi organique n°97.15", "Loi sur la liberté d'expression n°45.10", "Loi sur la justice sociale n°23.08"],
        "answer": "Loi organique n°97.15",
    },
    {
        "question": "Combien d’accords économiques ont été signés entre la France et le Maroc en octobre 2024 ?",
        "options": ["10", "15", "22"],
        "answer": "22",
    },
    {
        "question": "Lors de la manifestation à Casablanca, quel sujet controversé a déclenché les protestations ?",
        "options": ["Le discours d’Emmanuel Macron", "Une réforme sur l’éducation", "Un projet de loi sur l’immigration"],
        "answer": "Le discours d’Emmanuel Macron",
    },
    {
        "question": "Comment s’appelle la première marketplace cloud souveraine lancée au Maroc en 2025 ?",
        "options": ["Cloud Atlas", "Rkube", "Atlas Cloud Services (ACS)"],
        "answer": "Atlas Cloud Services (ACS)",
    },
    {
        "question": "En novembre 2024, Casablanca a été frappée par une canicule inhabituelle. Quelle température a-t-on dépassée ?",
        "options": ["30°C", "33°C", "35°C"],
        "answer": "33°C",
    },
    {
        "question": "Quels pays ont intégré l’espace Schengen en janvier 2025 après treize ans d’attente ?",
        "options": ["Roumanie et Bulgarie", "Croatie et Slovénie", "Grèce et Hongrie"],
        "answer": "Roumanie et Bulgarie",
    },
    {
        "question": "À combien s’élève désormais le SMIC net en France depuis novembre 2024 ?",
        "options": ["1 426,30 €", "1 500,00 €", "1 600,50 €"],
        "answer": "1 426,30 €",
    },
    {
        "question": "Quel événement a poussé des milliers de Roumains à manifester en janvier 2025 ?",
        "options": ["L'annulation de l’élection présidentielle", "Une réforme des retraites", "Une nouvelle loi sur la presse"],
        "answer": "L'annulation de l’élection présidentielle",
    },
    {
        "question": "Où s’est tenu le Web Summit de novembre 2024, rassemblant des milliers de participants ?",
        "options": ["Paris", "Lisbonne", "Berlin"],
        "answer": "Lisbonne",
    },
    {
        "question": "Quel phénomène climatique a menacé Mayotte en janvier 2025 ?",
        "options": ["Une éruption volcanique", "Une tempête tropicale", "Un tsunami"],
        "answer": "Une tempête tropicale",
    },
    {
        "question": "En décembre 2024, quel dirigeant syrien a fui son pays après la chute de son régime ?",
        "options": ["Bachar Al-Assad", "Hassan Rouhani", "Mahmoud Abbas"],
        "answer": "Bachar Al-Assad",
    },
    {
        "question": "Quelle décision controversée a suscité des manifestations en Géorgie depuis octobre 2024 ?",
        "options": [
            "Suspension du processus d’adhésion à l’UE",
            "Suppression de la langue géorgienne dans les écoles",
            "Fermeture des frontières avec la Russie",
        ],
        "answer": "Suspension du processus d’adhésion à l’UE",
    },
    {
        "question": "Quel président américain a opposé son veto à l’acquisition d’U.S. Steel en janvier 2025 ?",
        "options": ["Joe Biden", "Donald Trump", "Kamala Harris"],
        "answer": "Joe Biden",
    },
    {
        "question": "Quels outils technologiques Meta a-t-il intégrés dans ses plateformes en 2024 ?",
        "options": [
            "Assistants vocaux",
            "Génération d’images par IA et chatbots",
            "Applications de réalité augmentée",
        ],
        "answer": "Génération d’images par IA et chatbots",
    },
    {
        "question": "Lors de la COP29, quel montant annuel de financement pour les pays en développement a été fixé ?",
        "options": ["200 milliards de dollars", "300 milliards de dollars", "400 milliards de dollars"],
        "answer": "300 milliards de dollars",
    },
]
for index, q in enumerate(questions, start=1):
    st.subheader(f"Question {index}")
    user_answer = st.radio(q["question"], q["options"], key=f"q{index}")

    if st.button(f"Valider la réponse {index}", key=f"btn_{index}"):
        if index not in st.session_state.validated_questions:
            if user_answer == q["answer"]:
                st.success("Bonne réponse !")
                st.session_state.score += 1
            else:
                st.error("Mauvaise réponse.")
            st.session_state.validated_questions.add(index)

if st.button("Afficher le score final"):
    st.write(f"Votre score final est : {st.session_state.score}/{len(questions)}")
