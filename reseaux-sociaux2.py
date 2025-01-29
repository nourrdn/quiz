import streamlit as st

def main():
    st.title("Quiz : Les réseaux sociaux et la sociabilité des jeunes")
    
    questions = [
        ("Quel est l’un des principaux avantages des réseaux sociaux pour les jeunes ?", [
            "L’isolement et la solitude",
            "La réduction des contacts avec la famille",
            "La possibilité de créer et entretenir des relations sociales à distance"
        ], 2),
        ("Quelle plateforme est particulièrement utilisée pour partager des vidéos courtes et virales ?", [
            "WhatsApp",
            "TikTok",
            "LinkedIn"
        ], 1),
        ("Comment les réseaux sociaux peuvent-ils favoriser l’intégration des jeunes introvertis ?", [
            "En les forçant à parler en public",
            "En limitant leurs interactions sociales",
            "En leur offrant un espace d’expression où ils peuvent partager leurs idées plus facilement"
        ], 2),
        ("Quel risque est associé à l’algorithme de TikTok ?", [
            "Il bloque l’accès aux vidéos populaires",
            "Il encourage la lecture de livres",
            "Il favorise la dépendance en proposant du contenu personnalisé et engageant"
        ], 2),
        ("En quoi les réseaux sociaux peuvent-ils être un outil de solidarité ?", [
            "En supprimant les conversations sur les injustices",
            "En permettant la mobilisation autour de causes sociales et humanitaires",
            "En interdisant l’accès aux informations importantes"
        ], 1),
        ("Quel est l’un des principaux effets négatifs des réseaux sociaux sur la santé mentale des jeunes ?", [
            "Une réduction du temps passé en ligne",
            "Une amélioration de la confiance en soi",
            "Une augmentation du stress et de la comparaison sociale"
        ], 2),
        ("Comment le confinement a-t-il influencé l’utilisation des réseaux sociaux ?", [
            "Il a réduit leur importance dans la vie des jeunes",
            "Il a encouragé les rencontres physiques malgré les restrictions",
            "Il a entraîné une forte augmentation du temps passé sur les plateformes"
        ], 2),
        ("Quel phénomène négatif est amplifié par l’anonymat des réseaux sociaux ?", [
            "Le cyberharcèlement",
            "L’amélioration de la communication bienveillante",
            "La diminution des interactions en ligne"
        ], 0),
        ("Pourquoi les interactions en face à face restent-elles essentielles malgré l’essor des réseaux sociaux ?", [
            "Elles sont moins intéressantes que les discussions en ligne",
            "Elles sont inutiles dans un monde numérique",
            "Elles permettent de mieux comprendre les émotions et les signaux non verbaux"
        ], 2),
        ("Quel effet paradoxal les réseaux sociaux peuvent-ils avoir sur la sociabilité des jeunes ?", [
            "Ils empêchent totalement les interactions sociales",
            "Ils remplacent efficacement toutes les interactions physiques",
            "Ils favorisent les connexions tout en pouvant accentuer l’isolement"
        ], 2)
    ]
    
    score = 0
    user_answers = []
    
    for i, (question, options, correct_index) in enumerate(questions):
        st.write(f"### {i+1}. {question}")
        user_choice = st.radio("Choisissez une réponse:", options, key=i)
        if st.button(f"Valider la question {i+1}", key=f"btn_{i}"):
            if user_choice == options[correct_index]:
                st.success("Bonne réponse !")
                score += 1
            else:
                st.error(f"Mauvaise réponse. La bonne réponse est : {options[correct_index]}")
            user_answers.append(user_choice)
    
    if len(user_answers) == len(questions):
        st.write("### Quiz terminé !")
        st.write(f"Votre score final : {score} / {len(questions)}")

if __name__ == "__main__":
    main()