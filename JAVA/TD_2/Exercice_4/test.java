package TD_2.Exercice_4;

public class test {
    public static void main(String[] args) {
        // Premier étudiant avec 3 notes
        Etudiant e1 = new Etudiant("Omar El Idrissi", 123456);
        e1.ajouterNote(15, "Mathématiques");
        e1.ajouterNote(13, "Physique");
        e1.ajouterNote(17, "Informatique");
        e1.afficherNotes();
        System.out.println("Moyenne : " + e1.CalculerMoyenne());
        System.out.println(e1);
        System.out.println("-----------------------------");

        // Deuxième étudiant avec 5 notes (cas limite)
        Etudiant e2 = new Etudiant("Salma Benali", 654321);
        e2.ajouterNote(10, "Anglais");
        e2.ajouterNote(12, "Histoire");
        e2.ajouterNote(14, "Biologie");
        e2.ajouterNote(16, "Chimie");
        e2.ajouterNote(18, "Mathématiques");
        e2.afficherNotes();
        System.out.println("Moyenne : " + e2.CalculerMoyenne());
        System.out.println(e2);
        System.out.println("-----------------------------");

        // Troisième étudiant avec seulement 1 note
        Etudiant e3 = new Etudiant("Youssef Amrani", 789012);
        e3.ajouterNote(20, "Philosophie");
        e3.afficherNotes();
        System.out.println("Moyenne : " + e3.CalculerMoyenne());
        System.out.println(e3);
        System.out.println("-----------------------------");

        // Quatrième étudiant : test d'ajout de plus de 5 notes
        Etudiant e4 = new Etudiant("Fatima Zahra", 345678);
        e4.ajouterNote(11, "Math");
        e4.ajouterNote(12, "Physique");
        e4.ajouterNote(13, "SVT");
        e4.ajouterNote(14, "Français");
        e4.ajouterNote(15, "Anglais");
        e4.ajouterNote(16, "Informatique"); // devrait afficher un message d'erreur
        e4.afficherNotes();
        System.out.println("Moyenne : " + e4.CalculerMoyenne());
        System.out.println(e4);
        System.out.println("___________Results_______________");
        System.out.println(e1.toString());
        System.out.println(e2.toString());
        System.out.println(e3.toString());
    }
}
