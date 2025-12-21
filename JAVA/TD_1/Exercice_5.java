package TD_1;
public class Exercice_5 {
    public static void main(String[] args) {
        int min = Integer.parseInt(args[0]);
        int max = Integer.parseInt(args[1]);

        for (int n = min; n <= max; n++) {
            if (estPremier(n)) {
                System.out.println(n + " est premier");
            }
        }
    }

    static boolean estPremier(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

// Affiche tous les nombres premiers entre min et max, données en arguments du 
// main(String args[]) .
// Rappel : Un nombre premier est un entier supérieur à 1 qui n'a aucun diviseur à part 1 et 
// lui-même.
// • Exemples : 2, 3, 5, 7, 11 sont premiers.
// • Contre-exemples : 4 (divisible par 2), 9 (divisible par 3), 1 (cas spécial), 0 (cas 
// spécial)