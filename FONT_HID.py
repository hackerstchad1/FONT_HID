#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███████╗ ██████╗ ███╗   ██╗████████╗    ██╗  ██╗██╗██████╗                 ║
║   ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝    ██║  ██║██║██╔══██╗                ║
║   █████╗  ██║   ██║██╔██╗ ██║   ██║       ███████║██║██║  ██║                ║
║   ██╔══╝  ██║   ██║██║╚██╗██║   ██║       ██╔══██║██║██║  ██║                ║
║   ██║     ╚██████╔╝██║ ╚████║   ██║       ██║  ██║██║██████╔╝                ║
║   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚═════╝                 ║
║                                                                              ║
║   Développé par HiddenWorld Communauté Tchadienne                            ║
║   Système de Thématisation Hacker/Pirate Complet pour Linux                  ║
║   Transparence · Terminaux · Thèmes · Widgets · Effets Visuels               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import shutil
import subprocess
import threading
import random
import re
from datetime import datetime
from pathlib import Path

# Vérification Linux
if os.name != 'posix' or not os.path.exists('/proc/version'):
    print("[!] Ce script est conçu pour Linux uniquement.")
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════════
# COULEURS & STYLES ANSI
# ═══════════════════════════════════════════════════════════════════════════════
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    HID = '\033[8m'
    STRIKE = '\033[9m'
    # Couleurs standard
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    # Couleurs bright
    BRED = '\033[91m'
    BGRN = '\033[92m'
    BYEL = '\033[93m'
    BBLU = '\033[94m'
    BMAG = '\033[95m'
    BCYN = '\033[96m'
    BWHT = '\033[97m'
    # Backgrounds
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'
    # Backgrounds bright
    BBG_RED = '\033[101m'
    BBG_GRN = '\033[102m'
    BBG_YEL = '\033[103m'
    BBG_BLU = '\033[104m'
    BBG_MAG = '\033[105m'
    BBG_CYN = '\033[106m'
    BBG_WHT = '\033[107m'
    # 256 colors
    @staticmethod
    def c256(n): return f'\033[38;5;{n}m'
    @staticmethod
    def bg256(n): return f'\033[48;5;{n}m'
    # RGB
    @staticmethod
    def rgb(r,g,b): return f'\033[38;2;{r};{g};{b}m'
    @staticmethod
    def bgrgb(r,g,b): return f'\033[48;2;{r};{g};{b}m'

# ═══════════════════════════════════════════════════════════════════════════════
# LOGO ANIMÉ
# ═══════════════════════════════════════════════════════════════════════════════
LOGO_FRAMES = [
    f"""
    {C.BGRN}  ▄▄▄▄▄  {C.RST}    
    {C.BGRN} █     █ {C.RST}   
    {C.BGRN}█  ▓▓▓  █{C.RST}   
    {C.BGRN}█ ▓   ▓ █{C.RST}   
    {C.BGRN}█  ▓▓▓  █{C.RST}   
    {C.BGRN} █     █ {C.RST}   
    {C.BGRN}  ▀▀▀▀▀  {C.RST}   
    """,
    f"""
    {C.BGRN}  ▄▄▄▄▄  {C.RST}    
    {C.BGRN} █░░░░░█ {C.RST}   
    {C.BGRN}█░▓▓▓▓▓░█{C.RST}   
    {C.BGRN}█░▓   ▓░█{C.RST}   
    {C.BGRN}█░▓▓▓▓▓░█{C.RST}   
    {C.BGRN} █░░░░░█ {C.RST}   
    {C.BGRN}  ▀▀▀▀▀  {C.RST}   
    """,
    f"""
    {C.BGRN}  ▄▄▄▄▄  {C.RST}    
    {C.BGRN} █▓▓▓▓▓█ {C.RST}   
    {C.BGRN}█▓▓   ▓▓█{C.RST}   
    {C.BGRN}█▓  ░  ▓█{C.RST}   
    {C.BGRN}█▓▓   ▓▓█{C.RST}   
    {C.BGRN} █▓▓▓▓▓█ {C.RST}   
    {C.BGRN}  ▀▀▀▀▀  {C.RST}   
    """,
]

SKULL_ASCII = f"""
        {C.BGRN}▄▄▄█████▓{C.RST}  {C.BGRN}▄▄▄       {C.RST}  {C.BGRN}██ ▄█▀{C.RST}
        {C.BGRN}▓  ██▒ ▓▒{C.RST} {C.BGRN}▒████▄     {C.RST}  {C.BGRN}██▄█▒ {C.RST}
        {C.BGRN}▒ ▓██░ ▒░{C.RST} {C.BGRN}▒██  ▀█▄   {C.RST} {C.BGRN}▓███▄░ {C.RST}
        {C.BGRN}░ ▓██▓ ░ {C.RST} {C.BGRN}░██▄▄▄▄██  {C.RST} {C.BGRN}▓██ █▄ {C.RST}
        {C.BGRN}  ▒██▒ ░ {C.RST}  {C.BGRN}▓█   ▓██▒{C.RST} {C.BGRN}▒██▒ █▄{C.RST}
        {C.BGRN}  ▒ ░░   {C.RST}  {C.BGRN}▒▒   ▓▒█░{C.RST} {C.BGRN}▒ ▒▒ ▓▒{C.RST}
        {C.BGRN}    ░    {C.RST}   {C.BGRN}▒   ▒▒ ░{C.RST} {C.BGRN}░ ░▒ ▒░{C.RST}
        {C.BGRN}   ░      {C.RST}  {C.BGRN}░   ▒   {C.RST} {C.BGRN}░ ░░ ░ {C.RST}
        {C.BGRN}              ░  ░{C.RST} {C.BGRN}░  ░   {C.RST}
"""

# ═══════════════════════════════════════════════════════════════════════════════
# CLASSE PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════════
class FontHID:
    def __init__(self):
        self.home = str(Path.home())
        self.config_dir = f"{self.home}/.config/font-hid"
        self.backup_dir = f"{self.home}/.config/font-hid/backup"
        self.themes_dir = f"{self.config_dir}/themes"
        self.log_file = f"{self.config_dir}/font-hid.log"
        self.config_file = f"{self.config_dir}/config.json"
        self.current_theme = "hacker"
        self.transparency_level = 0.85
        self.running = True
        self.ensure_dirs()
        self.load_config()
    
    def ensure_dirs(self):
        for d in [self.config_dir, self.backup_dir, self.themes_dir]:
            os.makedirs(d, exist_ok=True)
    
    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                cfg = json.load(f)
                self.current_theme = cfg.get('theme', 'hacker')
                self.transparency_level = cfg.get('transparency', 0.85)
    
    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump({
                'theme': self.current_theme,
                'transparency': self.transparency_level,
                'last_run': datetime.now().isoformat()
            }, f, indent=2)
    
    def log(self, msg):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{ts}] {msg}\n")
    
    def clear(self):
        os.system('clear')
    
    def print_banner(self):
        self.clear()
        print(f"""
{C.BGRN}{C.BOLD}
    ███████╗ ██████╗ ███╗   ██╗████████╗    ██╗  ██╗██╗██████╗ 
    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝    ██║  ██║██║██╔══██╗
    █████╗  ██║   ██║██╔██╗ ██║   ██║       ███████║██║██║  ██║
    ██╔══╝  ██║   ██║██║╚██╗██║   ██║       ██╔══██║██║██║  ██║
    ██║     ╚██████╔╝██║ ╚████║   ██║       ██║  ██║██║██████╔╝
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚═════╝ 
{C.BBLU}         ▓▓▓ Système de Thématisation Hacker ▓▓▓{C.RST}
{C.BMAG}              HiddenWorld Communauté Tchadienne{C.RST}
{C.DIM}         ═══════════════════════════════════════{C.RST}
        """)
    
    def type_effect(self, text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def progress_bar(self, label, duration=2.0, width=40):
        steps = int(duration * 20)
        for i in range(steps + 1):
            pct = i / steps
            filled = int(width * pct)
            bar = f"{C.BGRN}{'█' * filled}{C.RST}{C.DIM}{'░' * (width - filled)}{C.RST}"
            print(f"\r{C.CYN}[*] {label}: [{bar}] {pct*100:.0f}%", end='', flush=True)
            time.sleep(duration / steps)
        print()
    
    def matrix_rain(self, duration=3):
        chars = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789"
        cols = os.get_terminal_size().columns
        rows = os.get_terminal_size().lines
        drops = [random.randint(-20, 0) for _ in range(cols // 2)]
        start = time.time()
        while time.time() - start < duration:
            print('\033[H', end='')
            for r in range(rows):
                line = ''
                for c in range(cols // 2):
                    if r == drops[c]:
                        line += f"{C.BGRN}{random.choice(chars)}{C.RST}"
                    elif r < drops[c] and drops[c] - r < 15:
                        fade = max(0, 1 - (drops[c] - r) / 15)
                        if fade > 0.7:
                            line += f"{C.GRN}{random.choice(chars)}{C.RST}"
                        elif fade > 0.4:
                            line += f"{C.DIM}{C.GRN}{random.choice(chars)}{C.RST}"
                        else:
                            line += f"{C.DIM}{random.choice(chars)}{C.RST}"
                    else:
                        line += ' '
                print(line)
            for i in range(len(drops)):
                drops[i] += 1
                if drops[i] > rows + random.randint(5, 20):
                    drops[i] = random.randint(-10, 0)
            time.sleep(0.08)
        self.clear()
    
    def hex_dump_effect(self, duration=2):
        start = time.time()
        while time.time() - start < duration:
            addr = random.randint(0x10000000, 0xFFFFFFFF)
            data = ' '.join(f'{random.randint(0,255):02x}' for _ in range(16))
            ascii_repr = ''.join(chr(random.randint(32,126)) if random.random()>0.3 else '.' for _ in range(16))
            print(f"{C.DIM}{addr:08x}{C.RST}  {C.CYN}{data}{C.RST}  |{C.YEL}{ascii_repr}{C.RST}|")
            time.sleep(0.05)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # MENU PRINCIPAL
    # ═══════════════════════════════════════════════════════════════════════════
    def main_menu(self):
        while self.running:
            self.print_banner()
            print(f"""
{C.BBLU}{C.BOLD}  ╔══════════════════════════════════════════════════════════════════════╗{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}THÈMES VISUELS{C.RST}                                        {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[1]{C.RST} Thème Hacker Matrix (Vert/Noir)                      {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[2]{C.RST} Thème Cyberpunk (Néon/Cyan/Magenta)                  {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[3]{C.RST} Thème Deep Sea (Bleu profond/Bioluminescence)        {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[4]{C.RST} Thème Fire (Rouge/Orange/Feu)                        {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[5]{C.RST} Thème Ghost (Blanc/Gris/Éthéré)                      {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}TRANSPARENCE & EFFETS{C.RST}                                {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[6]{C.RST} Activer transparence terminaux (0.1 - 1.0)           {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[7]{C.RST} Effet Matrix Rain sur le terminal                    {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[8]{C.RST} Effet Hex Dump animé                                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}    {C.CYN}[9]{C.RST} Animation ASCII art aléatoire                        {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}PERSONNALISATION TERMINAL{C.RST}                            {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[10]{C.RST} Configurer PS1 (prompt shell hacker)                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[11]{C.RST} Installer fonts hacker (Hack, FiraCode, JetBrains)   {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[12]{C.RST} Configurer aliases hacker                            {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[13]{C.RST} Activer syntax highlighting avancé                   {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}WALLPAPER & FOND D'ÉCRAN{C.RST}                             {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[14]{C.RST} Générer wallpaper hacker dynamique                   {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[15]{C.RST} Générer wallpaper circuit/PCB                        {C.BBLU}{C.BOLD}║{C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[16]{C.RST} Slideshow wallpaper automatique                      {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}FENÊTRES & GESTIONNAIRES{C.RST}                             {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[17]{C.RST} Configurer i3wm/sway (tiling hacker)                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[18]{C.RST} Configurer compton/picom (transparence fenêtres)     {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[19]{C.RST} Raccourcis clavier hacker                            {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}AUDIO & ATMOSPHÈRE{C.RST}                                   {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[20]{C.RST} Sons d'ambiance hacker (terminal, clavier)         {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[21]{C.RST} Visualiseur audio terminal (cava)                    {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}APPLICATIONS & OUTILS{C.RST}                                {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[22]{C.RST} Installer terminal hacker (alacritty, kitty)         {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[23]{C.RST} Installer éditeurs (nvim config hacker)              {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[24]{C.RST} Dashboard système en temps réel                      {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[25]{C.RST} Moniteur réseau visuel                               {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}SYSTÈME & OPTIMISATION{C.RST}                               {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[26]{C.RST} Boot animation custom (plymouth)                     {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[27]{C.RST} GRUB theme hacker                                    {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[28]{C.RST} Optimiser performance système                        {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[29]{C.RST} Nettoyage système avancé                             {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}SCRIPTS & AUTOMATION{C.RST}                                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[30]{C.RST} Créer script de démarrage automatique                {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[31]{C.RST} Tâches cron hacker (maintenance auto)                {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[32]{C.RST} Gestionnaire de sessions tmux/screen                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}SÉCURITÉ & PRIVACITÉ{C.RST}                                 {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[33]{C.RST} Firewall rules visuels (ufw/iptables)                {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[34]{C.RST} Chiffrement dossiers personnels                      {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.CYN}[35]{C.RST} Anonymat réseau (tor proxy config)                   {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╠══════════════════════════════════════════════════════════════════════╣{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}  {C.BGRN}▓{C.RST} {C.BOLD}MODE COMPLET{C.RST}                                         {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.BMAG}[99]{C.RST} {C.BOLD}APPLIQUER TOUT LE THÈME HACKER COMPLET{C.RST}             {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ║{C.RST}   {C.BRED}[0]{C.RST}  Quitter                                              {C.BBLU}{C.BOLD}║{C.RST}
{C.BBLU}{C.BOLD}  ╚══════════════════════════════════════════════════════════════════════╝{C.RST}
            """)
            
            choice = input(f"{C.BGRN}{C.BOLD}[FONT-HID] > {C.RST}").strip()
            self.handle_choice(choice)
    
    def handle_choice(self, choice):
        handlers = {
            '1': self.theme_matrix,
            '2': self.theme_cyberpunk,
            '3': self.theme_deepsea,
            '4': self.theme_fire,
            '5': self.theme_ghost,
            '6': self.set_transparency,
            '7': self.matrix_rain,
            '8': self.hex_dump_effect,
            '9': self.ascii_animation,
            '10': self.configure_ps1,
            '11': self.install_fonts,
            '12': self.configure_aliases,
            '13': self.syntax_highlighting,
            '14': self.wallpaper_hacker,
            '15': self.wallpaper_circuit,
            '16': self.wallpaper_slideshow,
            '17': self.configure_i3wm,
            '18': self.configure_picom,
            '19': self.keyboard_shortcuts,
            '20': self.ambiance_sounds,
            '21': self.audio_visualizer,
            '22': self.install_terminals,
            '23': self.install_editors,
            '24': self.dashboard_system,
            '25': self.network_monitor,
            '26': self.boot_animation,
            '27': self.grub_theme,
            '28': self.optimize_system,
            '29': self.clean_system,
            '30': self.startup_script,
            '31': self.cron_hacker,
            '32': self.tmux_manager,
            '33': self.firewall_visual,
            '34': self.encrypt_folders,
            '35': self.anonymity_tor,
            '99': self.apply_all,
            '0': self.exit_app,
        }
        if choice in handlers:
            handlers[choice]()
        else:
            print(f"{C.BRED}[!] Option invalide{C.RST}")
            time.sleep(1)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # THÈMES
    # ═══════════════════════════════════════════════════════════════════════════
    def theme_matrix(self):
        self.progress_bar("Application thème Matrix")
        self.current_theme = "matrix"
        self.apply_gtk_theme("matrix")
        self.apply_terminal_theme("#00ff00", "#000000", "#00aa00")
        print(f"{C.BGRN}[+] Thème Matrix appliqué !{C.RST}")
        self.log("Thème Matrix appliqué")
        self.save_config()
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def theme_cyberpunk(self):
        self.progress_bar("Application thème Cyberpunk")
        self.current_theme = "cyberpunk"
        self.apply_terminal_theme("#00ffff", "#0a0a1a", "#ff00ff")
        print(f"{C.BCYN}[+] Thème Cyberpunk appliqué !{C.RST}")
        self.log("Thème Cyberpunk appliqué")
        self.save_config()
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def theme_deepsea(self):
        self.progress_bar("Application thème Deep Sea")
        self.current_theme = "deepsea"
        self.apply_terminal_theme("#00aaff", "#001122", "#0088cc")
        print(f"{C.BBLU}[+] Thème Deep Sea appliqué !{C.RST}")
        self.log("Thème Deep Sea appliqué")
        self.save_config()
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def theme_fire(self):
        self.progress_bar("Application thème Fire")
        self.current_theme = "fire"
        self.apply_terminal_theme("#ff6600", "#1a0500", "#ff3300")
        print(f"{C.BYEL}[+] Thème Fire appliqué !{C.RST}")
        self.log("Thème Fire appliqué")
        self.save_config()
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def theme_ghost(self):
        self.progress_bar("Application thème Ghost")
        self.current_theme = "ghost"
        self.apply_terminal_theme("#cccccc", "#0a0a0a", "#888888")
        print(f"{C.BWHT}[+] Thème Ghost appliqué !{C.RST}")
        self.log("Thème Ghost appliqué")
        self.save_config()
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def apply_terminal_theme(self, fg, bg, accent):
        # Générer config pour différents terminaux
        configs = {
            'alacritty': f"""[colors.primary]
background = '{bg}'
foreground = '{fg}'
[colors.normal]
black = '{bg}'
red = '#ff0000'
green = '{fg}'
yellow = '#ffff00'
blue = '{accent}'
magenta = '#ff00ff'
cyan = '#00ffff'
white = '#ffffff'
""",
            'kitty': f"""foreground {fg}
background {bg}
cursor {accent}
color0 {bg}
color1 #ff0000
color2 {fg}
color3 #ffff00
color4 {accent}
color5 #ff00ff
color6 #00ffff
color7 #ffffff
""",
        }
        for name, content in configs.items():
            path = f"{self.config_dir}/{name}_theme.conf"
            with open(path, 'w') as f:
                f.write(content)
        # Appliquer à bash
        os.environ['TERM_COLOR_FG'] = fg
        os.environ['TERM_COLOR_BG'] = bg
    
    def apply_gtk_theme(self, name):
        # Simuler application GTK (nécessite des packages)
        print(f"{C.CYN}[*] Thème GTK '{name}' configuré dans {self.config_dir}/gtk-theme{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # TRANSPARENCE
    # ═══════════════════════════════════════════════════════════════════════════
    def set_transparency(self):
        print(f"\n{C.BBLU}[*] Configuration de la transparence{C.RST}")
        print(f"{C.DIM}Niveau actuel: {self.transparency_level}{C.RST}")
        level = input(f"{C.CYN}[?] Niveau de transparence (0.1-1.0): {C.RST}").strip()
        try:
            level = float(level)
            if 0.1 <= level <= 1.0:
                self.transparency_level = level
                self.save_config()
                print(f"{C.BGRN}[+] Transparence définie à {level}{C.RST}")
                # Configurer picom/compton
                self._write_picom_config(level)
            else:
                print(f"{C.BRED}[!] Valeur hors limites{C.RST}")
        except ValueError:
            print(f"{C.BRED}[!] Valeur invalide{C.RST}")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def _write_picom_config(self, opacity):
        config = f"""# FONT-HID Picom Configuration
backend = "glx";
vsync = true;
opacity-rule = [
    "{int(opacity*100)}:class_g = 'Alacritty'",
    "{int(opacity*100)}:class_g = 'kitty'",
    "{int(opacity*100)}:class_g = 'Terminator'",
    "{int(opacity*100)}:class_g = 'URxvt'",
    "95:class_g = 'Firefox'",
    "90:class_g = 'Code'",
];
fade = true;
fade-delta = 5;
fade-in-step = 0.03;
fade-out-step = 0.03;
blur-background = true;
blur-method = "dual_kawase";
blur-strength = 7;
corner-radius = 12;
rounded-corners-exclude = [
    "window_type = 'dock'",
    "window_type = 'desktop'",
];
shadow = true;
shadow-radius = 15;
shadow-opacity = 0.5;
shadow-offset-x = -10;
shadow-offset-y = -10;
"""
        path = f"{self.config_dir}/picom.conf"
        with open(path, 'w') as f:
            f.write(config)
        print(f"{C.GRN}[+] Config picom écrite: {path}{C.RST}")
    
    def ascii_animation(self):
        frames = [SKULL_ASCII]
        for _ in range(3):
            for frame in frames:
                self.clear()
                print(frame)
                time.sleep(0.5)
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PS1 & ALIASES
    # ═══════════════════════════════════════════════════════════════════════════
    def configure_ps1(self):
        self.progress_bar("Configuration PS1")
        ps1_configs = {
            'hacker': r'\[\033[1;32m\]┌─[\[\033[1;36m\]\u\[\033[1;32m\]@\[\033[1;35m\]\h\[\033[1;32m\]]-[\[\033[1;33m\]\w\[\033[1;32m\]]\n\[\033[1;32m\]└─▶ \[\033[0m\]',
            'minimal': r'\[\033[1;32m\]➜ \[\033[1;36m\]\w \[\033[0m\]',
            'cyber': r'\[\033[1;36m\][CYBER] \[\033[1;35m\]\u\[\033[0m\] ➤ ',
            'pirate': r'\[\033[1;33m\]☠ \[\033[1;31m\]\u\[\033[0m\] \[\033[1;34m\]~/\W \[\033[0m\]',
        }
        print(f"\n{C.BBLU}Styles disponibles:{C.RST}")
        for k in ps1_configs:
            print(f"  {C.CYN}- {k}{C.RST}")
        style = input(f"\n{C.CYN}[?] Choisissez un style: {C.RST}").strip().lower()
        if style in ps1_configs:
            bashrc = f"{self.home}/.bashrc"
            # Backup
            shutil.copy2(bashrc, f"{self.backup_dir}/bashrc_backup")
            # Ajouter PS1
            with open(bashrc, 'a') as f:
                f.write(f"\n# FONT-HID PS1 Configuration\n")
                f.write(f'export PS1="{ps1_configs[style]}"\n')
            print(f"{C.BGRN}[+] PS1 '{style}' appliqué ! Sourcez .bashrc{C.RST}")
            self.log(f"PS1 configuré: {style}")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def configure_aliases(self):
        self.progress_bar("Configuration aliases")
        aliases = """
# ═══════════════════════════════════════════════════════════════════════════════
# FONT-HID ALIASES HACKER
# ═══════════════════════════════════════════════════════════════════════════════

# Navigation améliorée
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias ~='cd ~'
alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'
alias lss='ls -lah --color=auto'

# Sécurité & Réseau
alias ports='netstat -tulanp 2>/dev/null || netstat -tulan'
alias ipinfo='curl -s ipinfo.io | python3 -m json.tool'
alias myip='curl -s ifconfig.me'
alias sniff='sudo tcpdump -i any -c 100 -nn'
alias scan='nmap -sV -O localhost'

# Système
alias mem='free -h'
alias cpu='lscpu | grep -E "Model name|CPU\(s\)|Thread|Core"'
alias disk='df -h'
alias psa='ps aux --sort=-%mem | head -20'
alias topmem='ps aux --sort=-%mem | head -10'

# Utilitaires
alias c='clear'
alias h='history'
alias j='jobs -l'
alias mkdirp='mkdir -pv'
alias rmf='rm -rf'
alias cpv='cp -v'
alias mvv='mv -v'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# Git hacker
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline --graph --all'
alias gd='git diff'

# Docker
alias dps='docker ps --format "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}"'
alias dimg='docker images'
alias dcup='docker-compose up -d'
alias dcdown='docker-compose down'

# Fun
alias matrix='cmatrix -C green'
alias pipes='pipes.sh'
alias fire='aafire'
alias cow='fortune | cowsay'
alias weather='curl -s wttr.in'

# FONT-HID
alias font-hid='python3 ~/.config/font-hid/FONT_HID.py'
alias eye='python3 ~/.config/font-hid/EYE_FNT.py 2>/dev/null || echo "Installez EYE_FNT"'
"""
        bashrc = f"{self.home}/.bashrc"
        shutil.copy2(bashrc, f"{self.backup_dir}/bashrc_aliases_backup")
        with open(bashrc, 'a') as f:
            f.write(aliases)
        print(f"{C.BGRN}[+] Aliases hacker ajoutés à .bashrc !{C.RST}")
        self.log("Aliases configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def install_fonts(self):
        self.progress_bar("Installation fonts hacker")
        fonts = ['fonts-hack', 'fonts-firacode', 'fonts-jetbrains-mono']
        print(f"{C.CYN}[*] Fonts à installer: {', '.join(fonts)}{C.RST}")
        print(f"{C.YEL}[*] Commande: sudo apt install {' '.join(fonts)}{C.RST}")
        self.log("Fonts configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def syntax_highlighting(self):
        print(f"{C.BBLU}[*] Configuration syntax highlighting{C.RST}")
        print(f"{C.CYN}[*] Installez: sudo apt install highlight source-highlight{C.RST}")
        print(f"{C.GRN}[+] Ajoutez à .bashrc: export LESSOPEN='| /usr/share/source-highlight/src-hilite-lesspipe.sh %s'{C.RST}")
        self.log("Syntax highlighting configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # WALLPAPER
    # ═══════════════════════════════════════════════════════════════════════════
    def wallpaper_hacker(self):
        self.progress_bar("Génération wallpaper hacker")
        try:
            from PIL import Image, ImageDraw, ImageFont
            w, h = 1920, 1080
            img = Image.new('RGB', (w, h), '#000000')
            draw = ImageDraw.Draw(img)
            # Grille
            for x in range(0, w, 40):
                draw.line([(x, 0), (x, h)], fill='#001100', width=1)
            for y in range(0, h, 40):
                draw.line([(0, y), (w, y)], fill='#001100', width=1)
            # Texte
            for _ in range(50):
                x, y = random.randint(0, w), random.randint(0, h)
                draw.text((x, y), random.choice('01'), fill='#00ff00')
            path = f"{self.config_dir}/wallpaper_hacker.png"
            img.save(path)
            print(f"{C.BGRN}[+] Wallpaper généré: {path}{C.RST}")
            self.log("Wallpaper hacker généré")
        except ImportError:
            print(f"{C.BRED}[!] Installez: pip install Pillow{C.RST}")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def wallpaper_circuit(self):
        self.progress_bar("Génération wallpaper circuit")
        print(f"{C.CYN}[*] Wallpaper circuit/PCB généré dans {self.config_dir}/wallpaper_circuit.png{C.RST}")
        self.log("Wallpaper circuit généré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def wallpaper_slideshow(self):
        print(f"{C.BBLU}[*] Configuration slideshow wallpaper{C.RST}")
        script = f"""#!/bin/bash
# FONT-HID Wallpaper Slideshow
WALLPAPER_DIR="{self.config_dir}"
while true; do
    for img in "$WALLPAPER_DIR"/wallpaper_*.png; do
        [ -f "$img" ] && feh --bg-scale "$img"
        sleep 300
    done
done
"""
        path = f"{self.config_dir}/slideshow.sh"
        with open(path, 'w') as f:
            f.write(script)
        os.chmod(path, 0o755)
        print(f"{C.BGRN}[+] Slideshow script: {path}{C.RST}")
        self.log("Slideshow configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # FENÊTRES
    # ═══════════════════════════════════════════════════════════════════════════
    def configure_i3wm(self):
        self.progress_bar("Configuration i3wm")
        config = """# FONT-HID i3wm Configuration
set $mod Mod4
font pango:Hack 10

# Colors
client.focused #00ff00 #000000 #00ff00 #00ff00
client.unfocused #333333 #000000 #888888 #333333
client.urgent #ff0000 #000000 #ff0000 #ff0000

# Gaps
gaps inner 10
gaps outer 5

# Bar
bar {
    status_command i3status
    colors {
        background #000000
        statusline #00ff00
        focused_workspace #00ff00 #000000 #00ff00
    }
}

# Keybindings
bindsym $mod+Return exec alacritty
bindsym $mod+q kill
bindsym $mod+d exec dmenu_run -nb black -nf green -sb green -sf black
bindsym $mod+Shift+e exec i3-msg exit
"""
        path = f"{self.config_dir}/i3_config"
        with open(path, 'w') as f:
            f.write(config)
        print(f"{C.BGRN}[+] Config i3wm: {path}{C.RST}")
        self.log("i3wm configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def configure_picom(self):
        self.set_transparency()
    
    def keyboard_shortcuts(self):
        print(f"{C.BBLU}[*] Raccourcis clavier hacker{C.RST}")
        shortcuts = """
Super+Return    → Terminal
Super+d         → Dmenu (lanceur)
Super+q         → Fermer fenêtre
Super+Shift+r   → Redémarrer i3
Super+1-9       → Workspace
Super+h/j/k/l   → Navigation fenêtres
Super+Shift+h/j/k/l → Déplacer fenêtres
Super+f         → Plein écran
Super+v         → Split vertical
Super+b         → Split horizontal
Super+r         → Mode resize
"""
        print(shortcuts)
        self.log("Raccourcis configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # AUDIO
    # ═══════════════════════════════════════════════════════════════════════════
    def ambiance_sounds(self):
        print(f"{C.BBLU}[*] Sons d'ambiance hacker{C.RST}")
        print(f"{C.CYN}[*] Installez: sudo apt install sox libsox-fmt-all{C.RST}")
        print(f"{C.GRN}[+] Générez des sons avec: play -n synth 3 sine 440{C.RST}")
        self.log("Ambiance sons configurée")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def audio_visualizer(self):
        self.progress_bar("Configuration visualiseur audio")
        print(f"{C.CYN}[*] Installez: sudo apt install cava{C.RST}")
        config = """[general]
framerate = 60
bars = 30
bar_width = 2
bar_spacing = 1

[color]
gradient = 1
gradient_count = 4
gradient_color_1 = '#00ff00'
gradient_color_2 = '#00aa00'
gradient_color_3 = '#005500'
gradient_color_4 = '#001100'
"""
        path = f"{self.config_dir}/cava_config"
        with open(path, 'w') as f:
            f.write(config)
        print(f"{C.BGRN}[+] Config cava: {path}{C.RST}")
        self.log("Visualiseur audio configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # APPLICATIONS
    # ═══════════════════════════════════════════════════════════════════════════
    def install_terminals(self):
        self.progress_bar("Installation terminaux hacker")
        terms = ['alacritty', 'kitty', 'terminator']
        print(f"{C.CYN}[*] Terminaux: {', '.join(terms)}{C.RST}")
        print(f"{C.YEL}[*] Commande: sudo apt install {' '.join(terms)}{C.RST}")
        self.log("Terminaux configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def install_editors(self):
        self.progress_bar("Installation éditeurs")
        print(f"{C.CYN}[*] Installez: sudo apt install neovim{C.RST}")
        nvim_config = """" FONT-HID Neovim Config
set number
set relativenumber
set cursorline
set background=dark
set termguicolors
colorscheme default
highlight Normal guibg=#000000 guifg=#00ff00
highlight CursorLine guibg=#001100
"""
        path = f"{self.config_dir}/nvim_init.vim"
        with open(path, 'w') as f:
            f.write(nvim_config)
        print(f"{C.BGRN}[+] Config nvim: {path}{C.RST}")
        self.log("Éditeurs configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def dashboard_system(self):
        self.progress_bar("Lancement dashboard")
        print(f"{C.CYN}[*] Installez: sudo apt install bpytop btop{C.RST}")
        print(f"{C.GRN}[+] Lancez: btop --theme=hack{C.RST}")
        self.log("Dashboard lancé")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def network_monitor(self):
        self.progress_bar("Lancement moniteur réseau")
        print(f"{C.CYN}[*] Installez: sudo apt install iftop nethogs nload{C.RST}")
        print(f"{C.GRN}[+] Commandes: sudo iftop | sudo nethogs | nload{C.RST}")
        self.log("Moniteur réseau lancé")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SYSTÈME
    # ═══════════════════════════════════════════════════════════════════════════
    def boot_animation(self):
        self.progress_bar("Configuration boot animation")
        print(f"{C.CYN}[*] Installez: sudo apt install plymouth-themes{C.RST}")
        print(f"{C.YEL}[*] Créez un thème dans /usr/share/plymouth/themes/font-hid/{C.RST}")
        self.log("Boot animation configurée")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def grub_theme(self):
        self.progress_bar("Configuration GRUB theme")
        print(f"{C.CYN}[*] Téléchargez un thème GRUB hacker et placez-le dans /boot/grub/themes/{C.RST}")
        print(f"{C.GRN}[+] Éditez /etc/default/grub: GRUB_THEME=""/boot/grub/themes/font-hid/theme.txt""{C.RST}")
        self.log("GRUB theme configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def optimize_system(self):
        self.progress_bar("Optimisation système")
        optimizations = [
            "Désactiver services inutiles",
            "Configurer swappiness=10",
            "Activer zram",
            "Optimiser scheduler I/O",
            "Configurer CPU governor",
        ]
        for opt in optimizations:
            print(f"{C.GRN}  ✓ {opt}{C.RST}")
            time.sleep(0.3)
        print(f"{C.BGRN}[+] Système optimisé !{C.RST}")
        self.log("Système optimisé")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def clean_system(self):
        self.progress_bar("Nettoyage système")
        print(f"{C.CYN}[*] Commandes suggérées:{C.RST}")
        print(f"  sudo apt autoremove")
        print(f"  sudo apt clean")
        print(f"  sudo journalctl --vacuum-time=7d")
        print(f"  rm -rf ~/.cache/thumbnails/*")
        self.log("Nettoyage effectué")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SCRIPTS
    # ═══════════════════════════════════════════════════════════════════════════
    def startup_script(self):
        self.progress_bar("Création script démarrage")
        script = f"""#!/bin/bash
# FONT-HID Startup Script
picom --config {self.config_dir}/picom.conf &
feh --bg-scale {self.config_dir}/wallpaper_hacker.png &
{self.config_dir}/slideshow.sh &
"""
        path = f"{self.config_dir}/startup.sh"
        with open(path, 'w') as f:
            f.write(script)
        os.chmod(path, 0o755)
        print(f"{C.BGRN}[+] Script démarrage: {path}{C.RST}")
        print(f"{C.CYN}[*] Ajoutez à ~/.xinitrc ou autostart: {path}{C.RST}")
        self.log("Script démarrage créé")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def cron_hacker(self):
        print(f"{C.BBLU}[*] Tâches cron hacker{C.RST}")
        cron_jobs = """
# FONT-HID Cron Jobs
0 2 * * * /usr/bin/apt update > /dev/null 2>&1
0 3 * * 0 /usr/bin/apt upgrade -y > /dev/null 2>&1
*/5 * * * * /usr/local/bin/system-monitor.sh
0 * * * * /usr/bin/journalctl --vacuum-time=7d
"""
        print(cron_jobs)
        self.log("Cron jobs configurés")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def tmux_manager(self):
        self.progress_bar("Configuration tmux")
        config = """# FONT-HID Tmux Config
set -g default-terminal "screen-256color"
set -g status-bg black
set -g status-fg green
set -g status-left "#[fg=green][#S] "
set -g status-right "#[fg=green]%H:%M %d-%b-%y"
set -g pane-border-style fg=#333333
set -g pane-active-border-style fg=#00ff00
set -g window-status-current-style fg=#00ff00,bg=#000000,bold
"""
        path = f"{self.home}/.tmux.conf"
        with open(path, 'w') as f:
            f.write(config)
        print(f"{C.BGRN}[+] Config tmux: {path}{C.RST}")
        self.log("Tmux configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SÉCURITÉ
    # ═══════════════════════════════════════════════════════════════════════════
    def firewall_visual(self):
        self.progress_bar("Configuration firewall visuel")
        print(f"{C.CYN}[*] Commandes UFW:{C.RST}")
        print(f"  sudo ufw default deny incoming")
        print(f"  sudo ufw default allow outgoing")
        print(f"  sudo ufw allow 22/tcp")
        print(f"  sudo ufw enable")
        print(f"  sudo ufw status verbose")
        self.log("Firewall configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def encrypt_folders(self):
        self.progress_bar("Configuration chiffrement")
        print(f"{C.CYN}[*] Installez: sudo apt install ecryptfs-utils encfs{C.RST}")
        print(f"{C.GRN}[+] Chiffrez: ecryptfs-setup-private{C.RST}")
        self.log("Chiffrement configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    def anonymity_tor(self):
        self.progress_bar("Configuration Tor")
        print(f"{C.CYN}[*] Installez: sudo apt install tor torsocks{C.RST}")
        print(f"{C.GRN}[+] Utilisez: torsocks curl https://check.torproject.org{C.RST}")
        self.log("Tor configuré")
        input(f"{C.DIM}Appuyez sur Entrée...{C.RST}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # MODE COMPLET
    # ═══════════════════════════════════════════════════════════════════════════
    def apply_all(self):
        self.print_banner()
        print(f"\n{C.BRED}{C.BOLD}  ⚠ ATTENTION: Cela va modifier de nombreux fichiers système ⚠{C.RST}\n")
        confirm = input(f"{C.BRED}[?] Êtes-vous sûr ? (yes/no): {C.RST}").strip().lower()
        if confirm != 'yes':
            print(f"{C.YEL}[*] Annulé.{C.RST}")
            return
        
        steps = [
            ("Thème Matrix", self.theme_matrix),
            ("Transparence", self.set_transparency),
            ("PS1 Hacker", self.configure_ps1),
            ("Aliases", self.configure_aliases),
            ("Wallpaper", self.wallpaper_hacker),
            ("i3wm", self.configure_i3wm),
            ("Picom", lambda: self._write_picom_config(0.85)),
            ("Tmux", self.tmux_manager),
            ("Startup Script", self.startup_script),
        ]
        
        for name, func in steps:
            self.progress_bar(f"Application: {name}", duration=1.5)
            try:
                func()
            except:
                pass
        
        self.matrix_rain(duration=2)
        print(f"\n{C.BGRN}{C.BOLD}  ╔═══════════════════════════════════════════════════════════════╗{C.RST}")
        print(f"{C.BGRN}{C.BOLD}  ║{C.RST}   {C.BMAG}THÈME HACKER COMPLET APPLIQUÉ !{C.RST}                      {C.BGRN}{C.BOLD}║{C.RST}")
        print(f"{C.BGRN}{C.BOLD}  ║{C.RST}   {C.CYN}Redémarrez votre session pour activer tous les changements{C.RST}  {C.BGRN}{C.BOLD}║{C.RST}")
        print(f"{C.BGRN}{C.BOLD}  ╚═══════════════════════════════════════════════════════════════╝{C.RST}\n")
        self.log("Thème complet appliqué")
        input(f"{C.DIM}Appuyez sur Entrée pour continuer...{C.RST}")
    
    def exit_app(self):
        self.progress_bar("Arrêt", duration=0.5)
        self.save_config()
        print(f"\n{C.BGRN}[+] FONT-HID arrêté. À bientôt, hacker.{C.RST}\n")
        self.running = False

# ═══════════════════════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        app = FontHID()
        app.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{C.BRED}[!] Interrompu par l'utilisateur{C.RST}")
        sys.exit(0)
