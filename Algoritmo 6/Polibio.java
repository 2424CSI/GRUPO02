package com.cs.gr1.algoritmo;

public class Polibio {

    private final char[][] tablaCifrado;
    public Polibio(char[][] tablaCifrado){ //ingresa la tabla
        this.tablaCifrado=tablaCifrado;

    }


    public String cifrar(String cadena){
        StringBuilder cadenaCifrada = new StringBuilder();
        for (char c : cadena.toCharArray()) { //for each para recorrer la cadena a encriptar
            boolean encontrado = false;
            for (int i = 0; i < tablaCifrado.length; i++) {
                for (int j = 0; j < tablaCifrado[i].length; j++) {
                    if (tablaCifrado[i][j] == c) {
                        //Entonces si el elemento de la tabla coincide con el carácter,
                        // yo agrego al StringBuilder las coordenadas de la tabla.
                        cadenaCifrada.append(tablaCifrado[i][0]).append(tablaCifrado[0][j]);
                        encontrado = true;
                        break;
                    }
                }
                if (encontrado) {
                    break;
                }
            }
            if (!encontrado) {
                //si no se llega a encontrar agrego **
                cadenaCifrada.append("**");
            }
        }
        return cadenaCifrada.toString();
    }


    public char[][] getTablaCifrado() {
        return tablaCifrado;
    }
}
