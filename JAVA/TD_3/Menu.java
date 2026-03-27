package JAVA.TD_3;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Etudiant etudiant = null;
        int choix;

        do {
            System.out.println("\n===== MENU ETUDIANT =====");
            System.out.println("1. Creer un etudiant");
            System.out.println("2. Saisir ses notes");
            System.out.println("3. Afficher ses resultats");
            System.out.println("4. Verifier son admission (seuil 10)");
            System.out.println("5. Quitter");
            System.out.print("Choix : ");
            
            // Check if there is an integer to consume
            if (!scanner.hasNextInt()) {
                System.out.println("Entree invalide, veuillez reessayer.");
                scanner.next(); // consume invalid input
                choix = -1;
                continue;
            }
            choix = scanner.nextInt();
            scanner.nextLine();

            switch (choix) {
                case 1:
                    System.out.print("Nom : ");
                    String nom = scanner.nextLine();
                    System.out.print("Prenom : ");
                    String prenom = scanner.nextLine();
                    System.out.print("Nombre maximum de notes : ");
                    int maxNotes = scanner.nextInt();
                    etudiant = new Etudiant(nom, prenom, maxNotes);
                    System.out.println("Etudiant cree avec succes !");
                    break;
                case 2:
                    if (etudiant == null) {
                        System.out.println("Veuillez d'abord creer un etudiant.");
                    } else {
                        System.out.print("Saisir la note : ");
                        double note = scanner.nextDouble();
                        etudiant.ajouterNote(note);
                    }
                    break;
                case 3:
                    if (etudiant == null) {
                        System.out.println("Veuillez d'abord creer un etudiant.");
                    } else {
                        etudiant.afficherInfos();
                        System.out.println("Note la plus elevee : " + etudiant.noteMax());
                        etudiant.afficherNotesTriees();
                    }
                    break;
                case 4:
                    if (etudiant == null) {
                        System.out.println("Veuillez d'abord creer un etudiant.");
                    } else {
                        if (etudiant.estAdmis(10)) {
                            System.out.println("L'etudiant est admis.");
                        } else {
                            System.out.println("L'etudiant n'est pas admis.");
                        }
                    }
                    break;
                case 5:
                    System.out.println("Au revoir !");
                    break;
                default:
                    System.out.println("Choix invalide.");
            }
        } while (choix != 5);
        
        scanner.close();
    }
}
