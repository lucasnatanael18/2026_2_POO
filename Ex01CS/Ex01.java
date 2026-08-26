import java.util.Scanner;

public class Ex01 {
    public static void main(String [] args) {
        Scanner scanner = new Scanner(System.in);

        String nome;

        System.out.print("Digite seu nome: ");
        nome = scanner.next();

        System.out.println("Olá, " + nome);
        
        scanner.close();
    }
}

//javac Ex01.Java