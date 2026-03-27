package JAVA.TD_3;

import java.util.Scanner;

public class Exercice_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Veuillez saisir le nom et prenom :");
        String saisie = scanner.nextLine();
        
        // Nettoyer les espaces au début et à la fin
        saisie = saisie.trim();
        
        // Remplacer les '-' par des espaces
        saisie = saisie.replace("-", " ");
        
        // On suppose que le dernier mot est le prénom et le reste est le nom
        // Ou bien, on peut traiter chaque mot. "En-Nassiri ahmed" -> "EN NASSIRI" "Ahmed"
        // Le plus simple c'est de séparer selon l'espace et de supposer que le dernier mot est le prénom
        String[] mots = saisie.split("\\s+");
        if (mots.length >= 2) {
            String prenom = mots[mots.length - 1];
            StringBuilder nomBuilder = new StringBuilder();
            
            for (int i = 0; i < mots.length - 1; i++) {
                nomBuilder.append(mots[i].toUpperCase()).append(" ");
            }
            String nom = nomBuilder.toString().trim();
            
            // Format prenom
            String prenomFormatte = prenom.substring(0, 1).toUpperCase() + prenom.substring(1).toLowerCase();
            
            System.out.println("Resultat : " + nom + " " + prenomFormatte);
        } else if (mots.length == 1) {
            System.out.println("Resultat : " + mots[0].toUpperCase());
        }
        
        scanner.close();
    }
}
