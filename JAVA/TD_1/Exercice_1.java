package JAVA.TD_1;

public class Exercice_1 {
    public static void main(String[] args) {
        // 1.
        int a = 10;
        double b = 5.5;
        double resultat1 = a + b; // int + double = double
        
        // 2.
        byte b1 = 10;
        byte b2 = 20;
        int resultat2 = b1 + b2; // byte + byte is promoted to int in Java
        
        // 3.
        String s = "100";
        int i = 50;
        String resultat3 = s + i; // String + int = String (concatenation)
        
        // 4.
        char c = 'A'; // 'A' a la valeur 65
        int j = 1;
        int resultat4 = c + j; // char + int is promoted to int in Java
        
        System.out.println("Resultat 1 (double): " + resultat1);
        System.out.println("Resultat 2 (int): " + resultat2);
        System.out.println("Resultat 3 (String): " + resultat3);
        System.out.println("Resultat 4 (int): " + resultat4);
    }
}
