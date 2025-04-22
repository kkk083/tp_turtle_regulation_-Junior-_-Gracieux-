# 🐢 TP - Turtle Regulation (ROS2)

Ce projet est un TP réalisé avec ROS2 et le simulateur `turtlesim`. L’objectif est de réguler l’orientation d’une tortue virtuelle (`/turtle1`) vers un **waypoint fixe (7, 7)** à l’aide d’un **contrôleur proportionnel (P-controller)**.

---

## 📁 Structure du projet

```
tp_turtle_regulation/
└── turtle_regulation/
    ├── set_way_point.py        # Noeud principal
    ├── package.xml
    ├── setup.py
    └── ...
```

---

## 🚀 Installation

1. Cloner le dépôt Git :
   ```bash
   git clone https://github.com/<TON_UTILISATEUR>/tp_turtle_regulation.git
   ```

2. Se placer dans ton workspace ROS2 :
   ```bash
   cd ~/ros2_ws
   ```

3. Copier le package dans `src/` s’il n’y est pas encore :
   ```bash
   mv ~/Downloads/tp_turtle_regulation/turtle_regulation ~/ros2_ws/src/
   ```

4. Compiler le workspace :
   ```bash
   colcon build
   source install/setup.bash
   ```

---

## 🐢 Lancement

Ouvre **deux terminaux** :

### ✅ Terminal 1 : Lancer le simulateur

```bash
ros2 run turtlesim turtlesim_node
```

### ✅ Terminal 2 : Lancer le nœud `set_way_point`

```bash
source install/setup.bash
ros2 run turtle_regulation set_way_point
```

---

## ⚙️ Fonctionnement du nœud `set_way_point.py`

Le nœud :
- Souscrit au topic `/turtle1/pose` (`turtlesim/msg/Pose`) pour obtenir la position actuelle de la tortue,
- Calcule l’angle désiré entre la tortue et le point `(7.0, 7.0)` avec :
  \
  \( \theta_{\text{desire}} = \text{atan2}(y_{\text{waypoint}} - y, x_{\text{waypoint}} - x) \)
- Calcule l’erreur d’orientation :
  \
  \( e = \arctan\left(\tan\left(\frac{\theta_{\text{desire}} - \theta}{2}\right)\right) \)
- Génère une commande de rotation :
  \
  \( u = K_p \cdot e \)
- Publie la commande sur `/turtle1/cmd_vel` (`geometry_msgs/msg/Twist`) avec :
  - `angular.z = u`
  - `linear.x = 0.0` (la tortue ne se déplace pas vers le point, elle s’oriente uniquement)

---

## 📊 Tests de `Kp` – Influence sur le comportement

| Valeur de `Kp` | Comportement observé |
|----------------|----------------------|
| **0.5**        | Réaction très lente. La tortue tourne doucement vers le point. |
| **1.5**        | Mieux, mais encore lent pour de grands écarts d’angle. |
| **3.0**        | Bon compromis : réponse rapide et stable. ✅ (valeur par défaut) |
| **6.0**        | La tortue tourne vite, quelques petites oscillations. |
| **10.0**       | Instable : la tortue oscille et dépasse souvent l’angle cible. ❌ |

---

## 🛠 Commandes utiles

### 🔄 Réinitialiser la tortue

Ramène la tortue au centre de l’écran et efface la trace :
```bash
ros2 service call /reset std_srvs/srv/Empty
```

### 📡 Vérifier la pose de la tortue

```bash
ros2 topic echo /turtle1/pose
```

### 🧪 Tester une commande de rotation manuelle

```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist '{angular: {z: 2.0}}'
```

---

## 👨‍💻 Auteur

- **Junior Yissibi**  
- Étudiant à l’Université des Mascareignes  
- TP ROS2 — Régulation de cap avec turtlesim
