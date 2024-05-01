package com.cs.gr1.algoritmo;


import java.util.Scanner;

public class Literal6 {
    public static void main(String[] args) {

        Scanner scan=new Scanner(System.in);
        System.out.print("Ingrese la cadena a encriptar: ");
        String cadena = scan.nextLine();

        System.out.println();

        char[][] tablaCifrado = new char[6][6]; //Inicializo la tabla de encriptado

        tablaCifrado[0][0]='*';
        tablaCifrado[0][1]='A';
        tablaCifrado[0][2]='S';
        tablaCifrado[0][3]='D';
        tablaCifrado[0][4]='F';
        tablaCifrado[0][5]='G';

        tablaCifrado[1][0]='Q';
        tablaCifrado[1][1]='a';
        tablaCifrado[1][2]='b';
        tablaCifrado[1][3]='c';
        tablaCifrado[1][4]='d';
        tablaCifrado[1][5]='e';

        tablaCifrado[2][0]='W';
        tablaCifrado[2][1]='f';
        tablaCifrado[2][2]='g';
        tablaCifrado[2][3]='h';
        tablaCifrado[2][4]='i';
        tablaCifrado[2][5]='j';

        tablaCifrado[3][0]='E';
        tablaCifrado[3][1]='k';
        tablaCifrado[3][2]='l';
        tablaCifrado[3][3]='m';
        tablaCifrado[3][4]='n';
        tablaCifrado[3][5]='o';

        tablaCifrado[4][0]='R';
        tablaCifrado[4][1]='p';
        tablaCifrado[4][2]='q';
        tablaCifrado[4][3]='r';
        tablaCifrado[4][4]='s';
        tablaCifrado[4][5]='t';

        tablaCifrado[5][0]='T';
        tablaCifrado[5][1]='u';
        tablaCifrado[5][2]='v';
        tablaCifrado[5][3]='x';
        tablaCifrado[5][4]='y';
        tablaCifrado[5][5]='z';


        Polibio cifrado=new Polibio(tablaCifrado);
        String cadenaCifrada=cifrado.cifrar(cadena); //llamado al método


        System.out.println("Tabla de cifrado: ");
        for(int i = 0; i < 6; i++) { //Impresión de la tabla
            for(int j = 0; j < 6; j++) {
                System.out.print(cifrado.getTablaCifrado()[i][j] + "  ");
            }
            System.out.println();
        }

        System.out.println("Mensaje Original: " + cadena);
        System.out.println("Mensaje Cifrado: " + cadenaCifrada);

    }
}