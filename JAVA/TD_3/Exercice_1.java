package TD_3;

public class Exercice_1 {

    // Méthode pour nettoyer et formater le nom complet
    public static String nettoyerNom(String saisie) {
        // 1. Supprimer les espaces au début et à la fin
        String texte = saisie.trim();

        // 2. Remplacer les "-" par des espaces
        texte = texte.replace("-", " ");

        // 3. Séparer nom et prénom (en supposant qu'il y a un espace entre les deux)
        String[] parties = texte.split("\\s+"); // découpe par un ou plusieurs espaces

        if (parties.length < 2) {
            return "Format invalide (nom et prénom requis)";
        }

        String nom = parties[0].toUpperCase(); // nom en majuscule
        String prenom = parties[1].substring(0, 1).toUpperCase() + 
                        parties[1].substring(1).toLowerCase(); // première lettre majuscule

        return nom + " " + prenom;
    }
    // Programme principal pour tester
    public static void main(String[] args) {
        String saisie = "    En-Nassiri ahmed  ";
        String resultat = nettoyerNom(saisie);
        System.out.println("Avant nettoyage : \"" + saisie + "\"");
        System.out.println("Après nettoyage : \"" + resultat + "\"");
    }
}

// Exercice 1 : Nettoyer un formulaire utilisateur
//  Un utilisateur saisit son nomet prenom avec des espaces ou des caractères 
// inutiles, par exemple «    En-Nassiri ahmed  ». Pour uniformiser les noms, écrire un 
// programme qui :
// •nettoie la chaîne des espaces au début et fin.
// •met le nom en majuscule
// •met la première lettre du prénom en majuscule et le reste en minuscule
// •remplace les - par des espaces