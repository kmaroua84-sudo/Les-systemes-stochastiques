# Projet de présentation — Modèle de percolation

## Contenu
- `presentation/index.html` : présentation Reveal.js animée.
- `simulation/app.py` : application Python/Streamlit interactive.
- `simulation/requirements.txt` : dépendances de la simulation.

## 1) Tester la simulation sur votre ordinateur
Installez Python, puis dans le dossier `simulation` exécutez :

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 2) Publier gratuitement la simulation
1. Créez un dépôt GitHub et ajoutez le dossier `simulation`.
2. Ouvrez Streamlit Community Cloud et connectez votre GitHub.
3. Choisissez le dépôt, la branche et `simulation/app.py`.
4. Déployez l'application et copiez son URL publique.
5. Dans `presentation/index.html`, remplacez `https://percolation-demo.streamlit.app/?embed=true` par votre URL suivie de `?embed=true`.

La disponibilité de l'intégration iframe dépend des paramètres de sécurité et du navigateur. Si l'intégration est bloquée, gardez un bouton/lien de secours vers l'application.

## 3) Ouvrir la présentation
Ouvrez `presentation/index.html` dans un navigateur connecté à Internet. Pour la publier, vous pouvez activer GitHub Pages sur le dépôt (dossier racine ou `/presentation` selon l'organisation du dépôt).

## 4) Travail à cinq
Ajoutez les quatre autres membres comme Collaborators dans GitHub. Pour éviter les conflits, répartissez les fichiers : certaines modifient les diapositives, une personne la simulation, une autre vérifie le contenu scientifique. Évitez de modifier simultanément le même fichier.

## À personnaliser avant la soutenance
- Noms des cinq étudiantes, université, encadrant et année.
- URL Streamlit dans l'iframe.
- Vérifier la convention de voisinage demandée par l'enseignant (ici : voisinage par les côtés, pas les diagonales).
- Refaire les essais avec plusieurs valeurs de p et insérer vos propres résultats/commentaires.
