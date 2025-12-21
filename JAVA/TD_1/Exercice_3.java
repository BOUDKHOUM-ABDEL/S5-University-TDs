package TD_1;

public class Exercice_3 {
    public static void main(String[] args) {
       int n = 5; // Déclarer la constante n
       int factorial = 1;
        for (int i = 1; i <= n; i++) {
              factorial *= i; // Calculer la factorielle
        }
        System.out.println("La factorielle de " + n + " est : " + factorial);
        }
    
}
// Exercice 3 : 
// Écrire un programme qui calcule la factorielle d’un entier n (déclaré constante au début 
// du programme). 
// Rappel : La factorielle d'un nombre entier n est le produit (la multiplication) de tous les 
// entiers positifs de 1 jusqu'à n.