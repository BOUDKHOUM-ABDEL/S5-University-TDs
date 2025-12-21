package TD_2.Exercice_3;

public class Test {
    public static void main(String[] args) {
        Utilisateur u = new Utilisateur("Salma", 1000.0);

        u.afficherProfil();

        u.ajouterDepense(150.0, "Transport");
        u.ajouterDepense(200.0, "Courses");
        u.ajouterDepense(100.0, "Livres");

        u.afficherDepenses();

        System.out.println("Total des dépenses : " + u.calculerDepenses(u.getNbDepenses()) + " MAD");

        u.afficherProfil();
    }
}
