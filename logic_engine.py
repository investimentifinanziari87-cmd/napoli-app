# logic_engine.py
"""
MODULO LOGIC ENGINE: Generatore del Super Report Narrativo.
Versione: 3.0
"""
class AdvancedAnalysisEngine:

    @staticmethod
    def analyze_coach_strategy(stats):
        # Calcoli matematici
        ppda = round(stats.get('opp_passes', 400) / max(stats.get('def_actions', 50), 1), 2)
        
        att_left = stats.get('att_left', 33)
        att_center = stats.get('att_center', 34)
        att_right = stats.get('att_right', 33)
        tot_att = max(att_left + att_center + att_right, 1)
        asym_l = round((att_left / tot_att) * 100)
        asym_c = round((att_center / tot_att) * 100)
        asym_r = round((att_right / tot_att) * 100)
        
        idt = round((stats.get('passes_final_third', 100) / max(stats.get('total_passes', 500), 1)) * 100, 1)

        # GENERAZIONE SUPER REPORT (Testo Lungo per l'Allenatore)
        fase_possesso = (
            f"FASE DI POSSESSO:\nIl Napoli ha sviluppato il gioco mantenendo un Indice di Dominio Territoriale (IDT) del {idt}%. "
            f"La costruzione ha privilegiato chiaramente {'la fascia sinistra' if asym_l > 40 else 'le vie centrali' if asym_c > 40 else 'la catena di destra' if asym_r > 40 else 'uno sviluppo equilibrato su tutto il fronte'}, "
            f"cercando di scardinare le linee avversarie tramite un fitto possesso palla. "
            "Il Mister ha chiesto ai braccetti difensivi di alzarsi per creare superiorità numerica a centrocampo, favorendo le verticalizzazioni improvvise."
        )

        fase_non_possesso = (
            f"FASE DI NON POSSESSO:\nLa squadra ha registrato un PPDA di {ppda}. "
            f"{'Pressing feroce e baricentro altissimo, asfissiando le fonti di gioco avversarie fin dalla loro area di rigore.' if ppda < 10 else 'Atteggiamento tattico più attendista e difesa posizionale, preferendo chiudere ermeticamente le linee di passaggio piuttosto che aggredire freneticamente il portatore.'} "
            "Le transizioni difensive sono state gestite con repentine riaggressioni subito dopo aver perso il pallone."
        )

        chiave_tattica = (
            "CHIAVE TATTICA DEL MATCH:\nLa partita si è decisa a centrocampo, dove l'intensità nei duelli ha permesso al Napoli di "
            "indirizzare i ritmi di gioco. Determinante la lettura del Mister nelle marcature preventive."
        )

        return {
            "ppda": ppda,
            "asymmetry": f"Sx {asym_l}% | Cen {asym_c}% | Dx {asym_r}%",
            "idt": idt,
            "report_possesso": fase_possesso,
            "report_non_possesso": fase_non_possesso,
            "chiave_tattica": chiave_tattica
        }

    @staticmethod
    def analyze_player_advanced(name, stats):
        prog_passes = stats.get('prog_passes', 0)
        passes_box = stats.get('passes_box', 0)
        dribbles = stats.get('dribbles', 0)

        xt = round((prog_passes * 0.05) + (passes_box * 0.15) + (dribbles * 0.08), 2)
        lba = prog_passes + dribbles

        # GENERAZIONE TESTO LUNGO (Per ogni Giocatore)
        if xt >= 1.2 and lba >= 10:
            profile = "Catalizzatore Offensivo: rompe costantemente le linee e crea minacce ad altissimo coefficiente. È stato il faro della manovra avanzata, capace di saltare sistematicamente l'uomo e creare superiorità numerica disorientando la difesa."
        elif xt < 1.2 and lba >= 10:
            profile = "Regista di Costruzione: ottime rotture di linea, ma le sue giocate avvengono lontane dalla zona calda. Ha dettato i tempi con maestria eludendo il primo pressing avversario, gestendo i ritmi come un metronomo."
        elif xt >= 1.2 and lba < 10:
            profile = "Rifinitore Puro: pochi tocchi sul pallone, ma converte il possesso in minaccia letale per la porta avversaria. Cinico negli ultimi 16 metri, sfrutta ogni centimetro di spazio concesso dai difensori."
        else:
            profile = "Equilibratore: possesso conservativo, molto utile per la gestione. Grande lavoro oscuro in fase di copertura e raddoppio, garantendo solidità al reparto e proteggendo la linea difensiva dalle ripartenze."

        return {
            "name": name,
            "xt": xt,
            "lba": lba,
            "profile": profile
        }