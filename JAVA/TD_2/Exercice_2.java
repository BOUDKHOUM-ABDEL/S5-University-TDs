package TD_2;

public class Exercice_2 {
    class TableCarres{
       private static int[] carres;

       static {
        carres = new int[10]; // tableau de taille 10
        for (int i = 0; i < carres.length; i++) {
            carres[i] = i * i; // remplir avec les carrés
        }
        System.out.println("Bloc static exécuté : tableau initialisé !");
    }
        public static void afficher() {
        for (int val : carres) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
        

    }
    
    public static void main(String[] args) {
            
            TableCarres.afficher();
        } 
}
    
    


// Exercice 2 :
// // On un bloc d’initialisation statique permettant d’allouer le tableau et de le remplir avec les 
// carrés des nombres de 0 à 9 ;
// une méthode statique afficher() qui affiche le contenu du tableau sur une même ligne.
// Créez une classe TestTableCarres contenant la méthode main.
// Depuis cette méthode : Appelez TableCarres.afficher() pour afficher les valeurs du 
// tableau. 
// Résultat : 
// Bloc static exécuté : tableau initialisé !
// 0 1 4 9 16 25 36 49 64 81 but statique int[] carres ;