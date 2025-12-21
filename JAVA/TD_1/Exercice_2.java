package TD_1;

public class Exercice_2 {
    public static void main(String[] args) {
double score = 84.7;
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
