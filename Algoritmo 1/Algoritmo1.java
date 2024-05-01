package algoritmos;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Algoritmo1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese una palabra: ");
        String palabra = scanner.nextLine();

        ArrayList<String> permutaciones = permutarPalabra(palabra);
        Collections.sort(permutaciones);

        System.out.println("Número total de permutaciones: " + permutaciones.size());
        System.out.println("Las 10 primeras permutaciones ordenadas alfabéticamente:");

        for (int i = 0; i < 10 && i < permutaciones.size(); i++) {
            System.out.println(permutaciones.get(i));
        }
    }

    public static ArrayList<String> permutarPalabra(String palabra) {
        ArrayList<String> permutaciones = new ArrayList<>();
        permutarRecursivo("", palabra, permutaciones);
        return permutaciones;
    }

    private static void permutarRecursivo(String prefijo, String palabra, ArrayList<String> permutaciones) {
        if (palabra.length() == 0) {
            permutaciones.add(prefijo);
        } else {
            for (int i = 0; i < palabra.length(); i++) {
                permutarRecursivo(prefijo + palabra.charAt(i), palabra.substring(0, i) + palabra.substring(i + 1), permutaciones);
            }
        }
    }
}
