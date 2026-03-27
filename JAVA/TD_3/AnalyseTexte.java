package JAVA.TD_3;

import java.util.Arrays;

public class AnalyseTexte {

    public static String nettoyerTexte(String texte) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < texte.length(); i++) {
            char c = texte.charAt(i);
            if (Character.isLetterOrDigit(c) || Character.isWhitespace(c)) {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public static String motLePlusLong(String phrase) {
        String cleaned = nettoyerTexte(phrase);
        String[] mots = cleaned.split("\\s+");
        String longMot = "";
        for (String m : mots) {
            if (m.length() > longMot.length()) {
                longMot = m;
            }
        }
        return longMot;
    }

    public static int compterMots(String phrase) {
        if (phrase == null || phrase.trim().isEmpty()) {
            return 0;
        }
        return phrase.trim().split("\\s+").length;
    }

    public static String remplacerVoyelles(String phrase, char remplacant) {
        return phrase.replaceAll("[AEIOUYaeiouy]", String.valueOf(remplacant));
    }

    public static String inverserPhrase(String phrase) {
        String[] mots = phrase.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = mots.length - 1; i >= 0; i--) {
            sb.append(mots[i]).append(" ");
        }
        return sb.toString().trim();
    }

    public static boolean estAnagramme(String mot1, String mot2) {
        String m1 = mot1.replaceAll("\\s+", "").toLowerCase();
        String m2 = mot2.replaceAll("\\s+", "").toLowerCase();
        if (m1.length() != m2.length()) return false;
        
        char[] array1 = m1.toCharArray();
        char[] array2 = m2.toCharArray();
        Arrays.sort(array1);
        Arrays.sort(array2);
        
        return Arrays.equals(array1, array2);
    }
}
