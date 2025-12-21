public class TD_1 {
    public static void main(String[] args) {
double score = 92.7;
int intScore = (int) score;
int category = intScore / 10;
char grade;
switch (category) {
    case 10:
    case 9 :
        grade = 'A';
        break;
    case 8:
        grade = 'B';
        break;
    case 7:
        grade = 'C';
        break;
    case 6:
        grade = 'D';
        break;
    default:
        grade = 'F';
        break;
}
System.out.println("La note est : " + grade);
    }
}
// Un jeu vidéo stocke le score du joueur dans un double. On veut convertir ce score en une 
// note (char) basée sur des paliers entiers.
// • Déclarez double score = 84.7;
// • Convertissez ce score en int (ce qui va le tronquer, c'est voulu).
// • Divisez cet int par 10 pour obtenir une "catégorie" (un int de 0 à 10).
// • Utilisez un switch sur cette catégorie pour affecter une note à une variable char 
// grade ainsi:
// ◦ 10 et 9 : 'A'
// ◦ 8 : 'B'
// ◦ 7 : 'C'
// ◦ 6 : 'D'
// ◦ Autre (default) : 'F'
// • Affichez la note (grade).