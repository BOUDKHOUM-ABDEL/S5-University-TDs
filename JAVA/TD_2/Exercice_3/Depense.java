package TD_2.Exercice_3;


public class Depense {
    private double montant;
    private String description;

    public Depense(double montant, String description) {
        this.montant = montant;
        this.description = description;
    }

    public double getMontant() {
        return montant;
    }

    @Override
    public String toString() {
        return description + " : " + montant + " MAD";
    }
}
