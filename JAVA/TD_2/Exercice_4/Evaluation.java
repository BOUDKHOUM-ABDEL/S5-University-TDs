package TD_2.Exercice_4;

public class Evaluation {
    private double note ;
    private String matiere;

    public Evaluation(double note, String matiere ){
        if(note >=0 & note <=20){
            this.note = note;
            this.matiere = matiere;
        }else{
            System.out.println("note not valid !");
            this.note = 0;
            this.matiere = matiere;
        }
        
    }
    public double getNote() {
        return note;
    }
    public void toSring(){
        System.out.println(this.matiere+" : " + this.note);
    }
}
