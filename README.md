# FONT-HID

**Système de Thématisation Hacker/Pirate pour Linux**

**Développé par HiddenWorld Communauté Tchadienne**

---

## 🎯 Description

FONT-HID transforme complètement ton système Linux en environnement visuel de type hacker/pirate avec transparence, effets spéciaux, et fonctionnalités avancées. Inspiré des films et de la culture cyberpunk.

## ⚠️ Avertissements

- **Sauvegarde** tes configurations avant utilisation
- Ce script modifie le thème GTK, les icônes, le terminal, le fond d'écran, et les fichiers de configuration
- Fonctionne principalement sur Ubuntu/Debian avec GNOME ou XFCE
- Certaines fonctionnalités nécessitent `picom` ou `compton` pour la transparence

## 🚀 Installation

```bash
# Cloner ou télécharger
# Installer les dépendances
pip install -r requirements_FONT_HID.txt

# Lancer FONT-HID
python3 FONT_HID.py
```

## 🎨 Fonctionnalités

### Personnalisation Visuelle
- **Thème GTK** : Noir/vert matrix avec accents cyan
- **Icônes** : Style hacker/pirate personnalisé
- **Terminal** : Transparence, couleurs néon, police monospace
- **Fond d'écran** : Génération dynamique avec effets matrix
- **Curseur** : Style croixhair hacker
- **Police système** : Hack, JetBrains Mono, ou Fira Code

### Transparence & Effets
- **Picom/Compton** : Configuration optimisée pour la transparence
- **Opacité fenêtres** : 85-95% selon le type
- **Effets de flou** : Arrière-plan flou pour les fenêtres
- **Ombres** : Ombres néon colorées
- **Animations** : Transitions fluides

### Terminal Avancé
- **Tilix/Terminator** : Configuration avec transparence
- **ZSH + Oh-My-ZSH** : Thème powerlevel10k
- **Plugins** : Autosuggestions, syntax highlighting
- **Prompt** : Informations système en temps réel
- **Alias** : Commandes raccourcies style hacker

### Widgets & Monitoring
- **Conky** : Widgets système sur le bureau
- **CPU/RAM/GPU** : Monitoring en temps réel
- **Réseau** : Bande passante, connexions actives
- **Processus** : Top processus consommateurs
- **Horloge** : Style digital/matrix

### Sécurité & Privacy
- **Firewall** : Configuration UFW optimisée
- **MAC Changer** : Changement automatique de MAC
- **Tor** : Configuration proxy Tor
- **VPN** : Gestionnaire de connexions VPN
- **Chiffrement** : Outils de chiffrement de fichiers

### Outils Hacker Intégrés
- **Menu rapide** : Accès aux outils de pentest
- **Raccourcis clavier** : Lancement rapide des outils
- **Scripts** : Collection de scripts utiles
- **Templates** : Fichiers de configuration pré-configurés

## 🎮 Utilisation

### Menu Principal
```
1. Thème Complet (Tout appliquer)
2. Thème GTK Seul
3. Icônes Seules
4. Terminal Personnalisé
5. Fond d'Écran Dynamique
6. Conky Widgets
7. Picom Transparence
8. ZSH + Oh-My-ZSH
9. Police Système
10. Curseur Personnalisé
11. Menu Hacker
12. Firewall & Sécurité
13. MAC Changer
14. Configuration Tor
15. Gestionnaire VPN
16. Outils Chiffrement
17. Raccourcis Clavier
18. Scripts Utilitaires
19. Sauvegarder Config
20. Restaurer Config
21. Voir l'Aperçu
22. À Propos
23. Quitter
```

### Commandes Rapides
Après installation, utilise ces raccourcis :
- `Ctrl+Alt+T` : Terminal transparent
- `Ctrl+Alt+H` : Menu hacker
- `Ctrl+Alt+M` : Monitoring système
- `Ctrl+Alt+N` : Nouvelle fenêtre terminal
- `Ctrl+Alt+F` : Plein écran
- `Super+Space` : Lanceur d'applications

## 🔧 Configuration Manuelle

### Picom (Transparence)
```bash
# Vérifier que picom est installé
sudo apt install picom

# Lancer picom avec la config FONT-HID
picom --config ~/.config/picom/picom.conf
```

### Conky (Widgets)
```bash
# Installer conky
sudo apt install conky-all

# Lancer conky
conky -c ~/.config/conky/conky.conf
```

### ZSH
```bash
# Installer zsh
sudo apt install zsh

# Définir comme shell par défaut
chsh -s $(which zsh)
```

## 🛡️ Sécurité

Ce script :
- Ne modifie pas les fichiers système critiques
- Crée des sauvegardes automatiques
- Peut être désinstallé proprement
- Respecte la privacy (pas de données envoyées)

## 📝 Fichiers Modifiés

- `~/.bashrc` / `~/.zshrc`
- `~/.config/gtk-3.0/`
- `~/.config/picom/`
- `~/.config/terminator/` ou `~/.config/tilix/`
- `~/.config/conky/`
- `~/.themes/`
- `~/.icons/`
- `/usr/share/themes/` (avec sudo)

## 🎓 Crédits

**HiddenWorld Communauté Tchadienne**
- Concepteur : Hacker Tchadien
- Contributeurs : Communauté HiddenWorld

## 📜 Licence

MIT License - Usage éducatif et personnel

---

**Transforme ton Linux en machine de guerre cybernétique !**
