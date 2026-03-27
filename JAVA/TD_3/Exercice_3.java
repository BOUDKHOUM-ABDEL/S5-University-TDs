package JAVA.TD_3;

import java.util.Scanner;

public class Exercice_3 {
    
    public static boolean estAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z') ||
               (c >= 'a' && c <= 'z') ||
               (c >= '0' && c <= '9');
    }

    public static String extraireEmail(String texte) {
        int indexArobase = texte.indexOf('@');
        
        if (indexArobase == -1) {
            return null; // Pas d'email trouvé
        }
        
        // Trouver le début de l'email (mot alphanumérique avant @)
        int debut = indexArobase - 1;
        while (debut >= 0 && estAlphaNum(texte.charAt(debut))) {
            debut--;
        }
        debut++; // On revient sur le premier caractère valide
        
        // Trouver la fin de l'email (mot alphanumérique après @)
        int fin = indexArobase + 1;
        while (fin < texte.length() && (estAlphaNum(texte.charAt(fin)) || texte.charAt(fin) == '.')) { 
            // NOTE: Normalement un domaine contient des points. L'énoncé dit alphanumérique, 
            // mais on va inclure le point pour un format correct si nécessaire,
            // ou bien rester strict à alphanumérique comme demandé.
            // L'énoncé: "(espace) + (mot alphanumérique) + @ + (mot alphanumérique) + (espace)"
            fin++;
        }
        
        if (debut < indexArobase && fin > indexArobase + 1) {
            return texte.substring(debut, fin);
        }
        
        return null; // Format non respecté
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Veuillez saisir une phrase contenant des emails :");
        String phrase = scanner.nextLine();
        
        String email = extraireEmail(phrase);
        if (email != null) {
            System.out.println("Email extrait : " + email);
        } else {
            System.out.println("Aucun email valide n'a ete trouve.");
        }
        scanner.close();
    }
}
