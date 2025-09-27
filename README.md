# Ce dépôt est en cours de configuration CI/CD. 

run the server

```bash
flask --app app run
```

init some data

```bash
flask --app main sample-data
```

## Déploiement avec Docker

Pour conteneuriser l'application et la lancer de manière portable, suivez ces étapes :

### 1. Construire l'image Docker

Utilisez le `Dockerfile` fourni pour créer l'image.

```bash
# La commande -t (tag) permet de nommer l'image (ex: 'water-tracker-app')
docker build -t water-tracker-app .
