package TD_2;

public class Exercice_1 {

    public static void main(String[] args) {
    class CompteBancaire{
        private String nmCompte ;
        private String Titulaire ;
        private double Solde ;

        public CompteBancaire(){
            this.nmCompte = "0000";
            this.Titulaire = "Inconnu";
            this.Solde = 0.0;
        }
        public CompteBancaire(String numero ,String nom ){
            this(numero, nom , 0.0);
            
        }
         public CompteBancaire(String numero ,String nom , double solde ){
            this.nmCompte = numero;
            this.Titulaire =nom;
            this.Solde = 0.0;
        }
        public void deposer(double montant)  {
            if (montant >= 0) {
                this.Solde += montant ;
            System.out.println(this.Titulaire + " a depose(e) : " + montant + " DH"); }
            else System.out.println("Invalid montant .");   
        }
        public void retirer(double montant) {
            if (montant <= this.Solde) {
                this.Solde -= montant ;
                System.out.println(this.Titulaire + " a retire(e) : " + montant + " DH"); }
            else System.out.println("Solde insuffisant !"); 
        }
        public void afficher() {
        System.out.println("Numéro : " + this.nmCompte +
                           ", Nom : " + this.Titulaire +
                           ", Solde : " + this.Solde + " DH");
    }
    }
        CompteBancaire c1 = new CompteBancaire(); // par défaut
        CompteBancaire c2 = new CompteBancaire("1234", "Ali"); // 2 paramètres
        CompteBancaire c3 = new CompteBancaire("5678", "Sara", 500.0); // 3 paramètres

        c1.deposer(200);
        c2.deposer(100);
        c3.retirer(50);

        c1.afficher();
        c2.afficher();
        c3.afficher();  
    }
}
