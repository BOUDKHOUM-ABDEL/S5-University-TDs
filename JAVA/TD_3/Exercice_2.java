package JAVA.TD_3;

import java.util.Scanner;

public class Exercice_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Veuillez saisir une phrase :");
        String phrase = scanner.nextLine();
        
        String motRecherche = "java";
        int count = 0;
        
        // On convertit tout en minuscules pour ne pas tenir compte de la casse
        String phraseLower = phrase.toLowerCase();
        
        // On peut utiliser split pour compter les mots exacts "java", ou bien compter les sous-chaînes
        // L'énoncé dit "occurrences d'un mot", donc on va séparer par les espaces ou la ponctuation
        String[] mots = phraseLower.split("\\W+");
        for (String mot : mots) {
            if (mot.equals(motRecherche)) {
                count++;
            }
        }
        
        System.out.println("Le mot '" + motRecherche + "' apparait " + count + " fois.");
        scanner.close();
    }
}
