package algoritmos;
import java.util.Scanner;
public class Algoritmo2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el número de filas (n): ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consumir el salto de línea restante

        System.out.print("Ingrese el mensaje: ");
        String mensaje = scanner.nextLine().replaceAll("\\s+", ""); // Eliminar espacios en blanco

        if (mensaje.length() > n * n) {
            System.out.println("El mensaje es demasiado largo para la matriz de cifrado.");
            return;
        }

        char[][] matrizCifrado = new char[n][n];

        // Llenar la matriz de cifrado con el mensaje de forma recursiva
        llenarMatrizCifrado(matrizCifrado, mensaje, 0, 0);

        // Imprimir la matriz de cifrado
        System.out.println("Matriz de cifrado:");
        imprimirMatriz(matrizCifrado);

        // Imprimir el mensaje original
        System.out.println("Mensaje original: " + mensaje);

        // Imprimir el mensaje cifrado
        String mensajeCifrado = generarMensajeCifrado(matrizCifrado, n);
        System.out.println("Mensaje cifrado: " + mensajeCifrado);
    }

    private static void llenarMatrizCifrado(char[][] matrizCifrado, String mensaje, int fila, int columna) {
        if (columna == matrizCifrado[0].length) {
            fila++;
            columna = 0;
        }

        if (fila == matrizCifrado.length || mensaje.isEmpty()) {
            // Llenar los espacios restantes con '*'
            llenarConCaracter(matrizCifrado, fila, columna, '*');
            return;
        }

        matrizCifrado[fila][columna] = mensaje.charAt(0);
        llenarMatrizCifrado(matrizCifrado, mensaje.substring(1), fila, columna + 1);
    }

    private static String generarMensajeCifrado(char[][] matrizCifrado, int n) {
        StringBuilder mensajeCifrado = new StringBuilder();
        for (int columna = 0; columna < n; columna++) {
            for (int fila = 0; fila < n; fila++) {
                if (matrizCifrado[fila][columna] != '*') {
                    mensajeCifrado.append(matrizCifrado[fila][columna]);
                }
            }
        }
        return mensajeCifrado.toString();
    }

    private static void imprimirMatriz(char[][] matriz) {
        for (char[] fila : matriz) {
            for (char elemento : fila) {
                System.out.print(elemento + " ");
            }
            System.out.println();
        }
    }

    private static void llenarConCaracter(char[][] matriz, int filaInicio, int columnaInicio, char caracter) {
        for (int fila = filaInicio; fila < matriz.length; fila++) {
            for (int columna = (fila == filaInicio) ? columnaInicio : 0; columna < matriz[0].length; columna++) {
                matriz[fila][columna] = caracter;
            }
        }
    }

}
