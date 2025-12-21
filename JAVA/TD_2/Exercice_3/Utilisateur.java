package TD_2.Exercice_3;

public class Utilisateur {
    private String nom;
    private double solde;
    private Depense[] depenses;
    private int nbDepenses;

    public Utilisateur(String nom, double solde) {
        this.nom = nom;
        this.solde = solde;
        this.depenses = new Depense[10];
        this.nbDepenses = 0;
    }

    public void ajouterDepense(double montant, String description) {
        if (montant <= solde && nbDepenses < depenses.length) {
            depenses[nbDepenses] = new Depense(montant, description);
            nbDepenses++;
            solde -= montant;
        } else {
            System.out.println("Impossible d'ajouter la dépense.");
        }
    }

    public void afficherDepenses() {
        System.out.println("Liste des dépenses :");
        for (int i = 0; i < nbDepenses; i++) {
            System.out.println(depenses[i]);
        }
    }

    public double calculerDepenses(int n) {
        if (n == 0) return 0;
        return depenses[n - 1].getMontant() + calculerDepenses(n - 1);
    }

    public void afficherProfil() {
        System.out.println("Nom : " + nom);
        System.out.println("Solde : " + solde + " MAD");
        System.out.println("Nombre de dépenses : " + nbDepenses);
    }

    public int getNbDepenses() {
        return nbDepenses;
    }
}
