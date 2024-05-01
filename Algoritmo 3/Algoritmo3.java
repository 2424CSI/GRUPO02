package Proyecto1;



//3. Algoritmo que realice el cifrado de un mensaje por permutación de columnas, 
//teniendo como clave n columnas. Tanto n como el texto del mensaje se ingresan 
//al iniciar el algoritmo. El algoritmo debe controlar que el número de caracteres 
//del mensaje (sin espacios), sea menor o igual que n x n. Imprima la matriz de cifrado, 
//el mensaje original y el mensaje cifrado.  Si en la matriz de cifrado sobran espacios 
//para almacenar los caracteres del mensaje original, estos deben llenarse con "*".
class Ejercicio {
  public static void main(String[] args) {
        
        String mensaje = "holamundo";
        int n = 5;

        if (mensaje.length() > n * n) {
            System.out.println("El número de caracteres del mensaje (sin espacios) debe ser menor o igual que n x n.");
            return;
        }

        char[][] matriz = new char[n][n];
        int index = 0;

        // Llenar la matriz con el mensaje
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (index < mensaje.length()) {
                    matriz[i][j] = mensaje.charAt(index);
                    index++;
                } else {
                    matriz[i][j] = '*';
                }
            }
        }

        // Imprimir la matriz de cifrado
        System.out.println("Matriz de cifrado:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        // Imprimir el mensaje original
        System.out.println("Mensaje original: " + mensaje);

        // Imprimir el mensaje cifrado
        System.out.print("Mensaje cifrado: ");
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                System.out.print(matriz[i][j]);
            }
        }
    }
 
}