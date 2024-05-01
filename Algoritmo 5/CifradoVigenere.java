
public class CifradoVigenere {

    public static String cifrarVigenere(String mensaje, String clave) {
        StringBuilder mensajeCifrado = new StringBuilder();
        String alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        clave = clave.toUpperCase();
        int claveIndex = 0;

        for (char caracter : mensaje.toCharArray()) {
            if (Character.isLetter(caracter)) {
                char caracterUpper = Character.toUpperCase(caracter);
                int fila = alfabeto.indexOf(caracterUpper);
                int columna = alfabeto.indexOf(clave.charAt(claveIndex));

                char caracterCifrado = alfabeto.charAt((fila + columna) % 26);
                mensajeCifrado.append(caracterCifrado);

                claveIndex = (claveIndex + 1) % clave.length();
            } else {
                mensajeCifrado.append(caracter);
            }
        }

        return mensajeCifrado.toString();
    }

    public static String descifrarVigenere(String mensajeCifrado, String clave) {
        StringBuilder mensajeDescifrado = new StringBuilder();
        String alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        clave = clave.toUpperCase();
        int claveIndex = 0;

        for (char caracter : mensajeCifrado.toCharArray()) {
            if (Character.isLetter(caracter)) {
                char caracterUpper = Character.toUpperCase(caracter);
                int fila = alfabeto.indexOf(caracterUpper);
                int columna = alfabeto.indexOf(clave.charAt(claveIndex));

                char caracterDescifrado = alfabeto.charAt((fila - columna + 26) % 26);
                mensajeDescifrado.append(caracterDescifrado);

                claveIndex = (claveIndex + 1) % clave.length();
            } else {
                mensajeDescifrado.append(caracter);
            }
        }

        return mensajeDescifrado.toString();
    }

    public static void main(String[] args) {
        String mensaje = "CRIPTOGRAFIA";
        String clave = "OCTAVO";
        System.out.println("Cadena de Caracteres Ingresada: "+ mensaje);
        System.out.println("Clave: "+clave);

        String mensajeCifrado = cifrarVigenere(mensaje, clave);
        System.out.println("Mensaje cifrado: " + mensajeCifrado);

        String mensajeDescifrado = descifrarVigenere(mensajeCifrado, clave);
        System.out.println("Mensaje descifrado: " + mensajeDescifrado);
    }
}