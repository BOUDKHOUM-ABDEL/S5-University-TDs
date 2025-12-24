package TD_2.Exercice_4;

public class Etudiant {
    private String nom;
    private int codeApogee;
    private Evaluation[] evaluations; 
    private int nbEvaluations;

    public Etudiant(String nom, int codeApogee){
        this.nom = nom;
        this.codeApogee = codeApogee;
        this.evaluations = new Evaluation[5];
        nbEvaluations = 0;
    }
    public void ajouterNote(double note){
        ajouterNote(note , "Unkown");
    }

    public void ajouterNote(double note, String matiere){
    if(nbEvaluations <=5){
        if(note >=0 && note <=20){
            evaluations[nbEvaluations] = new Evaluation(note, matiere);
            nbEvaluations++;
        }else{
            System.out.println("note not valid !");
    }
    }else System.out.println("Impossible d'ajouter plus de 5 notes.");
    }

    public void afficherNotes() { 
        System.out.println("Notes de " + nom + " :");
        for (int i = 0; i < nbEvaluations; i++) {
            System.out.println(evaluations[i].getNote()); 
        }
    }

    public double CalculerMoyenne(){
        if(evaluations.length==0){
            System.out.println(" pas de notes");
            return 0 ;
        }
        double  Somme = 0;
        for (int i = 0; i < nbEvaluations; i++) {
            Somme+=evaluations[i].getNote(); 
        }
        return Somme/nbEvaluations;
    }
    public String toString(){
        return this.nom +" : "+ this.codeApogee +" , "+ this.nbEvaluations;
    }
}
