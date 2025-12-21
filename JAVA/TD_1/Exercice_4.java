package TD_1;

public class Exercice_4 {
    public static void main(String[] args) {
       int n = 6; // Déclarer la constante n
       int sumOfDivisors = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sumOfDivisors += i; // Ajouter le diviseur à la somme
            }
        }
        if (sumOfDivisors == n) {
            System.out.println(n + " est un nombre parfait.");
        } else {
            System.out.println(n + " n'est pas un nombre parfait.");
        }
    }
}
// Écrire un programme qui teste si le nombre n est parfait.
// Rappel : Un nombre est parfait s’il est égal à la somme de ses diviseurs (hors lui-même).
// Exemple : 6 = 1 + 2 + 3