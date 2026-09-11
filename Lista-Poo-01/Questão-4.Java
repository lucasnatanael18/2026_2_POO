import java.util.*;

class EntradaCinema {
    String dia;
    int horario;

    double calcularInteira() {
        double valor;
        
        if (dia.equalsIgnoreCase("Quarta")) {
            return 8.00;
        }
        
        if (dia.equalsIgnoreCase("Segunda") || dia.equalsIgnoreCase("Terça") || dia.equalsIgnoreCase("Quinta")) {
            valor = 16.00;
        } else {
            valor = 20.00; 
        }

        if (horario >= 17) {
            valor = valor * 1.5;
        }
        
        return valor;
    }

    double calcularMeia() {
        if (dia.equalsIgnoreCase("Quarta")) {
            return 8.00;
        }
        return calcularInteira() / 2;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        EntradaCinema ingresso = new EntradaCinema();

        System.out.println("Digite o dia da sessão (ex: Segunda, Quarta, Sexta): ");
        ingresso.dia = entrada.nextLine();

        System.out.println("Digite o horario da sessão: ");
        ingresso.horario = entrada.nextInt();

        System.out.println("Dia: " + ingresso.dia);
        System.out.println("Horario: " + ingresso.horario + "h");
        System.out.printf("Entrada inteira: R$ %.2f%n", ingresso.calcularInteira());
        System.out.printf("Meia-Entrada: R$ %.2f%n", ingresso.calcularMeia());

        entrada.close();
    }
}
