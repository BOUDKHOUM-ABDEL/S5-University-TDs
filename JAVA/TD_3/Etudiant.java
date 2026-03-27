package JAVA.TD_3;

import java.util.Arrays;

public class Etudiant {
    private String nom;
    private String prenom;
    private double[] notes;
    private int nbNotes;

    public Etudiant(String nom, String prenom, int maxNotes) {
        this.nom = nom;
        this.prenom = prenom;
        this.notes = new double[maxNotes];
        this.nbNotes = 0;
    }

    public double moyenne() {
        if (nbNotes == 0) return 0.0;
        double sum = 0;
        for (int i = 0; i < nbNotes; i++) {
            sum += notes[i];
        }
        return sum / nbNotes;
    }

    public double noteMax() {
        if (nbNotes == 0) return 0.0;
        double max = notes[0];
        for (int i = 1; i < nbNotes; i++) {
            if (notes[i] > max) {
                max = notes[i];
            }
        }
        return max;
    }

    public boolean estAdmis(double seuil) {
        return moyenne() >= seuil;
    }

    public void ajouterNote(double note) {
        if (nbNotes < notes.length) {
            notes[nbNotes++] = note;
        } else {
            System.out.println("Le tableau de notes est plein !");
        }
    }

    public void afficherInfos() {
        System.out.println("Informations de l'etudiant :");
        System.out.println("Nom : " + nom);
        System.out.println("Prenom : " + prenom);
        System.out.println("Moyenne : " + moyenne());
        System.out.println("Admission (seuil 10) : " + (estAdmis(10) ? "Oui" : "Non"));
    }

    public void afficherNotesTriees() {
        if (nbNotes == 0) {
            System.out.println("Aucune note a afficher.");
            return;
        }
        double[] notesValides = Arrays.copyOf(notes, nbNotes);
        Arrays.sort(notesValides);
        System.out.print("Notes triees : ");
        for (double n : notesValides) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
