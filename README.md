# tp_turtle_regulation_-Junior-_-Gracieux-
#  TP - Turtle Regulation (ROS2)

Ce projet est un TP réalisé avec ROS2 et `turtlesim`. Il permet de réguler l’orientation d'une tortue virtuelle vers un **point cible (waypoint)** à l’aide d’un **contrôleur proportionnel**.
 
![Turtlesim Regulation Demo](https://via.placeholder.com/600x400?text=Turtle+Regulation+Demo)

Ce projet ROS2 permet de contrôler une tortue dans le simulateur `turtlesim` avec :
- **Régulation en distance** vers un waypoint
- **Contrôle d'orientation** proportionnel
- **Service** pour modifier le waypoint dynamiquement

## 📦 Structure du package

tp_turtle_regulation/
├── turtle_regulation/
│ ├── set_way_point.py # Nœud principal de régulation
│ ├── waypoint_service.py # Service de modification du waypoint
│ └── package.xml
├── turtle_interfaces/
│ ├── srv/
│ │ └── SetWayPoint.srv # Définition du service
│ └── package.xml
└── README.md

## 🚀 Installation & Exécution

1. **Cloner le dépôt** :
```bash
git clone https://github.com/Junior-Gracieux/tp_turtle_regulation.git
cd tp_turtle_regulation

👨💻 Auteurs

    Junior

    Gracieux
    *Année 2025 - Projet académique*

- `turtle_regulation/`
  - `set_way_point.py` : Noeud ROS2 qui aligne la tortue vers un waypoint fixe `(7.0, 7.0)`


