package JAVA.TD_3;

import java.util.Arrays;

public class AnalyseTableau {

    public static int frequenceValeur(int[] t, int v) {
        int count = 0;
        for (int i : t) {
            if (i == v) {
                count++;
            }
        }
        return count;
    }

    public static boolean estSymetrique(int[] t) {
        int left = 0;
        int right = t.length - 1;
        while (left < right) {
            if (t[left] != t[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static int[] extraireSousTableau(int[] t, int debut, int fin) {
        if (debut < 0 || fin >= t.length || debut > fin) {
            System.err.println("Erreur: indices invalides.");
            return new int[0];
        }
        int[] sub = new int[fin - debut + 1];
        System.arraycopy(t, debut, sub, 0, sub.length);
        return sub;
    }

    public static int[] sommePairsImpairs(int[] t) {
        int sommePairs = 0;
        int sommeImpairs = 0;
        for (int j : t) {
            if (j % 2 == 0) {
                sommePairs += j;
            } else {
                sommeImpairs += j;
            }
        }
        return new int[]{sommePairs, sommeImpairs};
    }

    public static int[] fusionEtTri(int[] t1, int[] t2) {
        // Concatenation
        int[] t3 = new int[t1.length + t2.length];
        System.arraycopy(t1, 0, t3, 0, t1.length);
        System.arraycopy(t2, 0, t3, t1.length, t2.length);
        
        // Tri par Selection
        for (int i = 0; i < t3.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < t3.length; j++) {
                if (t3[j] < t3[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = t3[minIndex];
            t3[minIndex] = t3[i];
            t3[i] = temp;
        }

        // Suppression des doublons
        if (t3.length == 0) return t3;
        int[] tempArr = new int[t3.length];
        int j = 0;
        for (int i = 0; i < t3.length - 1; i++) {
            if (t3[i] != t3[i + 1]) {
                tempArr[j++] = t3[i];
            }
        }
        tempArr[j++] = t3[t3.length - 1];
        
        int[] result = new int[j];
        System.arraycopy(tempArr, 0, result, 0, j);
        return result;
    }

    public static boolean estPermutation(int[] t1, int[] t2) {
        if (t1.length != t2.length) return false;
        
        int[] sortedT1 = Arrays.copyOf(t1, t1.length);
        int[] sortedT2 = Arrays.copyOf(t2, t2.length);
        Arrays.sort(sortedT1);
        Arrays.sort(sortedT2);
        
        return Arrays.equals(sortedT1, sortedT2);
    }
}
